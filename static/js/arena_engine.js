/**
 * arena_engine.js - Đấu Trường Phản Xạ 2 Phút (Speed Arena Engine)
 * Bao phủ đầy đủ 9 Dạng Bài Tập, Giới hạn 2 lượt/ngày, Bộ lọc theo tiến độ & Bộ chấm dịch đa tầng.
 */

// =============================================================================
// 1. BỘ CHẤM ĐIỂM DỊCH ĐA TẦNG & TỔ HỢP ĐỒNG NGHĨA (FLEXIBLE TRANSLATION GRADER)
// =============================================================================

function normalizeArenaText(str, lang = 'de') {
    if (!str) return '';
    let s = String(str).toLowerCase().trim();
    // Xóa toàn bộ dấu câu ở đầu/cuối và chuẩn hóa khoảng trắng
    s = s.replace(/[.,!?;"'„“”«»()[\]{}/\\~`–—\-]+/g, ' ').replace(/\s+/g, ' ').trim();
    if (lang === 'de') {
        // Hỗ trợ người dùng không có bàn phím Đức gõ ae, oe, ue, ss
        s = s.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss');
        const numMap = {
            'eins': '1', 'zwei': '2', 'drei': '3', 'vier': '4', 'fuenf': '5', 'fünf': '5',
            'sechs': '6', 'sieben': '7', 'acht': '8', 'neun': '9', 'zehn': '10'
        };
        Object.keys(numMap).forEach(word => {
            s = s.replace(new RegExp(`\\b${word}\\b`, 'g'), numMap[word]);
        });
    }
    return s;
}

function cleanVietnameseStopwords(str) {
    if (!str) return '';
    let s = String(str).toLowerCase().trim();
    s = s.replace(/[.,!?;"'„“”«»()[\]{}/\\~`–—\-]+/g, ' ').replace(/\s+/g, ' ').trim();

    // Lược bỏ lượng từ đồ vật không bắt buộc
    const classifiers = ['cái', 'chiếc', 'quyển', 'cuốn', 'tờ', 'bức', 'ngôi', 'căn', 'quả', 'trái', 'ly', 'cốc', 'tách', 'chai'];
    classifiers.forEach(c => {
        s = s.replace(new RegExp(`\\b${c}\\b`, 'g'), ' ');
    });

    // Lược bỏ từ đệm / trợ từ nối
    const particles = ['thì', 'là', 'mà', 'rất', 'khá', 'nhé', 'nha', 'ạ', 'vậy', 'đấy', 'đó', 'một'];
    particles.forEach(p => {
        s = s.replace(new RegExp(`\\b${p}\\b`, 'g'), ' ');
    });

    // Quy đổi từ đồng nghĩa tiếng Việt về token chuẩn
    const synonyms = [
        [/\b(phòng bếp|căn bếp|nhà bếp)\b/g, 'bếp'],
        [/\b(kệ sách|giá sách|tủ sách)\b/g, 'tủ sách'],
        [/\b(viết bi|cây bút bi|bút bi)\b/g, 'bút bi'],
        [/\b(cục gôm|cục tẩy|gôm)\b/g, 'tẩy'],
        [/\b(điện thoại di động|di động|dế yêu)\b/g, 'điện thoại'],
        [/\b(ti vi|ti-vi|vô tuyến|màn hình tivi)\b/g, 'tivi'],
        [/\b(trả tiền|tính tiền)\b/g, 'thanh toán'],
        [/\b(ở phía bắc|nằm ở phía bắc|nằm về phía bắc|ở miền bắc)\b/g, 'miền bắc'],
        [/\b(ở phía nam|nằm ở phía nam|nằm về phía nam|ở miền nam)\b/g, 'miền nam'],
        [/\b(ở phía đông|nằm ở phía đông|ở miền đông)\b/g, 'miền đông'],
        [/\b(ở phía tây|nằm ở phía tây|ở miền tây)\b/g, 'miền tây'],
        [/\b(ở miền trung|nằm ở miền trung)\b/g, 'miền trung'],
        [/\b(mình|tớ|tôi|em|anh|chị)\b/g, 'tôi'],
        [/\b(cậu|bạn|anh|chị|mày)\b/g, 'bạn'],
        [/\b(chúng mình|chúng ta|tụi mình|bọn mình|bọn tôi)\b/g, 'chúng tôi']
    ];
    synonyms.forEach(([rgx, rep]) => {
        s = s.replace(rgx, rep);
    });

    return s.replace(/\s+/g, ' ').trim();
}

function evaluateFlexibleTranslation(userAns, acceptedList, lang = 'de') {
    if (!userAns) return false;
    if (!acceptedList || !Array.isArray(acceptedList) || acceptedList.length === 0) return false;

    // 1. So khớp trực tiếp sau chuẩn hóa chuỗi & Umlaut
    const normUser = normalizeArenaText(userAns, lang);
    for (const acc of acceptedList) {
        if (normUser === normalizeArenaText(acc, lang)) return true;
    }

    if (lang === 'vi') {
        const cleanUserVi = cleanVietnameseStopwords(userAns);
        for (const acc of acceptedList) {
            const cleanAccVi = cleanVietnameseStopwords(acc);
            if (cleanUserVi === cleanAccVi) return true;
            // Chấp nhận nếu bao hàm cụm cốt lõi có nghĩa
            if (cleanUserVi.length >= 6 && cleanAccVi.length >= 6) {
                if (cleanUserVi.includes(cleanAccVi) || cleanAccVi.includes(cleanUserVi)) return true;
            }
        }
    } else if (lang === 'de') {
        // Lược bỏ mạo từ der/die/das/ein/eine khi người học dịch từ vựng
        const stripArt = (s) => normalizeArenaText(s, 'de').replace(/^(der|die|das|den|dem|ein|eine|einen|einem|kein|keine|keinen)\s+/, '');
        const uStripped = stripArt(userAns);
        for (const acc of acceptedList) {
            if (uStripped === stripArt(acc)) return true;
        }

        // Tận dụng thêm engine checkGermanAnswerEquivalence nếu có sẵn
        if (typeof checkGermanAnswerEquivalence === 'function') {
            for (const acc of acceptedList) {
                if (checkGermanAnswerEquivalence(userAns, acc)) return true;
            }
        }
    }

    return false;
}

// =============================================================================
// 2. HIỆU ỨNG ÂM THANH PHẢN HỒI (WEB AUDIO API CHIME)
// =============================================================================

function playAudioFeedback(isCorrect) {
    try {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;
        const ctx = new AudioCtx();

        if (isCorrect) {
            // Chuông ngân 2 nốt cao tích cực (587Hz -> 880Hz)
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.type = 'sine';
            osc.frequency.setValueAtTime(587.33, ctx.currentTime);
            osc.frequency.setValueAtTime(880, ctx.currentTime + 0.08);
            gain.gain.setValueAtTime(0.18, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
            osc.start();
            osc.stop(ctx.currentTime + 0.35);
        } else {
            // Âm cảnh báo trầm (220Hz -> 180Hz)
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(220, ctx.currentTime);
            osc.frequency.setValueAtTime(180, ctx.currentTime + 0.1);
            gain.gain.setValueAtTime(0.18, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.28);
            osc.start();
            osc.stop(ctx.currentTime + 0.28);
        }
    } catch (e) {}
}

// =============================================================================
// 3. BIẾN TRẠNG THÁI TOÀN CỤC ĐẤU TRƯỜNG & TÀI KHOẢN
// =============================================================================

let currentAuthUser = null;
let arenaSessionToken = null;
let arenaTimerInterval = null;
let arenaTimeLeft = 120; // 2 phút = 120 giây
let arenaCurrentScore = 0;
let arenaQuestions = [];
let arenaCurrentIndex = 0;
let arenaCorrectCount = 0;
let arenaWrongCount = 0;
let arenaBreakdown = {};
let arenaMatchingPairsState = {
    selectedLeft: null,
    pairsMap: {} // { leftIndex: rightIndex }
};

// =============================================================================
// 4. KHỞI TẠO VÀ KIỂM TRA PHIÊN ĐĂNG NHẬP (AUTH FLOW)
// =============================================================================

async function checkCurrentAuthSession() {
    try {
        const res = await fetch('/api/auth/me');
        const data = await res.json();
        if (data.logged_in && data.user) {
            currentAuthUser = data.user;
            if (data.user.token) localStorage.setItem('dm_auth_token', data.user.token);
            if (data.user.progress && typeof window.userLessonsProgress !== 'undefined') {
                window.userLessonsProgress = Object.assign(window.userLessonsProgress || {}, data.user.progress);
                if (typeof saveLocalLessonsProgress === 'function') saveLocalLessonsProgress();
                if (typeof renderLessonList === 'function') renderLessonList();
                if (typeof updateLessonProgressUI === 'function') updateLessonProgressUI();
            }
            renderAuthUserUI();
            return;
        }

        // Tự động khôi phục tài khoản vĩnh viễn từ localStorage nếu cookie phiên bị trình duyệt xóa
        const savedToken = localStorage.getItem('dm_auth_token');
        if (savedToken) {
            const restRes = await fetch('/api/auth/restore-session', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ token: savedToken })
            });
            if (restRes.ok) {
                const restData = await restRes.json();
                if (restData.logged_in && restData.user) {
                    currentAuthUser = restData.user;
                    if (restData.user.progress && typeof window.userLessonsProgress !== 'undefined') {
                        window.userLessonsProgress = Object.assign(window.userLessonsProgress || {}, restData.user.progress);
                        if (typeof saveLocalLessonsProgress === 'function') saveLocalLessonsProgress();
                        if (typeof renderLessonList === 'function') renderLessonList();
                        if (typeof updateLessonProgressUI === 'function') updateLessonProgressUI();
                    }
                    renderAuthUserUI();
                    return;
                }
            }
        }

        currentAuthUser = null;
        renderAuthUserUI();
    } catch (e) {
        currentAuthUser = null;
        renderAuthUserUI();
    }
}

function renderAuthUserUI() {
    window.currentAuthUser = currentAuthUser;
    const authContainer = document.getElementById('auth-header-container');
    if (!authContainer) return;

    if (currentAuthUser) {
        if (typeof updateExpUI === 'function') {
            updateExpUI(currentAuthUser.total_exp);
        }
        const initials = (currentAuthUser.username || 'HV').substring(0, 2).toUpperCase();
        const rem = currentAuthUser.arena_remaining_today !== undefined ? currentAuthUser.arena_remaining_today : 2;
        authContainer.innerHTML = `
            <div class="flex items-center gap-2 sm:gap-2.5">
                <div class="px-2.5 sm:px-3 py-1.5 rounded-xl bg-orange-50 border border-orange-200 text-orange-700 text-xs sm:text-sm font-bold flex items-center gap-1">
                    🔥 <span id="user-streak">${currentAuthUser.streak_days || 1}</span> ngày
                </div>
                <div class="px-2.5 sm:px-3.5 py-1.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-700 text-xs sm:text-sm font-extrabold flex items-center gap-1">
                    ⚡ <span id="user-exp">${(currentAuthUser.total_exp || 0).toLocaleString('en-US')}</span> EXP
                </div>
                <div class="hidden sm:flex items-center px-2.5 py-1.5 rounded-xl bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold">
                    🎟️ Đấu trường: ${rem}/2 lượt
                </div>
                <div class="relative group">
                    <button class="flex items-center gap-2 px-2.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 border border-slate-300/80 text-slate-800 text-xs font-bold transition cursor-pointer shadow-xs">
                        <span class="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-[10px] font-black">${initials}</span>
                        <span class="max-w-[130px] truncate flex items-center gap-1">
                            <span>${currentAuthUser.username}</span>
                            <span class="text-indigo-600 font-extrabold text-[11px]">(ID: #${currentAuthUser.id})</span>
                        </span>
                    </button>
                    <div class="hidden group-hover:block absolute right-0 top-full pt-1.5 w-52 z-50">
                        <div class="bg-white rounded-2xl shadow-xl border border-slate-200 p-3 text-xs space-y-2.5">
                            <div class="font-bold text-slate-900 border-b border-slate-100 pb-2">
                                <div class="flex items-center justify-between">
                                    <span class="font-black text-sm text-slate-900">👤 ${currentAuthUser.username}</span>
                                    <span class="px-2 py-0.5 rounded-md bg-indigo-100 text-indigo-700 font-mono text-[10px] font-extrabold">ID: #${currentAuthUser.id}</span>
                                </div>
                                <div class="text-[11px] text-slate-500 font-normal mt-0.5">Cấp độ: ${currentAuthUser.highest_level_code || 'A1'} - Bài ${currentAuthUser.highest_lesson_order || 1}</div>
                            </div>
                            <div class="text-slate-600 space-y-1">
                                <div>⚡ Tổng tích luỹ: <b class="text-amber-600">${(currentAuthUser.total_exp || 0).toLocaleString('en-US')} EXP</b></div>
                                <div>🏆 Kỷ lục: <b>${currentAuthUser.arena_best_score || 0}đ</b></div>
                                <div>🎟️ Lượt hôm nay: <b>${rem}/2</b></div>
                            </div>
                            <button onclick="handleUserLogout()" class="w-full text-left px-2.5 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-700 font-bold transition cursor-pointer">
                                🚪 Đăng xuất
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    } else {
        const guestExp = (typeof window.userTotalExp === 'number') ? window.userTotalExp : (parseInt(localStorage.getItem('dm_guest_exp') || '0', 10));
        authContainer.innerHTML = `
            <div class="flex items-center gap-2 sm:gap-3">
                <div class="px-2.5 sm:px-3 py-1.5 rounded-xl bg-orange-50 border border-orange-200 text-orange-700 text-xs sm:text-sm font-bold flex items-center gap-1">
                    🔥 <span id="user-streak">1</span> ngày
                </div>
                <div class="px-2.5 sm:px-3.5 py-1.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-700 text-xs sm:text-sm font-extrabold flex items-center gap-1">
                    ⚡ <span id="user-exp">${guestExp.toLocaleString('en-US')}</span> EXP
                </div>
                <button onclick="openAuthModal('login')" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 active:scale-95 text-white font-extrabold text-xs sm:text-sm shadow-sm transition flex items-center gap-1.5 cursor-pointer">
                    🔐 <span>Đăng nhập / Đua Top</span>
                </button>
            </div>
        `;
    }

    updateArenaHeaderBadge();
}

function updateArenaHeaderBadge() {
    const attemptsBadge = document.getElementById('arena-attempts-badge');
    const startBtn = document.getElementById('arena-start-btn');
    if (!attemptsBadge) return;

    if (currentAuthUser) {
        const rem = currentAuthUser.arena_remaining_today !== undefined ? currentAuthUser.arena_remaining_today : 2;
        attemptsBadge.innerText = `${rem}/2`;
        if (startBtn) {
            if (rem <= 0) {
                startBtn.disabled = true;
                startBtn.className = "px-6 py-3 rounded-2xl bg-slate-300 text-slate-500 font-bold text-sm cursor-not-allowed shadow-none";
                startBtn.innerHTML = "🎟️ Đã hết 2 lượt hôm nay (Reset 00:00)";
            } else {
                startBtn.disabled = false;
                startBtn.className = "px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-md transition cursor-pointer active:scale-95";
                startBtn.innerHTML = "⚔️ Bắt đầu ván đấu (120 giây)";
            }
        }
    } else {
        attemptsBadge.innerText = "2/2 (Khách)";
        if (startBtn) {
            startBtn.disabled = false;
            startBtn.className = "px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-md transition cursor-pointer active:scale-95";
            startBtn.innerHTML = "🔐 Đăng nhập để thi đấu";
        }
    }
}

// =============================================================================
// 5. MODAL ĐĂNG NHẬP / ĐĂNG KÝ
// =============================================================================

function openAuthModal(mode = 'login') {
    const modal = document.getElementById('auth-modal');
    if (!modal) return;
    modal.classList.remove('hidden');
    switchAuthTab(mode);
}

function closeAuthModal() {
    const modal = document.getElementById('auth-modal');
    if (modal) modal.classList.add('hidden');
}

function switchAuthTab(mode) {
    const loginTab = document.getElementById('auth-tab-login');
    const regTab = document.getElementById('auth-tab-reg');
    const loginForm = document.getElementById('auth-form-login');
    const regForm = document.getElementById('auth-form-reg');

    if (mode === 'login') {
        loginTab.className = "flex-1 py-2.5 font-extrabold text-sm border-b-2 border-indigo-600 text-indigo-600 transition";
        regTab.className = "flex-1 py-2.5 font-bold text-sm border-b-2 border-transparent text-slate-400 hover:text-slate-600 transition";
        loginForm.classList.remove('hidden');
        regForm.classList.add('hidden');
        setTimeout(() => document.getElementById('login-username')?.focus(), 100);
    } else {
        regTab.className = "flex-1 py-2.5 font-extrabold text-sm border-b-2 border-indigo-600 text-indigo-600 transition";
        loginTab.className = "flex-1 py-2.5 font-bold text-sm border-b-2 border-transparent text-slate-400 hover:text-slate-600 transition";
        regForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
        setTimeout(() => document.getElementById('reg-username')?.focus(), 100);
    }
}

let checkUserTimeout = null;
function handleUsernameInputChange(val) {
    clearTimeout(checkUserTimeout);
    const feedback = document.getElementById('reg-username-feedback');
    if (!feedback) return;

    const trimmed = (val || '').trim();
    if (trimmed.length === 0) {
        feedback.innerText = "";
        return;
    }
    if (trimmed.length < 4) {
        feedback.className = "text-xs font-semibold text-amber-600 mt-1";
        feedback.innerText = "⚠️ Tên tài khoản phải từ 4 đến 24 ký tự.";
        return;
    }
    if (!/^[a-zA-Z0-9_]{4,24}$/.test(trimmed)) {
        feedback.className = "text-xs font-semibold text-rose-600 mt-1";
        feedback.innerText = "❌ Chỉ dùng chữ cái không dấu, chữ số và gạch dưới (_).";
        return;
    }

    feedback.className = "text-xs text-slate-400 mt-1";
    feedback.innerText = "⏳ Đang kiểm tra tên...";

    checkUserTimeout = setTimeout(async () => {
        try {
            const res = await fetch(`/api/auth/check-username?username=${encodeURIComponent(trimmed)}`);
            const data = await res.json();
            if (data.available) {
                feedback.className = "text-xs font-bold text-emerald-600 mt-1";
                feedback.innerText = "✅ Tên tài khoản hợp lệ & có thể sử dụng!";
            } else {
                feedback.className = "text-xs font-bold text-rose-600 mt-1";
                feedback.innerText = `❌ Tên '${trimmed}' đã tồn tại! Vui lòng chọn tên khác.`;
            }
        } catch (e) {}
    }, 300);
}

function togglePasswordVisibility(inputId, btn) {
    const input = document.getElementById(inputId);
    if (!input) return;
    if (input.type === 'password') {
        input.type = 'text';
        btn.innerText = '🙈';
    } else {
        input.type = 'password';
        btn.innerText = '👁️';
    }
}

async function handleRegisterFormSubmit(e) {
    e.preventDefault();
    const username = document.getElementById('reg-username').value.trim();
    const password = document.getElementById('reg-password').value;
    const errBox = document.getElementById('reg-error-box');
    errBox.classList.add('hidden');

    if (username.length < 4) {
        errBox.innerText = "Tên tài khoản phải từ 4 ký tự trở lên!";
        errBox.classList.remove('hidden');
        return;
    }
    if (password.length < 8) {
        errBox.innerText = "Mật khẩu phải có tối thiểu 8 ký tự!";
        errBox.classList.remove('hidden');
        return;
    }

    // Lấy EXP tích luỹ hiện tại và tiến độ của khách để kế thừa vĩnh viễn vào tài khoản mới
    const currentExp = (typeof window.userTotalExp === 'number') ? window.userTotalExp : 0;
    let guestProg = {};
    try {
        const rawP = localStorage.getItem('dm_lessons_progress_guest');
        if (rawP) guestProg = JSON.parse(rawP);
    } catch (err) {}

    try {
        const res = await fetch('/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username,
                password,
                initial_exp: currentExp,
                guest_progress: guestProg
            })
        });
        const data = await res.json();
        if (res.ok) {
            currentAuthUser = data.user;
            if (data.token || (data.user && data.user.token)) {
                localStorage.setItem('dm_auth_token', data.token || data.user.token);
            }
            if (data.user && data.user.progress && typeof window.userLessonsProgress !== 'undefined') {
                window.userLessonsProgress = Object.assign(window.userLessonsProgress || {}, data.user.progress);
                if (typeof saveLocalLessonsProgress === 'function') saveLocalLessonsProgress();
                if (typeof renderLessonList === 'function') renderLessonList();
                if (typeof updateLessonProgressUI === 'function') updateLessonProgressUI();
            }
            closeAuthModal();
            renderAuthUserUI();
            loadLeaderboardData();

            const myId = (data.user && data.user.id) ? data.user.id : (data.user_id || '');
            alert(`🎉 CHÚC MỪNG ${username} TẠO TÀI KHOẢN THÀNH CÔNG!\n\n` +
                  `🔑 MÃ ID RIÊNG CỦA BẠN: #${myId}\n` +
                  `👤 TÊN ĐĂNG NHẬP: ${username}\n` +
                  `⚡ EXP ĐÃ BẢO LƯU: ${(data.user.total_exp || currentExp).toLocaleString('en-US')} EXP\n\n` +
                  `📌 Hãy ghi nhớ Mã ID (#${myId}) hoặc Tên đăng nhập. Lần sau truy cập lại, bạn chỉ cần nhập Tên đăng nhập (hoặc Mã ID) + Mật khẩu là dữ liệu và tiến độ học sẽ được bảo lưu 100%!`);
        } else {
            errBox.innerText = data.error || "Đăng ký thất bại. Vui lòng thử lại!";
            errBox.classList.remove('hidden');
        }
    } catch (err) {
        errBox.innerText = "Lỗi kết nối máy chủ!";
        errBox.classList.remove('hidden');
    }
}

