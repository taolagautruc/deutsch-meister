/**
 * b14_review_svg.js — Sơ đồ La bàn Phương hướng (Himmelsrichtungen) & Bộ chấm Semantic Tolerance Bài 14 (A1)
 * Scope: CHỈ dành cho Bài 14 (lesson_id = 28). Tuyệt đối không ảnh hưởng Bài 1 → Bài 13.
 */
(function (global) {
    'use strict';

    const B14_DIRECTIONS = {
        Norden: {
            vi: 'Bắc',
            adj: 'nördlich',
            nounEx: 'Hanoi liegt im Norden von Vietnam.',
            nounExVi: 'Hà Nội nằm ở miền Bắc của Việt Nam. (thuộc Việt Nam)',
            adjEx: 'China liegt nördlich von Vietnam.',
            adjExVi: 'Trung Quốc nằm ở phía Bắc của Việt Nam. (bên ngoài Việt Nam)'
        },
        Nordosten: {
            vi: 'Đông Bắc',
            adj: 'nordöstlich',
            nounEx: 'Hai Phong liegt im Nordosten von Vietnam.',
            nounExVi: 'Hải Phòng nằm ở miền Đông Bắc của Việt Nam. (thuộc Việt Nam)',
            adjEx: 'Rostock liegt nordöstlich von Hannover.',
            adjExVi: 'Rostock nằm ở phía Đông Bắc của Hannover. (hai thành phố riêng)'
        },
        Osten: {
            vi: 'Đông',
            adj: 'östlich',
            nounEx: 'Wien liegt im Osten von Österreich.',
            nounExVi: 'Viên nằm ở miền Đông của nước Áo. (thuộc nước Áo)',
            adjEx: 'Dresden liegt östlich von Köln.',
            adjExVi: 'Dresden nằm ở phía Đông của Köln. (hai thành phố riêng)'
        },
        Südosten: {
            vi: 'Đông Nam',
            adj: 'südöstlich',
            nounEx: 'Griechenland liegt im Südosten von Europa.',
            nounExVi: 'Hy Lạp nằm ở miền Đông Nam của châu Âu. (thuộc châu Âu)',
            adjEx: 'München liegt südöstlich von Stuttgart.',
            adjExVi: 'München nằm ở phía Đông Nam của Stuttgart. (hai thành phố riêng)'
        },
        Süden: {
            vi: 'Nam',
            adj: 'südlich',
            nounEx: 'München liegt im Süden von Deutschland.',
            nounExVi: 'München nằm ở miền Nam của nước Đức. (thuộc nước Đức)',
            adjEx: 'Österreich liegt südlich von Deutschland.',
            adjExVi: 'Áo nằm ở phía Nam của nước Đức. (hai quốc gia riêng)'
        },
        Südwesten: {
            vi: 'Tây Nam',
            adj: 'südwestlich',
            nounEx: 'Spanien liegt im Südwesten von Europa.',
            nounExVi: 'Tây Ban Nha nằm ở miền Tây Nam của châu Âu. (thuộc châu Âu)',
            adjEx: 'Bonn liegt südwestlich von Rostock.',
            adjExVi: 'Bonn nằm ở phía Tây Nam của Rostock. (hai thành phố riêng)'
        },
        Westen: {
            vi: 'Tây',
            adj: 'westlich',
            nounEx: 'Köln liegt im Westen von Deutschland.',
            nounExVi: 'Köln nằm ở miền Tây của nước Đức. (thuộc nước Đức)',
            adjEx: 'Frankreich liegt westlich von Deutschland.',
            adjExVi: 'Pháp nằm ở phía Tây của nước Đức. (hai quốc gia riêng)'
        },
        Nordwesten: {
            vi: 'Tây Bắc',
            adj: 'nordwestlich',
            nounEx: 'Bremen liegt im Nordwesten von Deutschland.',
            nounExVi: 'Bremen nằm ở miền Tây Bắc của nước Đức. (thuộc nước Đức)',
            adjEx: 'Bremen liegt nordwestlich von Leipzig.',
            adjExVi: 'Bremen nằm ở phía Tây Bắc của Leipzig. (hai thành phố riêng)'
        },
        Zentrum: {
            vi: 'Trung tâm / Miền Trung',
            adj: null,
            nounEx: 'Da Nang liegt in der Mitte von Vietnam.',
            nounExVi: 'Đà Nẵng nằm ở miền Trung của Việt Nam. (thuộc Việt Nam)',
            adjEx: 'Hue liegt im Zentrum von Vietnam.',
            adjExVi: 'Huế nằm ở trung tâm của Việt Nam. (thuộc Việt Nam)'
        }
    };

    let selectedDirection = 'Norden';

    function b14_speakGerman(text) {
        const clean = String(text || '').replace(/[„“"]/g, '').trim();
        if (!clean) return;
        if (typeof global.speakGerman === 'function') {
            global.speakGerman(clean);
        } else if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const u = new SpeechSynthesisUtterance(clean);
            u.lang = 'de-DE';
            window.speechSynthesis.speak(u);
        }
    }

    function b14_selectDirection(dirKey) {
        if (!B14_DIRECTIONS[dirKey]) return;
        selectedDirection = dirKey;
        b14_renderCompassMachine();
    }

    function b14_renderCompassMachine() {
        const el = document.getElementById('b14-compass-svg-container');
        if (!el) return;

        const d = B14_DIRECTIONS[selectedDirection] || B14_DIRECTIONS.Norden;
        const nodes = [
            { key: 'Norden', label: 'Norden', short: 'N', x: 160, y: 36 },
            { key: 'Nordosten', label: 'Nordosten', short: 'NO', x: 252, y: 74 },
            { key: 'Osten', label: 'Osten', short: 'O', x: 288, y: 160 },
            { key: 'Südosten', label: 'Südosten', short: 'SO', x: 252, y: 246 },
            { key: 'Süden', label: 'Süden', short: 'S', x: 160, y: 284 },
            { key: 'Südwesten', label: 'Südwesten', short: 'SW', x: 68, y: 246 },
            { key: 'Westen', label: 'Westen', short: 'W', x: 32, y: 160 },
            { key: 'Nordwesten', label: 'Nordwesten', short: 'NW', x: 68, y: 74 }
        ];

        const svgNodes = nodes.map(n => {
            const active = selectedDirection === n.key;
            const fill = active ? '#4f46e5' : '#f8fafc';
            const stroke = active ? '#312e81' : '#94a3b8';
            const txtColor = active ? '#ffffff' : '#0f172a';
            const r = n.short.length === 1 ? 26 : 23;
            return `
                <g style="cursor:pointer;" onclick="b14_selectDirection('${n.key}')">
                    <line x1="160" y1="160" x2="${n.x}" y2="${n.y}" stroke="${active ? '#6366f1' : '#cbd5e1'}" stroke-width="${active ? 3.5 : 1.5}" stroke-dasharray="${active ? '' : '4 3'}" />
                    <circle cx="${n.x}" cy="${n.y}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${active ? 3 : 1.5}" />
                    <text x="${n.x}" y="${n.y + 4}" text-anchor="middle" fill="${txtColor}" font-size="11" font-weight="800" font-family="ui-sans-serif, system-ui, sans-serif">${n.short}</text>
                </g>
            `;
        }).join('');

        const centerActive = selectedDirection === 'Zentrum';
        const nounSafe = d.nounEx.replace(/'/g, "\\'");
        const adjSafe = d.adjEx.replace(/'/g, "\\'");

        const way1Formula = (selectedDirection === 'Zentrum')
            ? `liegt <span class="underline decoration-blue-500">in der Mitte</span> von ... <span class="text-xs font-normal text-blue-700">(hoặc im Zentrum)</span>`
            : `liegt <span class="underline decoration-blue-500">im ${selectedDirection}</span> von ...`;

        const way2Html = d.adj ? `
            <div class="p-4 rounded-2xl bg-emerald-50 border-2 border-emerald-300 space-y-2">
                <div class="flex items-center justify-between gap-2 flex-wrap">
                    <span class="px-2.5 py-0.5 rounded-lg bg-emerald-600 text-white text-[11px] font-black uppercase">CÁCH 2 • Tính từ (-lich) • BÊN NGOÀI X</span>
                    <span class="px-2 py-0.5 rounded-md bg-rose-100 text-rose-800 border border-rose-300 text-[11px] font-black">TUYỆT ĐỐI KHÔNG dùng "im"</span>
                </div>
                <div class="text-xs text-emerald-800 font-semibold">So sánh vị trí hai nơi riêng biệt (A không thuộc X)</div>
                <div class="text-sm font-black text-emerald-950 font-mono">
                    liegt <span class="underline decoration-emerald-500">${d.adj}</span> von ...
                </div>
                <div class="p-2.5 rounded-xl bg-white border border-emerald-200 flex items-center justify-between gap-2 text-xs">
                    <div>
                        <div class="font-mono font-bold text-slate-900">„${d.adjEx}“</div>
                        <div class="text-slate-600 italic">${d.adjExVi}</div>
                    </div>
                    <button type="button" onclick="b14_speakGerman('${adjSafe}')" class="px-2.5 py-1 rounded-lg bg-emerald-100 hover:bg-emerald-200 text-emerald-900 font-bold cursor-pointer shrink-0">🔊</button>
                </div>
            </div>
        ` : `
            <div class="p-4 rounded-2xl bg-amber-50 border-2 border-amber-300 space-y-2">
                <div class="flex items-center justify-between gap-2">
                    <span class="px-2.5 py-0.5 rounded-lg bg-amber-600 text-white text-[11px] font-black uppercase">CỤM CỐ ĐỊNH • TRUNG TÂM</span>
                    <span class="text-[11px] font-bold text-amber-800">Không có tính từ -lich tương ứng</span>
                </div>
                <div class="text-sm font-black text-amber-950 font-mono">
                    liegt <span class="underline decoration-amber-500">in der Mitte / im Zentrum</span> von ...
                </div>
                <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-2 text-xs">
                    <div>
                        <div class="font-mono font-bold text-slate-900">„${d.adjEx}“</div>
                        <div class="text-slate-600 italic">${d.adjExVi}</div>
                    </div>
                    <button type="button" onclick="b14_speakGerman('${adjSafe}')" class="px-2.5 py-1 rounded-lg bg-amber-100 hover:bg-amber-200 text-amber-900 font-bold cursor-pointer shrink-0">🔊</button>
                </div>
            </div>
        `;

        el.innerHTML = `
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-center">
                <div class="lg:col-span-5 flex flex-col items-center">
                    <svg viewBox="0 0 320 320" class="w-full max-w-[300px] bg-white rounded-3xl border border-indigo-200 shadow-sm p-2">
                        <circle cx="160" cy="160" r="126" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
                        <circle cx="160" cy="160" r="78" fill="none" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3 3" />
                        ${svgNodes}
                        <g style="cursor:pointer;" onclick="b14_selectDirection('Zentrum')">
                            <circle cx="160" cy="160" r="32" fill="${centerActive ? '#d97706' : '#fef3c7'}" stroke="${centerActive ? '#92400e' : '#f59e0b'}" stroke-width="2.5" />
                            <text x="160" y="164" text-anchor="middle" fill="${centerActive ? '#ffffff' : '#92400e'}" font-size="11" font-weight="900" font-family="ui-sans-serif, system-ui, sans-serif">Zentrum</text>
                        </g>
                    </svg>
                    <p class="text-[11px] text-slate-500 font-semibold mt-2 text-center">
                        Bấm vào các hướng trên la bàn (N, NO, O, SO, S, SW, W, NW, Zentrum) để đối chiếu 2 cấu trúc.
                    </p>
                </div>
                <div class="lg:col-span-7 space-y-3">
                    <div class="flex flex-wrap items-center justify-between gap-2 pb-2 border-b border-slate-200">
                        <div>
                            <div class="text-xs font-bold text-indigo-600 uppercase">Hướng đang chọn</div>
                            <div class="text-xl font-black text-slate-900">${selectedDirection} <span class="text-sm font-bold text-slate-500">(${d.vi})</span></div>
                        </div>
                        <div class="flex flex-wrap gap-1.5">
                            ${Object.keys(B14_DIRECTIONS).map(k => `
                                <button type="button" onclick="b14_selectDirection('${k}')" class="px-2.5 py-1 rounded-lg text-xs font-bold cursor-pointer transition ${selectedDirection === k ? 'bg-indigo-600 text-white shadow-xs' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'}">${k}</button>
                            `).join('')}
                        </div>
                    </div>
                    <div class="p-4 rounded-2xl bg-blue-50 border-2 border-blue-300 space-y-2">
                        <div class="flex items-center justify-between gap-2 flex-wrap">
                            <span class="px-2.5 py-0.5 rounded-lg bg-blue-600 text-white text-[11px] font-black uppercase">CÁCH 1 • Danh từ viết hoa • BÊN TRONG X</span>
                            <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-900 border border-blue-200 text-[11px] font-black">Bắt buộc có "im" (A thuộc X)</span>
                        </div>
                        <div class="text-sm font-black text-blue-950 font-mono">
                            ${way1Formula}
                        </div>
                        <div class="p-2.5 rounded-xl bg-white border border-blue-200 flex items-center justify-between gap-2 text-xs">
                            <div>
                                <div class="font-mono font-bold text-slate-900">„${d.nounEx}“</div>
                                <div class="text-slate-600 italic">${d.nounExVi}</div>
                            </div>
                            <button type="button" onclick="b14_speakGerman('${nounSafe}')" class="px-2.5 py-1 rounded-lg bg-blue-100 hover:bg-blue-200 text-blue-900 font-bold cursor-pointer shrink-0">🔊</button>
                        </div>
                    </div>
                    ${way2Html}
                </div>
            </div>
            <div class="mt-4 p-3.5 rounded-2xl bg-white border border-indigo-200 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="p-2.5 rounded-xl bg-blue-50/70 border border-blue-200 flex items-center justify-between gap-2">
                    <div>
                        <span class="font-mono font-black text-blue-800">im Norden von Vietnam</span> → <b class="text-slate-900">Hanoi</b>
                        <span class="block text-slate-600 italic mt-0.5">Hà Nội thuộc Việt Nam (nằm BÊN TRONG Việt Nam)</span>
                    </div>
                    <button type="button" onclick="b14_speakGerman('Hanoi liegt im Norden von Vietnam.')" class="p-1.5 rounded-lg bg-white hover:bg-blue-100 border border-blue-200 cursor-pointer shrink-0">🔊</button>
                </div>
                <div class="p-2.5 rounded-xl bg-emerald-50/70 border border-emerald-200 flex items-center justify-between gap-2">
                    <div>
                        <span class="font-mono font-black text-emerald-800">nördlich von Vietnam</span> → <b class="text-slate-900">China</b>
                        <span class="block text-slate-600 italic mt-0.5">Trung Quốc không thuộc Việt Nam (nằm BÊN NGOÀI Việt Nam)</span>
                    </div>
                    <button type="button" onclick="b14_speakGerman('China liegt nördlich von Vietnam.')" class="p-1.5 rounded-lg bg-white hover:bg-emerald-100 border border-emerald-200 cursor-pointer shrink-0">🔊</button>
                </div>
            </div>
        `;
    }

    // =========================================================================
    // SEMANTIC TOLERANCE ENGINE (BÀI 14: DỊCH Đ-V / V-Đ / SỬA LỖI / W-FRAGEN)
    // =========================================================================
    function cleanViB14(str) {
        return String(str || '')
            .toLowerCase()
            .normalize('NFC')
            .replace(/[.,!?;:"'„“”«»‘`’–—\-\(\)\[\]\{\}\/\\~]+/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function hasViPhrase14(clean, pattern) {
        if (!clean) return false;
        return new RegExp('(?:^|\\s)(?:' + pattern + ')(?=\\s|$)').test(clean);
    }

    function evaluateLesson14Translation(userAns, qNum) {
        if (!userAns || typeof userAns !== 'string') return false;
        const clean = cleanViB14(userAns);
        if (!clean) return false;
        const hasQMark = String(userAns).includes('?');

        // Câu 9: „Russland liegt im Osten von Europa.“
        if (qNum === 9) {
            const hasCountry = hasViPhrase14(clean, 'nga|nước nga|liên bang nga');
            const hasDir = hasViPhrase14(clean, '(?:ở\\s+)?(?:miền|phía|khu vực)\\s+đông|đông');
            const hasEurope = hasViPhrase14(clean, 'châu âu|âu châu');
            const forbidden = hasViPhrase14(clean, 'tây|nam|bắc|đức|việt nam|pháp|châu á');
            return Boolean(hasCountry && hasDir && hasEurope && !forbidden);
        }

        // Câu 18: „Die Schweiz liegt südlich von Deutschland.“
        if (qNum === 18) {
            const hasCountry = hasViPhrase14(clean, 'thụy sĩ|nước thụy sĩ|thụy sỹ|nước thụy sỹ');
            const hasDir = hasViPhrase14(clean, '(?:ở\\s+)?(?:miền|phía)\\s+nam|nam');
            const hasGermany = hasViPhrase14(clean, 'đức|nước đức');
            const forbidden = hasViPhrase14(clean, 'bắc|đông|tây|thụy điển|áo|pháp');
            return Boolean(hasCountry && hasDir && hasGermany && !forbidden);
        }

        // Câu 27: „Wo liegt Da Nang?“
        if (qNum === 27) {
            const hasCity = hasViPhrase14(clean, 'đà nẵng|da nang');
            const hasWhere = hasViPhrase14(clean, 'nằm ở đâu|ở đâu|chỗ nào|vị trí nào');
            return Boolean(hasCity && hasWhere);
        }

        // Câu 55: „Letztes Jahr war sie in Vietnam.“
        if (qNum === 55) {
            const hasLastYear = hasViPhrase14(clean, 'năm ngoái|năm trước|vào năm ngoái');
            const hasSubj = hasViPhrase14(clean, 'cô ấy|chị ấy|bà ấy|em ấy|cô ta|họ');
            const hasInVn = hasViPhrase14(clean, '(?:đã\\s+)?(?:từng\\s+)?(?:ở|tại)\\s+(?:nước\\s+)?việt nam');
            const forbidden = hasViPhrase14(clean, 'anh ấy|tôi|bạn|chúng tôi|hôm nay|năm nay|đức');
            return Boolean(hasLastYear && hasSubj && hasInVn && !forbidden);
        }

        // Câu 98: „Fährst du am Wochenende nach Polen?“
        if (qNum === 98) {
            const hasWeekend = hasViPhrase14(clean, 'cuối tuần');
            const hasYou = hasViPhrase14(clean, 'bạn|cậu|mày|em|anh|chị');
            const hasGo = hasViPhrase14(clean, 'đi|lái xe|tới|đến|sang|về|du lịch');
            const hasPoland = hasViPhrase14(clean, 'ba lan');
            const hasQ = hasQMark || hasViPhrase14(clean, 'không|phải không|đúng không|à|hả|chứ|nhỉ');
            const forbidden = hasViPhrase14(clean, 'đức|pháp|việt nam|nga|tôi|các bạn|họ|chúng tôi|ngài');
            return Boolean(hasWeekend && hasYou && hasGo && hasPoland && hasQ && !forbidden);
        }

        // Câu 100: „Das klingt gut! Viel Spaß!“
        if (qNum === 100) {
            const hasGood = hasViPhrase14(clean, '(?:nghe\\s+)?(?:hay|tuyệt|tuyệt vời|ổn|tốt|hợp lý)');
            const hasFun = hasViPhrase14(clean, 'chúc\\s+(?:bạn\\s+|các bạn\\s+)?vui vẻ|vui vẻ nhé|chơi vui');
            return Boolean(hasGood && hasFun);
        }

        // Câu 101: „Was möchtet ihr trinken?“
        if (qNum === 101) {
            const hasSubj = hasViPhrase14(clean, 'các bạn|mọi người|tụi bạn|bọn bạn|các cậu');
            const hasDrinkWhat = hasViPhrase14(clean, 'uống gì|uống thứ gì|uống cái gì');
            const forbidden = hasViPhrase14(clean, 'ăn|tôi|chúng tôi|ngài|anh ấy|cô ấy');
            return Boolean(hasSubj && hasDrinkWhat && !forbidden);
        }

        // Câu 104: „Sie spricht Französisch und Englisch.“
        if (qNum === 104) {
            const hasSubj = hasViPhrase14(clean, 'cô ấy|chị ấy|bà ấy|em ấy|ngài|bạn');
            const hasSpeak = hasViPhrase14(clean, 'nói|nói được|giao tiếp');
            const hasFr = hasViPhrase14(clean, 'tiếng pháp|pháp');
            const hasEn = hasViPhrase14(clean, 'tiếng anh|anh');
            const forbidden = hasViPhrase14(clean, 'đức|nga|việt|tây ban nha|tôi|anh ấy');
            return Boolean(hasSubj && hasSpeak && hasFr && hasEn && !forbidden);
        }

        return false;
    }

    function b14_initReviewSvgDiagrams() {
        b14_renderCompassMachine();
    }

    global.b14_speakGerman = b14_speakGerman;
    global.b14_selectDirection = b14_selectDirection;
    global.b14_renderCompassMachine = b14_renderCompassMachine;
    global.b14_initReviewSvgDiagrams = b14_initReviewSvgDiagrams;
    global.evaluateLesson14Translation = evaluateLesson14Translation;
})(typeof window !== 'undefined' ? window : this);