async function handleLoginFormSubmit(e) {
    e.preventDefault();
    const username = document.getElementById('login-username').value.trim();
    const password = document.getElementById('login-password').value;
    const errBox = document.getElementById('login-error-box');
    errBox.classList.add('hidden');

    try {
        const res = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const data = await res.json();
        if (res.ok) {
            currentAuthUser = data.user;
            if (data.token || (data.user && data.user.token)) {
                localStorage.setItem('dm_auth_token', data.token || data.user.token);
            }
            if (data.user && data.user.progress && typeof window.userLessonsProgress !== 'undefined') {
                window.userLessonsProgress = Object.assign(window.userLessonsProgress || {}, data.user.progress);
                if (typeof saveLocalLessonsProgress === 'function') saveLocalLessonsProgress();
                if (typeof renderLessonList === 'function') renderLessonList();
                if (typeof updateLessonProgressUI === 'function') updateLessonProgressUI();
            }
            closeAuthModal();
            renderAuthUserUI();
            loadLeaderboardData();
        } else {
            if (data.not_found && username) {
                errBox.innerHTML = `
                    <div class="space-y-2 text-left">
                        <div class="font-bold text-amber-300">⚠️ Tài khoản "${username}" chưa tồn tại trên máy chủ mới.</div>
                        <div class="text-[11px] text-slate-200">Bạn có muốn kích hoạt ngay tài khoản này với mật khẩu vừa nhập không? (EXP và tiến trình học trên máy bạn sẽ được bảo lưu 100%)</div>
                        <button type="button" onclick="quickRegisterFromLogin('${username.replace(/'/g, "\\'")}')" class="w-full mt-2 py-2 px-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-extrabold rounded-xl shadow transition cursor-pointer text-xs flex items-center justify-center gap-1.5">
                            ⚡ KÍCH HOẠT & BẢO LƯU TIẾN TRÌNH NGAY
                        </button>
                    </div>
                `;
            } else {
                errBox.innerText = data.error || "Đăng nhập thất bại!";
            }
            errBox.classList.remove('hidden');
        }
    } catch (err) {
        errBox.innerText = "Lỗi kết nối máy chủ!";
        errBox.classList.remove('hidden');
    }
}

async function quickRegisterFromLogin(uname) {
    const password = document.getElementById('login-password').value;
    const errBox = document.getElementById('login-error-box');
    if (!password || password.length < 8) {
        alert("Vui lòng nhập mật khẩu tối thiểu 8 ký tự vào ô mật khẩu trước khi kích hoạt!");
        return;
    }
    const currentExp = (typeof userTotalExp !== 'undefined') ? userTotalExp : 0;
    const currentProgress = (typeof userLessonsProgress !== 'undefined') ? userLessonsProgress : {};

    try {
        const res = await fetch('/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username: uname,
                password: password,
                initial_exp: currentExp,
                guest_progress: currentProgress
            })
        });
        const data = await res.json();
        if (res.ok) {
            currentAuthUser = data.user;
            if (data.token || (data.user && data.user.token)) {
                localStorage.setItem('dm_auth_token', data.token || data.user.token);
            }
            if (data.user && data.user.progress && typeof window.userLessonsProgress !== 'undefined') {
                window.userLessonsProgress = Object.assign(window.userLessonsProgress || {}, data.user.progress);
                if (typeof saveLocalLessonsProgress === 'function') saveLocalLessonsProgress();
                if (typeof renderLessonList === 'function') renderLessonList();
                if (typeof updateLessonProgressUI === 'function') updateLessonProgressUI();
            }
            closeAuthModal();
            renderAuthUserUI();
            loadLeaderboardData();

            const myId = (data.user && data.user.id) ? data.user.id : (data.user_id || '');
            alert(`🎉 CHÚC MỪNG ${uname} ĐÃ KÍCH HOẠT TÀI KHOẢN THÀNH CÔNG!\n\n` +
                  `🔑 MÃ ID RIÊNG: #${myId}\n` +
                  `👤 TÊN ĐĂNG NHẬP: ${uname}\n` +
                  `⚡ EXP BẢO LƯU: ${(data.user.total_exp || currentExp).toLocaleString('en-US')} EXP\n\n` +
                  `📌 Lần sau truy cập lại, bạn chỉ cần nhập Tên đăng nhập (hoặc Mã ID #${myId}) + Mật khẩu này!`);
        } else {
            errBox.innerText = data.error || "Kích hoạt thất bại. Vui lòng thử lại!";
            errBox.classList.remove('hidden');
        }
    } catch (err) {
        errBox.innerText = "Lỗi kết nối máy chủ!";
        errBox.classList.remove('hidden');
    }
}

async function handleUserLogout() {
    try {
        localStorage.removeItem('dm_auth_token');
        await fetch('/api/auth/logout', { method: 'POST' });
        currentAuthUser = null;
        if (typeof window.userLessonsProgress !== 'undefined') {
            window.userLessonsProgress = {};
            if (typeof loadLessonsProgress === 'function') loadLessonsProgress();
        }
        renderAuthUserUI();
        initArenaLobbyScreen();
        loadLeaderboardData();
    } catch (e) {}
}

// =============================================================================
// 6. KHỞI TẠO MÀN HÌNH CHÍNH ĐẤU TRƯỜNG & LOBBY
// =============================================================================

function initArenaLobbyScreen() {
    clearInterval(arenaTimerInterval);
    arenaTimerInterval = null;
    arenaTimeLeft = 120;
    arenaCurrentScore = 0;

    const timerEl = document.getElementById('arena-timer');
    const scoreEl = document.getElementById('arena-score');
    if (timerEl) {
        timerEl.innerText = "02:00";
        timerEl.className = "font-mono font-extrabold text-slate-800";
    }
    if (scoreEl) scoreEl.innerText = "0";

    const playBox = document.getElementById('arena-play-box');
    if (!playBox) return;

    playBox.innerHTML = `
        <div class="space-y-6 text-center max-w-2xl mx-auto py-2">
            <div class="inline-flex items-center justify-center w-16 h-16 rounded-3xl bg-indigo-100 text-indigo-600 text-3xl shadow-inner">
                ⚔️
            </div>
            <div class="space-y-2">
                <h3 class="text-xl sm:text-2xl font-black text-slate-900">Đấu Trường Phản Xạ Tiếng Đức (2 Phút)</h3>
                <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">
                    Đồng hồ đếm ngược <b>120 giây (02:00)</b> liên tục. Bộ câu hỏi được lọc chính xác theo <b>tiến độ bài học bạn đã mở</b>. Bao phủ đủ <b>9 dạng bài tập</b> với ma trận điểm số thưởng/phạt khắt khe!
                </p>
            </div>

            <!-- Bảng ma trận điểm số Đấu trường -->
            <div class="p-4 rounded-2xl bg-white border border-slate-200 text-left shadow-xs space-y-3">
                <div class="text-xs font-black uppercase text-indigo-700 tracking-wider flex items-center justify-between">
                    <span>📋 Ma trận Điểm Thưởng / Phạt:</span>
                    <span class="text-slate-400 font-semibold normal-case">Học đến đâu - Thi đến đó</span>
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[11px]">
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80">
                        <b>1. Trắc nghiệm:</b> <span class="text-emerald-600 font-bold">+5</span> / <span class="text-rose-600 font-bold">-2</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80">
                        <b>2. Điền khuyết:</b> <span class="text-emerald-600 font-bold">+7</span> / <span class="text-rose-600 font-bold">-3</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80">
                        <b>3. Dịch từ (V ⇄ Đ):</b> <span class="text-emerald-600 font-bold">+6</span> / <span class="text-rose-600 font-bold">-3</span>
                    </div>
                    <div class="p-2 rounded-xl bg-indigo-50/70 border border-indigo-200">
                        <b>4. Nối ô (4 cặp):</b> <span class="text-emerald-600 font-bold">+10</span> / <span class="text-rose-600 font-bold">-4</span>
                    </div>
                    <div class="p-2 rounded-xl bg-amber-50/70 border border-amber-200">
                        <b>5. Dịch câu (V ⇄ Đ):</b> <span class="text-emerald-600 font-bold">+15</span> / <span class="text-rose-600 font-bold">-6</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80">
                        <b>6. Nghe & Điền:</b> <span class="text-emerald-600 font-bold">+10</span> / <span class="text-rose-600 font-bold">-4</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80">
                        <b>7. Điền tạo câu:</b> <span class="text-emerald-600 font-bold">+5</span> / <span class="text-rose-600 font-bold">-2</span>
                    </div>
                    <div class="p-2 rounded-xl bg-emerald-50/70 border border-emerald-300">
                        <b>8. Đọc hiểu đoạn văn:</b> <span class="text-emerald-600 font-bold">+12</span> / <span class="text-rose-600 font-bold">-4</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200/80 col-span-2 sm:col-span-4 text-center text-[10px] text-slate-500">
                        <i>Giới hạn nghiêm ngặt: <b>2 lượt / ngày / tài khoản</b> • Tự động mở khóa câu hỏi theo bài đã học</i>
                    </div>
                </div>
            </div>

            <div class="pt-2">
                <button id="arena-start-btn" onclick="startArenaGame2Min()" class="px-8 py-3.5 rounded-2xl bg-indigo-600 hover:bg-indigo-500 active:scale-95 text-white font-extrabold text-sm sm:text-base shadow-lg shadow-indigo-200 transition cursor-pointer">
                    ⚔️ Bắt đầu ván đấu (120 giây)
                </button>
            </div>
        </div>
    `;

    updateArenaHeaderBadge();
}

// =============================================================================
// 7. VẬN HÀNH VÁN ĐẤU 2 PHÚT (SPEED ARENA ENGINE)
// =============================================================================

async function startArenaGame2Min() {
    if (!currentAuthUser) {
        openAuthModal('login');
        return;
    }

    try {
        const res = await fetch('/api/arena/start', { method: 'POST' });
        const data = await res.json();

        if (!res.ok) {
            alert(data.error || "Không thể bắt đầu ván đấu!");
            return;
        }

        arenaSessionToken = data.session_token;
        arenaQuestions = data.questions || [];
        arenaCurrentIndex = 0;
        arenaCurrentScore = 0;
        arenaCorrectCount = 0;
        arenaWrongCount = 0;
        arenaBreakdown = {};
        arenaTimeLeft = data.duration_seconds || 120;

        if (currentAuthUser) {
            currentAuthUser.arena_remaining_today = data.remaining_today;
            renderAuthUserUI();
        }

        if (arenaQuestions.length === 0) {
            alert("Chưa có đủ câu hỏi cho phạm vi bài học của bạn!");
            initArenaLobbyScreen();
            return;
        }

        // Bắt đầu đồng hồ đếm ngược
        startArenaTimer();
        renderCurrentArenaQuestion();
    } catch (e) {
        alert("Lỗi kết nối máy chủ khi bắt đầu ván đấu!");
    }
}

function startArenaTimer() {
    clearInterval(arenaTimerInterval);
    const timerEl = document.getElementById('arena-timer');

    const updateTimerDisplay = () => {
        const m = Math.floor(arenaTimeLeft / 60);
        const s = arenaTimeLeft % 60;
        const formatted = `${m < 10 ? '0' + m : m}:${s < 10 ? '0' + s : s}`;
        if (timerEl) {
            timerEl.innerText = formatted;
            if (arenaTimeLeft <= 10) {
                timerEl.className = "font-mono font-black text-rose-600 animate-pulse text-lg";
            } else if (arenaTimeLeft <= 30) {
                timerEl.className = "font-mono font-extrabold text-amber-500 text-lg";
            } else {
                timerEl.className = "font-mono font-extrabold text-slate-800 text-lg";
            }
        }
    };

    updateTimerDisplay();

    arenaTimerInterval = setInterval(() => {
        arenaTimeLeft--;
        updateTimerDisplay();
        if (arenaTimeLeft <= 0) {
            clearInterval(arenaTimerInterval);
            finishArenaGame();
        }
    }, 1000);
}

function showFloatingScore(pts) {
    const box = document.getElementById('arena-floating-score-box');
    if (!box) return;
    const isPositive = pts > 0;
    const el = document.createElement('div');
    el.className = `absolute right-2 top-0 font-black text-sm sm:text-base pointer-events-none transition-all duration-700 transform -translate-y-4 opacity-100 ${isPositive ? 'text-emerald-600' : 'text-rose-600'}`;
    el.innerText = `${isPositive ? '+' : ''}${pts}`;
    box.appendChild(el);

    setTimeout(() => {
        el.classList.add('-translate-y-10', 'opacity-0');
    }, 50);
    setTimeout(() => {
        el.remove();
    }, 750);
}

function renderCurrentArenaQuestion() {
    if (arenaTimeLeft <= 0 || arenaCurrentIndex >= arenaQuestions.length) {
        finishArenaGame();
        return;
    }

    const q = arenaQuestions[arenaCurrentIndex];
    const playBox = document.getElementById('arena-play-box');
    if (!playBox) return;

    let inputAreaHtml = '';

    // Dạng 1: Trắc nghiệm (4 options) hoặc Đọc hiểu đoạn văn có options
    if (q.type === 'trac_nghiem' || (q.type === 'doc_hieu' && q.options && q.options.length > 0)) {
        const opts = (q.options && q.options.length > 0) ? q.options : ["A", "B", "C", "D"];
        inputAreaHtml = `
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-4">
                ${opts.map((opt, optIdx) => {
                    const letter = String.fromCharCode(65 + optIdx);
                    return `
                        <button onclick="handleArenaAnswer('${opt.replace(/'/g, "\\'")}')" class="text-left px-5 py-3.5 rounded-2xl bg-white hover:bg-indigo-600 hover:text-white border border-slate-200 hover:border-indigo-600 text-sm font-bold text-slate-800 shadow-sm transition flex items-center gap-3 group cursor-pointer active:scale-95">
                            <span class="w-7 h-7 rounded-xl bg-slate-100 group-hover:bg-indigo-700 text-slate-700 group-hover:text-white font-black text-xs flex items-center justify-center shrink-0 border border-slate-200 group-hover:border-indigo-500">${letter}</span>
                            <span class="pt-0.5">${opt}</span>
                        </button>
                    `;
                }).join('')}
            </div>
        `;
    }
    // Dạng 5: Nối ô 4 cặp (noi_o)
    else if (q.type === 'noi_o') {
        arenaMatchingPairsState = { selectedLeft: null, pairsMap: {} };
        const leftItems = q.left_items || [];
        const rightItems = q.right_items || [];
        inputAreaHtml = `
            <div class="space-y-4 mt-4">
                <div class="text-xs text-slate-500 font-medium">Bấm 1 ô bên trái rồi bấm 1 ô bên phải để ghép cặp:</div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="space-y-2">
                        <div class="text-xs font-bold text-slate-400 uppercase">Cột Trái</div>
                        ${leftItems.map((item, idx) => `
                            <button id="match-l-${idx}" onclick="handleMatchingClick('left', ${idx})" class="w-full text-left p-3 rounded-xl bg-white border-2 border-slate-200 text-xs sm:text-sm font-bold text-slate-800 shadow-xs transition cursor-pointer flex items-center justify-between">
                                <span>${item}</span>
                                <span id="match-l-badge-${idx}" class="text-[10px] px-1.5 py-0.5 rounded font-black hidden"></span>
                            </button>
                        `).join('')}
                    </div>
                    <div class="space-y-2">
                        <div class="text-xs font-bold text-slate-400 uppercase">Cột Phải (Xáo trộn)</div>
                        ${rightItems.map((item, idx) => `
                            <button id="match-r-${idx}" onclick="handleMatchingClick('right', ${idx})" class="w-full text-left p-3 rounded-xl bg-white border-2 border-slate-200 text-xs sm:text-sm font-bold text-slate-800 shadow-xs transition cursor-pointer flex items-center justify-between">
                                <span>${item}</span>
                                <span id="match-r-badge-${idx}" class="text-[10px] px-1.5 py-0.5 rounded font-black hidden"></span>
                            </button>
                        `).join('')}
                    </div>
                </div>
                <div class="flex justify-end pt-2">
                    <button id="match-confirm-btn" onclick="confirmMatchingPairs()" disabled class="px-6 py-2.5 rounded-xl bg-slate-200 text-slate-400 font-bold text-xs cursor-not-allowed transition">
                        Nối đủ 4 cặp để xác nhận
                    </button>
                </div>
            </div>
        `;
    }
    // Dạng 8: Nghe & Điền (nghe_dien)
    else if (q.type === 'nghe_dien') {
        const textToSpeak = (q.audio_text || q.correct_answer || '').replace(/'/g, "\\'");
        inputAreaHtml = `
            <div class="space-y-3 mt-4">
                <div class="flex flex-wrap gap-2">
                    <button onclick="speakGerman('${textToSpeak}', 1.0)" class="px-4 py-2 rounded-xl bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 text-xs font-bold flex items-center gap-1.5 cursor-pointer">
                        🔊 Nghe chuẩn (1.0x)
                    </button>
                    <button onclick="speakGerman('${textToSpeak}', 0.65)" class="px-4 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-200 text-xs font-bold flex items-center gap-1.5 cursor-pointer">
                        🐢 Nghe chậm (0.65x)
                    </button>
                </div>
                <div class="p-3.5 rounded-2xl bg-indigo-50/60 border border-indigo-200 text-indigo-950 font-bold text-sm sm:text-base">
                    ${q.display_sentence || q.question}
                </div>
                ${q.hint_vi ? `<div class="text-xs text-slate-500 font-medium italic">Gợi ý nghĩa: „${q.hint_vi}“</div>` : ''}
                <div class="flex gap-2">
                    <input id="arena-text-input" onkeydown="handleArenaInputKeydown(event)" type="text" placeholder="Gõ từ nghe được (nhấn Enter để gửi)..." class="flex-1 px-4 py-3 rounded-2xl bg-white border border-slate-300 text-sm font-semibold focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100">
                    <button onclick="submitArenaTextInput()" class="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm shadow-md transition cursor-pointer">
                        Gửi
                    </button>
                </div>
            </div>
        `;
        setTimeout(() => {
            speakGerman(q.audio_text || q.correct_answer, 1.0);
        }, 150);
    }
    // Dạng 9: Điền tạo câu (dien_tao_cau)
    else if (q.type === 'dien_tao_cau') {
        const hints = q.word_bank_hints || [];
        inputAreaHtml = `
            <div class="space-y-3 mt-4">
                <div class="p-3.5 rounded-2xl bg-indigo-50/60 border border-indigo-200 text-indigo-950 font-bold text-sm sm:text-base">
                    ${q.display_frame || q.question}
                </div>
                ${hints.length > 0 ? `
                    <div class="flex flex-wrap items-center gap-1.5">
                        <span class="text-xs text-slate-400 font-semibold mr-1">Thẻ từ gợi ý:</span>
                        ${hints.map(w => `
                            <button onclick="insertWordIntoArenaInput('${w.replace(/'/g, "\\'")}')" class="px-3 py-1 rounded-lg bg-white hover:bg-indigo-50 border border-slate-200 hover:border-indigo-300 text-xs font-bold text-slate-700 transition cursor-pointer active:scale-95">
                                + ${w}
                            </button>
                        `).join('')}
                    </div>
                ` : ''}
                <div class="flex gap-2">
                    <input id="arena-text-input" onkeydown="handleArenaInputKeydown(event)" type="text" placeholder="Nhập đáp án hoặc bấm thẻ từ trên (nhấn Enter để gửi)..." class="flex-1 px-4 py-3 rounded-2xl bg-white border border-slate-300 text-sm font-semibold focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100">
                    <button onclick="submitArenaTextInput()" class="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm shadow-md transition cursor-pointer">
                        Gửi
                    </button>
                </div>
            </div>
        `;
    }
    // Các dạng văn bản còn lại (dien_khuyet, dich_nghia_vd, dich_nghia_dv, dich_cau_vd, dich_cau_dv)
    else {
        const placeholder = q.type.includes('_dv') ? "Nhập bản dịch tiếng Việt..." : "Nhập đáp án tiếng Đức...";
        inputAreaHtml = `
            <div class="space-y-3 mt-4">
                <div class="flex gap-2">
                    <input id="arena-text-input" onkeydown="handleArenaInputKeydown(event)" type="text" placeholder="${placeholder} (nhấn Enter để gửi)" class="flex-1 px-4 py-3 rounded-2xl bg-white border border-slate-300 text-sm font-semibold focus:outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100">
                    <button onclick="submitArenaTextInput()" class="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm shadow-md transition cursor-pointer">
                        Gửi
                    </button>
                </div>
            </div>
        `;
    }

    playBox.innerHTML = `
        <div class="space-y-4">
            <div class="flex items-center justify-between text-xs">
                <span class="px-3 py-1 rounded-full bg-indigo-100 text-indigo-700 font-extrabold uppercase tracking-wide">
                    ${q.type_label || q.type}
                </span>
                <span class="font-extrabold text-slate-500">
                    Đúng: <b class="text-emerald-600">+${q.points_correct}</b> | Sai: <b class="text-rose-600">${q.points_wrong}</b>
                </span>
            </div>

            ${q.passage ? `
                <div class="p-4 rounded-2xl bg-indigo-50/80 border border-indigo-200 text-left text-xs sm:text-sm text-slate-800 leading-relaxed font-medium whitespace-pre-line shadow-xs mb-3">
                    <div class="text-[11px] font-black uppercase text-indigo-700 mb-1.5 flex items-center gap-1.5 tracking-wider">
                        <span>📖 Đoạn văn / Hội thoại:</span>
                    </div>
                    <div class="italic text-slate-900 font-normal leading-relaxed">${q.passage}</div>
                </div>
            ` : ''}

            <h4 class="text-base sm:text-lg font-bold text-slate-900 leading-snug">
                ${q.question}
            </h4>

            ${inputAreaHtml}

            <div id="arena-feedback-row" class="hidden text-xs p-3 rounded-xl mt-2 font-semibold"></div>
        </div>
    `;

    setTimeout(() => {
        const inp = document.getElementById('arena-text-input');
        if (inp) inp.focus();
    }, 60);
}

function handleArenaInputKeydown(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        submitArenaTextInput();
    }
}

function insertWordIntoArenaInput(word) {
    const inp = document.getElementById('arena-text-input');
    if (!inp) return;
    const cur = inp.value.trim();
    inp.value = cur ? `${cur} ${word}` : word;
    inp.focus();
}

function submitArenaTextInput() {
    const inp = document.getElementById('arena-text-input');
    if (!inp) return;
    handleArenaAnswer(inp.value.trim());
}

// Xử lý logic Nối ô 4 cặp
const MATCH_COLORS = [
    { border: 'border-indigo-500', bg: 'bg-indigo-50', text: 'text-indigo-700', badge: 'bg-indigo-600' },
    { border: 'border-emerald-500', bg: 'bg-emerald-50', text: 'text-emerald-700', badge: 'bg-emerald-600' },
    { border: 'border-amber-500', bg: 'bg-amber-50', text: 'text-amber-700', badge: 'bg-amber-600' },
    { border: 'border-purple-500', bg: 'bg-purple-50', text: 'text-purple-700', badge: 'bg-purple-600' }
];

function handleMatchingClick(side, index) {
    const q = arenaQuestions[arenaCurrentIndex];
    if (!q || q.type !== 'noi_o') return;

    if (side === 'left') {
        // Chọn ô bên trái
        arenaMatchingPairsState.selectedLeft = index;
        // Highlight ô trái đang chọn
        for (let i = 0; i < (q.left_items || []).length; i++) {
            const btn = document.getElementById(`match-l-${i}`);
            if (!btn) continue;
            if (i === index) {
                btn.classList.add('ring-2', 'ring-indigo-600', 'border-indigo-600');
            } else {
                btn.classList.remove('ring-2', 'ring-indigo-600');
            }
        }
    } else if (side === 'right') {
        if (arenaMatchingPairsState.selectedLeft === null) return;
        const leftIdx = arenaMatchingPairsState.selectedLeft;
        const rightIdx = index;

        // Nếu rightIdx này đã bị ghép với left khác, gỡ ghép cũ
        for (const [l, r] of Object.entries(arenaMatchingPairsState.pairsMap)) {
            if (r === rightIdx) delete arenaMatchingPairsState.pairsMap[l];
        }

        arenaMatchingPairsState.pairsMap[leftIdx] = rightIdx;
        arenaMatchingPairsState.selectedLeft = null;

        // Cập nhật giao diện màu sắc các cặp
        renderMatchingColors(q);
    }
}

function renderMatchingColors(q) {
    const leftCount = (q.left_items || []).length;
    const rightCount = (q.right_items || []).length;

    // Reset giao diện
    for (let i = 0; i < leftCount; i++) {
        const btn = document.getElementById(`match-l-${i}`);
        const badge = document.getElementById(`match-l-badge-${i}`);
        if (!btn || !badge) continue;
        btn.className = "w-full text-left p-3 rounded-xl bg-white border-2 border-slate-200 text-xs sm:text-sm font-bold text-slate-800 shadow-xs transition cursor-pointer flex items-center justify-between";
        badge.classList.add('hidden');
    }
    for (let j = 0; j < rightCount; j++) {
        const btn = document.getElementById(`match-r-${j}`);
        const badge = document.getElementById(`match-r-badge-${j}`);
        if (!btn || !badge) continue;
        btn.className = "w-full text-left p-3 rounded-xl bg-white border-2 border-slate-200 text-xs sm:text-sm font-bold text-slate-800 shadow-xs transition cursor-pointer flex items-center justify-between";
        badge.classList.add('hidden');
    }

    let pairIdx = 0;
    for (const [l, r] of Object.entries(arenaMatchingPairsState.pairsMap)) {
        const color = MATCH_COLORS[pairIdx % MATCH_COLORS.length];
        const btnL = document.getElementById(`match-l-${l}`);
        const badgeL = document.getElementById(`match-l-badge-${l}`);
        const btnR = document.getElementById(`match-r-${r}`);
        const badgeR = document.getElementById(`match-r-badge-${r}`);

        if (btnL && badgeL) {
            btnL.className = `w-full text-left p-3 rounded-xl ${color.bg} border-2 ${color.border} text-xs sm:text-sm font-bold ${color.text} shadow-xs transition cursor-pointer flex items-center justify-between`;
            badgeL.className = `text-[10px] px-2 py-0.5 rounded-md text-white font-black ${color.badge}`;
            badgeL.innerText = `Cặp #${pairIdx + 1}`;
            badgeL.classList.remove('hidden');
        }
        if (btnR && badgeR) {
            btnR.className = `w-full text-left p-3 rounded-xl ${color.bg} border-2 ${color.border} text-xs sm:text-sm font-bold ${color.text} shadow-xs transition cursor-pointer flex items-center justify-between`;
            badgeR.className = `text-[10px] px-2 py-0.5 rounded-md text-white font-black ${color.badge}`;
            badgeR.innerText = `Cặp #${pairIdx + 1}`;
            badgeR.classList.remove('hidden');
        }
        pairIdx++;
    }

    const confirmBtn = document.getElementById('match-confirm-btn');
    if (confirmBtn) {
        if (Object.keys(arenaMatchingPairsState.pairsMap).length === leftCount) {
            confirmBtn.disabled = false;
            confirmBtn.className = "px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-xs shadow-md transition cursor-pointer active:scale-95";
            confirmBtn.innerText = "Xác nhận nối 4 cặp";
        } else {
            confirmBtn.disabled = true;
            confirmBtn.className = "px-6 py-2.5 rounded-xl bg-slate-200 text-slate-400 font-bold text-xs cursor-not-allowed transition";
            confirmBtn.innerText = `Đã nối ${Object.keys(arenaMatchingPairsState.pairsMap).length}/4 cặp`;
        }
    }
}

function confirmMatchingPairs() {
    const q = arenaQuestions[arenaCurrentIndex];
    if (!q || q.type !== 'noi_o') return;

    const pairs = q.pairs || [];
    let isAllCorrect = true;

    for (let lIdx = 0; lIdx < pairs.length; lIdx++) {
        const rightIdx = arenaMatchingPairsState.pairsMap[lIdx];
        if (rightIdx === undefined) {
            isAllCorrect = false;
            break;
        }
        const userLeftText = q.left_items[lIdx];
        const userRightText = q.right_items[rightIdx];

        // So sánh với định nghĩa chuẩn
        const expectedPair = pairs.find(p => p.left === userLeftText);
        if (!expectedPair || expectedPair.right !== userRightText) {
            isAllCorrect = false;
            break;
        }
    }

    handleArenaAnswer(isAllCorrect ? 'MATCH_CORRECT' : 'MATCH_WRONG');
}

// Xử lý chấm điểm câu hỏi
function handleArenaAnswer(userAnswer) {
    if (arenaTimeLeft <= 0) return;
    const q = arenaQuestions[arenaCurrentIndex];
    if (!q) return;

    let isCorrect = false;

    if (q.type === 'noi_o') {
        isCorrect = (userAnswer === 'MATCH_CORRECT');
    } else if (q.type === 'trac_nghiem') {
        isCorrect = normalizeArenaText(userAnswer, 'de') === normalizeArenaText(q.correct_answer, 'de');
    } else if (q.type === 'dien_khuyet' || q.type === 'nghe_dien') {
        isCorrect = evaluateFlexibleTranslation(userAnswer, q.accepted_answers || [q.correct_answer], 'de');
    } else if (q.type === 'dich_nghia_vd' || q.type === 'dich_cau_vd') {
        isCorrect = evaluateFlexibleTranslation(userAnswer, q.accepted_answers || [q.correct_answer], 'de');
    } else if (q.type === 'dich_nghia_dv' || q.type === 'dich_cau_dv') {
        isCorrect = evaluateFlexibleTranslation(userAnswer, q.accepted_answers || [q.correct_answer], 'vi');
    } else if (q.type === 'doc_hieu') {
        if (q.options && q.options.length > 0) {
            isCorrect = normalizeArenaText(userAnswer, 'de') === normalizeArenaText(q.correct_answer, 'de') ||
                        userAnswer.trim().toLowerCase() === String(q.correct_answer).trim().toLowerCase();
        } else {
            isCorrect = evaluateFlexibleTranslation(userAnswer, q.accepted_answers || [q.correct_answer], 'de');
        }
    } else if (q.type === 'dien_tao_cau') {
        isCorrect = evaluateFlexibleTranslation(userAnswer, q.accepted_answers || [q.correct_answer], 'de');
    }

    const ptsDelta = isCorrect ? q.points_correct : q.points_wrong;
    arenaCurrentScore += ptsDelta;

    if (isCorrect) {
        arenaCorrectCount++;
    } else {
        arenaWrongCount++;
    }

    // Thống kê breakdown theo dạng
    if (!arenaBreakdown[q.type]) arenaBreakdown[q.type] = { correct: 0, wrong: 0 };
    if (isCorrect) arenaBreakdown[q.type].correct++;
    else arenaBreakdown[q.type].wrong++;

    // Cập nhật điểm và hiệu ứng
    const scoreEl = document.getElementById('arena-score');
    if (scoreEl) scoreEl.innerText = arenaCurrentScore;
    showFloatingScore(ptsDelta);
    playAudioFeedback(isCorrect);

    const feedbackRow = document.getElementById('arena-feedback-row');
    if (feedbackRow) {
        feedbackRow.classList.remove('hidden');
        if (isCorrect) {
            feedbackRow.className = "text-xs p-3 rounded-xl mt-3 bg-emerald-50 text-emerald-800 border border-emerald-200 font-bold flex items-center justify-between";
            feedbackRow.innerHTML = `<span>✅ Chính xác! +${q.points_correct} điểm</span><span>${q.translation ? '📖 ' + q.translation : ''}</span>`;
        } else {
            feedbackRow.className = "text-xs p-3 rounded-xl mt-3 bg-rose-50 text-rose-800 border border-rose-200 font-bold flex items-center justify-between";
            feedbackRow.innerHTML = `<span>❌ Chưa đúng (${q.points_wrong} điểm). Đáp án: <b>${q.correct_answer}</b></span><span>${q.translation ? '📖 ' + q.translation : ''}</span>`;
        }
    }

    // Delay trước khi chuyển sang câu tiếp theo (450ms đúng, 900ms sai)
    const delay = isCorrect ? 450 : 900;
    setTimeout(() => {
        arenaCurrentIndex++;
        if (arenaTimeLeft > 0) {
            renderCurrentArenaQuestion();
        }
    }, delay);
}

// =============================================================================
// 8. TỔNG KẾT VÀ LƯU KẾT QUẢ ĐẤU TRƯỜNG
// =============================================================================

async function finishArenaGame() {
    clearInterval(arenaTimerInterval);
    arenaTimerInterval = null;

    const playBox = document.getElementById('arena-play-box');
    if (!playBox) return;

    playBox.innerHTML = `
        <div class="text-center py-6 space-y-4">
            <div class="inline-block animate-spin text-3xl">⏳</div>
            <h3 class="text-lg font-bold text-slate-700">Đang tổng kết ván đấu...</h3>
        </div>
    `;

    try {
        const res = await fetch('/api/arena/finish', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                session_token: arenaSessionToken,
                final_score: arenaCurrentScore,
                correct_count: arenaCorrectCount,
                wrong_count: arenaWrongCount,
                breakdown: arenaBreakdown,
                scope_summary: currentAuthUser ? `${currentAuthUser.highest_level_code} - Bài ${currentAuthUser.highest_lesson_order}` : 'A1'
            })
        });
        const data = await res.json();

        if (currentAuthUser && data.user) {
            currentAuthUser.total_exp = data.user.total_exp;
            currentAuthUser.arena_best_score = data.user.arena_best_score;
            renderAuthUserUI();
        }

        const scoreClass = arenaCurrentScore >= 80 ? 'text-emerald-600' : (arenaCurrentScore >= 40 ? 'text-indigo-600' : 'text-slate-800');

        playBox.innerHTML = `
            <div class="space-y-6 text-center max-w-lg mx-auto py-2">
                <div class="w-16 h-16 rounded-3xl bg-indigo-100 text-indigo-600 flex items-center justify-center text-3xl mx-auto shadow-inner">
                    🏁
                </div>
                <div class="space-y-1">
                    <span class="text-xs font-black uppercase text-indigo-600 tracking-wider">Hết giờ 2 phút (02:00)</span>
                    <h3 class="text-2xl font-black text-slate-900">Tổng Kết Ván Đấu</h3>
                </div>

                <div class="p-6 rounded-3xl bg-slate-50 border border-slate-200 space-y-4">
                    <div class="text-4xl sm:text-5xl font-black ${scoreClass}">
                        ${arenaCurrentScore} <span class="text-sm font-extrabold text-slate-500">điểm</span>
                    </div>
                    <div class="flex items-center justify-center gap-6 text-xs sm:text-sm font-bold border-t border-slate-200/80 pt-4">
                        <div class="text-emerald-700">✅ Đúng: <b>${arenaCorrectCount}</b> câu</div>
                        <div class="text-rose-700">❌ Sai: <b>${arenaWrongCount}</b> câu</div>
                        <div class="text-amber-700">⚡ +${Math.max(0, arenaCurrentScore)} EXP</div>
                    </div>
                </div>

                <div class="flex items-center justify-center gap-3">
                    <button onclick="initArenaLobbyScreen()" class="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold text-sm shadow-md transition cursor-pointer active:scale-95">
                        Quay về Phòng chờ
                    </button>
                    <button onclick="switchLeaderboardTab('daily')" class="px-5 py-3 rounded-2xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 font-bold text-sm shadow-xs transition cursor-pointer">
                        Xem Bảng Xếp Hạng
                    </button>
                </div>
            </div>
        `;

        loadLeaderboardData();
    } catch (e) {
        initArenaLobbyScreen();
    }
}

// =============================================================================
// 9. BẢNG XẾP HẠNG THỰC TẾ (LEADERBOARD)
// =============================================================================

let activeLeaderboardTab = 'daily';

function switchLeaderboardTab(tab) {
    activeLeaderboardTab = tab;
    const tabDaily = document.getElementById('lb-tab-daily');
    const tabAllTime = document.getElementById('lb-tab-alltime');
    if (tabDaily && tabAllTime) {
        if (tab === 'daily') {
            tabDaily.className = "flex-1 py-1.5 rounded-lg bg-white text-indigo-700 font-extrabold text-xs shadow-xs transition";
            tabAllTime.className = "flex-1 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 font-bold text-xs transition";
        } else {
            tabAllTime.className = "flex-1 py-1.5 rounded-lg bg-white text-indigo-700 font-extrabold text-xs shadow-xs transition";
            tabDaily.className = "flex-1 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 font-bold text-xs transition";
        }
    }
    loadLeaderboardData();
}

async function loadLeaderboardData() {
    const listEl = document.getElementById('leaderboard-list');
    if (!listEl) return;

    try {
        const res = await fetch('/api/arena/leaderboard');
        const data = await res.json();
        const rows = activeLeaderboardTab === 'daily' ? (data.daily_top || []) : (data.all_time_top || []);

        if (rows.length === 0) {
            listEl.innerHTML = `
                <div class="text-center py-6 text-slate-400 text-xs">
                    Chưa có ván đấu nào hôm nay. Hãy là người đầu tiên ghi điểm!
                </div>
            `;
            return;
        }

        listEl.innerHTML = rows.map((u, idx) => {
            const isMe = currentAuthUser && (u.username === currentAuthUser.username || u.user_id === currentAuthUser.id);
            const scoreLabel = activeLeaderboardTab === 'daily' ? `${u.best_today_score}đ hôm nay` : `${u.arena_best_score}đ kỷ lục`;
            const badgeRank = idx === 0 ? '🥇' : (idx === 1 ? '🥈' : (idx === 2 ? '🥉' : `#${idx + 1}`));

            return `
                <div class="flex items-center justify-between p-3 rounded-2xl transition ${isMe ? 'bg-indigo-50 border border-indigo-300 text-indigo-950 font-black shadow-xs' : 'bg-slate-50 border border-slate-200/80 text-slate-800 font-semibold'}">
                    <div class="flex items-center gap-2.5">
                        <span class="w-6 text-center text-xs font-black text-slate-500">${badgeRank}</span>
                        <div>
                            <div class="text-xs sm:text-sm font-bold flex items-center gap-1.5">
                                <span>${u.username}</span>
                                <span class="text-[10px] px-1.5 py-0.2 rounded bg-indigo-100 text-indigo-700 font-extrabold">${u.highest_level_code || 'A1'}</span>
                                ${isMe ? '<span class="text-[10px] px-1.5 rounded bg-emerald-100 text-emerald-700 font-bold">Bạn</span>' : ''}
                            </div>
                            <div class="text-[11px] text-slate-400 font-normal">${scoreLabel}</div>
                        </div>
                    </div>
                    <div class="text-right">
                        <div class="text-amber-600 font-black text-xs sm:text-sm">⚡ ${(u.total_exp || 0).toLocaleString('en-US')}</div>
                        <div class="text-[10px] text-slate-400">EXP</div>
                    </div>
                </div>
            `;
        }).join('');
    } catch (e) {}
}

// =============================================================================
// 10. TỰ ĐỘNG CHẠY KHI TẢI TRANG
// =============================================================================

document.addEventListener('DOMContentLoaded', () => {
    checkCurrentAuthSession();
    initArenaLobbyScreen();
    loadLeaderboardData();
});

