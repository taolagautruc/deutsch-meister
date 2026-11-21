/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Körper, Gesundheit, dürfen, Akkusativ & Imperativ SVG
 * Dành riêng cho Bài 12 (A1): "Körper und Gesundheit - Đại từ Akkusativ, Modalverb dürfen & Câu Mệnh lệnh Imperativ"
 * 
 * Cung cấp 6 sơ đồ trực quan theo đặc tả kỹ thuật sư phạm chuẩn CEFR A1:
 * V1: Bản đồ Cơ thể Tương tác (Körperkarte) - Hotspot các bộ phận cơ thể kèm mạo từ, số nhiều và triệu chứng wehtun
 * V2: Bảng Đại từ & Lưu đồ Quyết định Akkusativ vs Dativ (Pronomen-Entscheidungsbaum)
 * V3: Máy Chế tạo Câu Mệnh Lệnh ngôi du (Imperativ-Generator - Biến đổi 3 bước & Xử lý biến âm)
 * V4: So sánh 3 Ngôi Mệnh Lệnh Song Song (Imperativ-Vergleich: du / ihr / Sie)
 * V5: Bảng Điều Khiển Modalverb Dürfen (Modalverb dürfen & Cấu trúc Khung câu Satzklammer)
 * V6: Hoạt cảnh Phòng Khám Bác Sĩ Tương Tác (Beim Arzt - Đối thoại Lễ tân, Bác sĩ & Bệnh nhân)
 */

(function (global) {
    'use strict';

    // =========================================================================
    // V1: BẢN ĐỒ CƠ THỂ TƯƠNG TÁC (KÖRPERKARTE)
    // =========================================================================
    const V1_BODY_PARTS = [
        { id: "kopf", name: "der Kopf", pl: "die Köpfe", art: "der", vi: "đầu", x: 150, y: 35, ex: "Mein Kopf tut mir weh.", tr: "Đầu tôi làm tôi đau (Tôi bị đau đầu)." },
        { id: "auge", name: "das Auge", pl: "die Augen", art: "das", vi: "mắt", x: 140, y: 50, ex: "Meine Augen tun mir weh.", tr: "Đôi mắt của tôi bị đau." },
        { id: "nase", name: "die Nase", pl: "die Nasen", art: "die", vi: "mũi", x: 150, y: 60, ex: "Die Nase läuft.", tr: "Mũi tôi bị chảy nước mũi." },
        { id: "mund", name: "der Mund", pl: "die Münder", art: "der", vi: "miệng", x: 150, y: 72, ex: "Öffnen Sie bitte den Mund!", tr: "Xin ngài hãy mở miệng ra!" },
        { id: "ohr", name: "das Ohr", pl: "die Ohren", art: "das", vi: "tai", x: 172, y: 55, ex: "Mein rechtes Ohr tut weh.", tr: "Tai phải của tôi bị đau." },
        { id: "hals", name: "der Hals", pl: "die Hälse", art: "der", vi: "cổ, họng", x: 150, y: 92, ex: "Ich habe starke Halsschmerzen.", tr: "Tôi bị đau họng dữ dội." },
        { id: "schulter", name: "die Schulter", pl: "die Schultern", art: "die", vi: "vai", x: 195, y: 110, ex: "Ihre Schulter tut sehr weh.", tr: "Vai của cô ấy rất đau." },
        { id: "brust", name: "die Brust", pl: "die Brüste", art: "die", vi: "ngực", x: 150, y: 130, ex: "Der Arzt hört meine Brust ab.", tr: "Bác sĩ nghe lồng ngực của tôi." },
        { id: "arm", name: "der Arm", pl: "die Arme", art: "der", vi: "cánh tay", x: 220, y: 160, ex: "Mein linker Arm tut weh.", tr: "Cánh tay trái của tôi bị đau." },
        { id: "ruecken", name: "der Rücken", pl: "die Rücken", art: "der", vi: "lưng", x: 110, y: 150, ex: "Mein Rücken tut mir sehr weh.", tr: "Lưng tôi làm tôi rất đau (Tôi bị đau lưng)." },
        { id: "bauch", name: "der Bauch", pl: "die Bäuche", art: "der", vi: "bụng", x: 150, y: 175, ex: "Er hat Bauchschmerzen.", tr: "Anh ấy bị đau bụng." },
        { id: "hand", name: "die Hand", pl: "die Hände", art: "die", vi: "bàn tay", x: 235, y: 220, ex: "Geben Sie mir Ihre Hand!", tr: "Hãy đưa tay ngài cho tôi!" },
        { id: "finger", name: "der Finger", pl: "die Finger", art: "der", vi: "ngón tay", x: 240, y: 240, ex: "Mein Finger blutet.", tr: "Ngón tay tôi bị chảy máu." },
        { id: "bein", name: "das Bein", pl: "die Beine", art: "das", vi: "chân (cẳng chân)", x: 175, y: 260, ex: "Meine Beine sind sehr müde.", tr: "Đôi chân tôi rất mệt mỏi." },
        { id: "knie", name: "das Knie", pl: "die Knie", art: "das", vi: "đầu gối", x: 175, y: 295, ex: "Das Knie tut beim Laufen weh.", tr: "Đầu gối tôi đau khi đi lại." },
        { id: "fuss", name: "der Fuß", pl: "die Füße", art: "der", vi: "bàn chân", x: 180, y: 355, ex: "Mein rechter Fuß tut weh.", tr: "Bàn chân phải của tôi bị đau." }
    ];

    let currentV1Index = 0;

    function b12_renderKoerperkarteSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v1-container");
        if (!c) return;
        const current = V1_BODY_PARTS[currentV1Index] || V1_BODY_PARTS[0];

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-rose-500/20 border border-rose-400/40 text-rose-300 font-bold text-xs">
                            Sơ đồ V1: Körperkarte
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Bản Đồ Cơ Thể & Triệu Chứng Bệnh</h4>
                    </div>
                    <span class="text-xs text-slate-400">💡 Bấm vào điểm sáng hoặc danh sách để xem từ & nghe đọc</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-center">
                    <!-- SVG Hình người vector -->
                    <div class="lg:col-span-6 flex justify-center items-center bg-slate-950/70 p-4 rounded-2xl border border-slate-800 relative">
                        <svg viewBox="0 0 300 390" class="w-full max-w-[260px] h-auto select-none">
                            <defs>
                                <radialGradient id="bodyGrad" cx="50%" cy="40%" r="60%">
                                    <stop offset="0%" stop-color="#475569" />
                                    <stop offset="100%" stop-color="#1e293b" />
                                </radialGradient>
                                <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                                    <feGaussianBlur stdDeviation="3" result="glow" />
                                    <feComposite in="SourceGraphic" in2="glow" operator="over" />
                                </filter>
                            </defs>

                            <!-- Đầu -->
                            <ellipse cx="150" cy="55" rx="28" ry="34" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="2" />
                            <!-- Cổ -->
                            <rect x="142" y="86" width="16" height="18" rx="4" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="1.5" />
                            <!-- Thân (Ngực, bụng) -->
                            <path d="M 115 104 Q 150 100 185 104 L 180 205 Q 150 215 120 205 Z" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="2" />
                            <!-- Cánh tay trái -->
                            <path d="M 115 104 L 80 170 L 68 230" fill="none" stroke="url(#bodyGrad)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" />
                            <circle cx="66" cy="235" r="8" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="1.5" />
                            <!-- Cánh tay phải -->
                            <path d="M 185 104 L 220 170 L 232 230" fill="none" stroke="url(#bodyGrad)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round" />
                            <circle cx="234" cy="235" r="8" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="1.5" />
                            <!-- Chân trái -->
                            <path d="M 134 205 L 126 295 L 120 360" fill="none" stroke="url(#bodyGrad)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" />
                            <ellipse cx="114" cy="370" rx="14" ry="7" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="1.5" />
                            <!-- Chân phải -->
                            <path d="M 166 205 L 174 295 L 180 360" fill="none" stroke="url(#bodyGrad)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" />
                            <ellipse cx="186" cy="370" rx="14" ry="7" fill="url(#bodyGrad)" stroke="#64748b" stroke-width="1.5" />

                            <!-- Các điểm Hotspot tương tác -->
                            ${V1_BODY_PARTS.map((p, idx) => {
                                const active = idx === currentV1Index;
                                const pinColor = p.art === 'der' ? '#38bdf8' : (p.art === 'die' ? '#f43f5e' : '#34d399');
                                return `
                                    <g class="cursor-pointer" onclick="b12_selectV1BodyPart(${idx})">
                                        ${active ? `<circle cx="${p.x}" cy="${p.y}" r="11" fill="${pinColor}" opacity="0.3" filter="url(#glow)"><animate attributeName="r" values="8;13;8" dur="1.8s" repeatCount="indefinite"/></circle>` : ''}
                                        <circle cx="${p.x}" cy="${p.y}" r="${active ? 7 : 5}" fill="${active ? pinColor : '#94a3b8'}" stroke="#ffffff" stroke-width="${active ? 2 : 1}" />
                                    </g>
                                `;
                            }).join('')}
                        </svg>
                    </div>

                    <!-- Panel thông tin chi tiết của bộ phận đã chọn -->
                    <div class="lg:col-span-6 space-y-3">
                        <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700/80 space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-0.5 rounded-lg text-xs font-black uppercase tracking-wider ${current.art === 'der' ? 'bg-sky-500/20 text-sky-400 border border-sky-400/30' : (current.art === 'die' ? 'bg-rose-500/20 text-rose-400 border border-rose-400/30' : 'bg-emerald-500/20 text-emerald-400 border border-emerald-400/30')}">
                                    ${current.art} (${current.art === 'der' ? 'Giống Đực' : (current.art === 'die' ? 'Giống Cái' : 'Giống Trung')})
                                </span>
                                <span class="text-xs text-slate-400 font-mono">PL: ${current.pl}</span>
                            </div>

                            <div class="flex items-center justify-between">
                                <div>
                                    <div class="text-2xl font-black text-white tracking-tight">${current.name}</div>
                                    <div class="text-sm font-semibold text-amber-300">Nghĩa: ${current.vi}</div>
                                </div>
                                <button type="button" onclick="speakGerman('${current.name}', 0.9)" class="p-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition shadow-md cursor-pointer flex items-center gap-1.5" title="Phát âm từ vựng">
                                    🔊 <span class="text-xs">Đọc từ</span>
                                </button>
                            </div>

                            <div class="pt-3 border-t border-slate-700/60 space-y-1.5">
                                <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Mẫu câu minh họa:</div>
                                <div class="text-sm sm:text-base font-bold text-emerald-300 font-sans">„${current.ex}“</div>
                                <div class="text-xs text-slate-300">📖 Dịch: ${current.tr}</div>
                                <div class="text-[11px] text-amber-300/90 italic pt-1">💡 Khi đã có đại từ sở hữu (mein-, ihr-...), đại từ Dativ (mir, ihr...) có thể được lược bỏ (ví dụ: Mein Ohr tut weh).</div>
                                <div class="pt-1 flex justify-end">
                                    <button type="button" onclick="speakGerman('${current.ex.replace(/'/g, "\\'")}', 0.9)" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition shadow-xs cursor-pointer flex items-center gap-1">
                                        🔊 Nghe câu mẫu
                                    </button>
                                </div>
                            </div>
                        </div>

                        <!-- Danh sách chọn nhanh bộ phận -->
                        <div class="space-y-1">
                            <div class="text-[11px] font-bold text-slate-400">Chọn nhanh bộ phận khác:</div>
                            <div class="flex flex-wrap gap-1.5 max-h-[140px] overflow-y-auto pr-1">
                                ${V1_BODY_PARTS.map((p, idx) => `
                                    <button type="button" onclick="b12_selectV1BodyPart(${idx})" class="px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${idx === currentV1Index ? 'bg-indigo-600 text-white shadow-sm' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}">
                                        ${p.name.split(' ')[1]} (${p.vi})
                                    </button>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    function b12_selectV1BodyPart(idx) {
        currentV1Index = idx;
        b12_renderKoerperkarteSvg();
    }

    // =========================================================================
    // V2: LƯU ĐỒ PHÂN BIỆT AKKUSATIV VS DATIV (PRONOMEN FLOWCHART)
    // =========================================================================
    const V2_TEST_ITEMS = [
        { verb: "lieben", caseType: "akk", prep: "", meaning: "yêu", sentence: "Ich liebe dich.", tr: "Tôi yêu bạn.", nom: "du", pronoun: "dich", reason: "Động từ lieben tác động trực tiếp lên đối tượng ➔ dùng Akkusativ (dich)." },
        { verb: "helfen", caseType: "dat", prep: "", meaning: "giúp đỡ", sentence: "Der Arzt hilft mir.", tr: "Bác sĩ giúp tôi.", nom: "ich", pronoun: "mir", reason: "Động từ helfen luôn đòi hỏi tân ngữ ở Dativ ➔ dùng mir." },
        { verb: "treffen", caseType: "akk", prep: "", meaning: "gặp gỡ", sentence: "Wir treffen ihn heute im Krankenhaus.", tr: "Chúng tôi gặp anh ấy hôm nay ở bệnh viện.", nom: "er", pronoun: "ihn", reason: "Động từ treffen + Akkusativ ➔ er đổi thành ihn." },
        { verb: "wehtun", caseType: "dat", prep: "", meaning: "làm đau", sentence: "Der Kopf tut ihr weh.", tr: "Đầu cô ấy bị đau.", nom: "sie", pronoun: "ihr", reason: "Cấu trúc 'tut + Dativ + weh' ➔ sie đổi thành ihr." },
        { verb: "anrufen", caseType: "akk", prep: "", meaning: "gọi điện", sentence: "Ruf mich bitte an!", tr: "Xin hãy gọi điện cho tôi!", nom: "ich", pronoun: "mich", reason: "Động từ tách anrufen + Akkusativ ➔ dùng mich." },
        { verb: "danken", caseType: "dat", prep: "", meaning: "cảm ơn", sentence: "Ich danke dir für die Hilfe.", tr: "Tôi cảm ơn bạn vì sự giúp đỡ.", nom: "du", pronoun: "dir", reason: "Động từ danken luôn đi với Dativ ➔ du đổi thành dir." },
        { verb: "hören", caseType: "akk", prep: "", meaning: "nghe", sentence: "Ich höre euch nicht.", tr: "Tôi không nghe thấy các bạn.", nom: "ihr", pronoun: "euch", reason: "Động từ hören + Akkusativ ➔ ihr đổi thành euch." },
        { verb: "kennen", caseType: "akk", prep: "", meaning: "quen biết", sentence: "Das ist Maria. Kennst du sie?", tr: "Kia là Maria. Bạn có biết cô ấy không?", nom: "sie", pronoun: "sie", reason: "Động từ kennen + Akkusativ ➔ sie vẫn là sie." },
        { verb: "für", caseType: "akk", prep: "für", meaning: "cho, dành cho", sentence: "Diese Medizin ist für uns.", tr: "Thuốc này là dành cho chúng tôi.", nom: "wir", pronoun: "uns", reason: "Giới từ für luôn đi kèm Akkusativ ➔ wir đổi thành uns." },
        { verb: "mit", caseType: "dat", prep: "mit", meaning: "với, cùng với", sentence: "Er spricht mit Ihnen.", tr: "Anh ấy nói chuyện với Ngài.", nom: "Sie", pronoun: "Ihnen", reason: "Giới từ mit luôn đi kèm Dativ ➔ Sie đổi thành Ihnen." }
    ];

    let currentV2Index = 0;

    function b12_renderAkkDativFlowchartSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v2-container");
        if (!c) return;
        const cur = V2_TEST_ITEMS[currentV2Index] || V2_TEST_ITEMS[0];
        const isAkk = cur.caseType === "akk";

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/40 text-indigo-300 font-bold text-xs">
                            Sơ đồ V2: Pronomen Akkusativ vs Dativ
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Lưu Đồ Quyết Định Chọn Cách Cho Đại Từ</h4>
                    </div>
                    <span class="text-xs text-slate-400">💡 Chọn động từ / giới từ bên dưới để chạy mô phỏng lưu đồ</span>
                </div>

                <!-- Bảng so sánh Đại từ Nom - Akk - Dat -->
                <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-950/60 p-3">
                    <table class="w-full text-xs text-center border-collapse">
                        <thead>
                            <tr class="border-b border-slate-800 text-[11px] uppercase tracking-wider text-slate-400">
                                <th class="p-2 text-left">Nominativ (Chủ ngữ)</th>
                                <th class="p-2 text-sky-400 font-black">Akkusativ (Tân ngữ Trực tiếp)</th>
                                <th class="p-2 text-amber-400 font-black">Dativ (Tân ngữ Gián tiếp)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 font-mono">
                            <tr class="${cur.nom === 'ich' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">ich (tôi)</td><td class="p-2 text-sky-300 font-black">mich</td><td class="p-2 text-amber-300 font-black">mir</td></tr>
                            <tr class="${cur.nom === 'du' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">du (bạn)</td><td class="p-2 text-sky-300 font-black">dich</td><td class="p-2 text-amber-300 font-black">dir</td></tr>
                            <tr class="${cur.nom === 'er' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">er (anh ấy)</td><td class="p-2 text-sky-300 font-black">ihn (biến đổi!)</td><td class="p-2 text-amber-300 font-black">ihm</td></tr>
                            <tr class="${cur.nom === 'sie' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">sie (cô ấy) / es (nó)</td><td class="p-2 text-sky-300 font-black">sie / es</td><td class="p-2 text-amber-300 font-black">ihr / ihm</td></tr>
                            <tr class="${cur.nom === 'wir' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">wir (chúng tôi)</td><td class="p-2 text-sky-300 font-black">uns</td><td class="p-2 text-amber-300 font-black">uns</td></tr>
                            <tr class="${cur.nom === 'ihr' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">ihr (các bạn)</td><td class="p-2 text-sky-300 font-black">euch</td><td class="p-2 text-amber-300 font-black">euch</td></tr>
                            <tr class="${cur.nom === 'Sie' ? 'bg-indigo-950/70 font-bold' : ''}"><td class="p-2 text-left font-sans text-slate-300">sie (họ) / Sie (Ngài)</td><td class="p-2 text-sky-300 font-black">sie / Sie</td><td class="p-2 text-amber-300 font-black">ihnen / Ihnen</td></tr>
                        </tbody>
                    </table>
                </div>

                <!-- Mô phỏng Lưu đồ SVG -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-2xl ${isAkk ? 'bg-sky-950/60 border-2 border-sky-500/80 shadow-lg' : 'bg-slate-950/40 border border-slate-800 opacity-60'} transition">
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-2 py-0.5 rounded-md bg-sky-500/20 text-sky-400 font-black text-xs">Nhánh 1: Akkusativ</span>
                            ${isAkk ? '<span class="text-xs font-bold text-sky-300 animate-pulse">● ĐANG KÍCH HOẠT</span>' : ''}
                        </div>
                        <div class="text-xs text-slate-300 space-y-1">
                            <div>👉 <b>Động từ:</b> <code>lieben, treffen, sehen, anrufen, besuchen, hören, kennen, fragen...</code></div>
                            <div>👉 <b>Giới từ:</b> <code>für, ohne, durch, gegen, um</code></div>
                            <div class="text-sky-300 font-bold pt-1">Kết luận: Dùng mich, dich, ihn, sie, es, uns, euch, sie, Sie.</div>
                        </div>
                    </div>

                    <div class="p-4 rounded-2xl ${!isAkk ? 'bg-amber-950/60 border-2 border-amber-500/80 shadow-lg' : 'bg-slate-950/40 border border-slate-800 opacity-60'} transition">
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-2 py-0.5 rounded-md bg-amber-500/20 text-amber-400 font-black text-xs">Nhánh 2: Dativ</span>
                            ${!isAkk ? '<span class="text-xs font-bold text-amber-300 animate-pulse">● ĐANG KÍCH HOẠT</span>' : ''}
                        </div>
                        <div class="text-xs text-slate-300 space-y-1">
                            <div>👉 <b>Động từ:</b> <code>helfen, wehtun, danken, gefallen, passen, schmecken, gehören...</code></div>
                            <div>👉 <b>Giới từ:</b> <code>mit, bei, von, zu, nach, aus, seit</code></div>
                            <div class="text-amber-300 font-bold pt-1">Kết luận: Dùng mir, dir, ihm, ihr, ihm, uns, euch, ihnen, Ihnen.</div>
                        </div>
                    </div>
                </div>

                <!-- Kết quả mô phỏng động từ đang chọn -->
                <div class="p-4 rounded-2xl bg-slate-800/90 border border-indigo-500/40 space-y-3">
                    <div class="flex items-center justify-between flex-wrap gap-2">
                        <span class="text-xs text-slate-300 font-semibold">Động từ/Giới từ: <b class="text-white font-mono text-sm">${cur.verb}</b> (${cur.meaning})</span>
                        <span class="px-2.5 py-1 rounded-lg text-xs font-black ${isAkk ? 'bg-sky-500/20 text-sky-300 border border-sky-400/40' : 'bg-amber-500/20 text-amber-300 border border-amber-400/40'}">
                            Quyết định: ${isAkk ? 'AKKUSATIV' : 'DATIV'} ➔ Đại từ '${cur.pronoun}'
                        </span>
                    </div>

                    <div class="p-3 rounded-xl bg-slate-950 border border-slate-700/80 flex items-center justify-between gap-3 flex-wrap">
                        <div class="space-y-0.5">
                            <div class="text-base sm:text-lg font-black text-white">👉 „${cur.sentence}“</div>
                            <div class="text-xs text-slate-300">📖 Dịch: ${cur.tr}</div>
                            <div class="text-[11px] text-indigo-300 pt-1">💡 <i>${cur.reason}</i></div>
                        </div>
                        <button type="button" onclick="speakGerman('${cur.sentence.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                            🔊 Nghe câu mẫu
                        </button>
                    </div>

                    <!-- Nút bấm chuyển trường hợp -->
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        ${V2_TEST_ITEMS.map((item, idx) => `
                            <button type="button" onclick="b12_selectV2Item(${idx})" class="px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${idx === currentV2Index ? 'bg-indigo-600 text-white shadow-sm' : 'bg-slate-700/80 hover:bg-slate-700 text-slate-300 border border-slate-600'}">
                                ${item.verb} (${item.caseType.toUpperCase()})
                            </button>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    function b12_selectV2Item(idx) {
        currentV2Index = idx;
        b12_renderAkkDativFlowchartSvg();
    }

    // =========================================================================
    // V3: MÁY CHẾ TẠO IMPERATIV NGÔI DU (3 BƯỚC BIẾN ĐỔI)
    // =========================================================================
    const V3_VERB_ITEMS = [
        {
            verb: "gehen", type: "regular", praesens: "Du gehst", ruleType: "Động từ có quy tắc",
            step1: "Chia ngôi du ở Hiện tại: 'Du gehst'",
            step2: "Bỏ chủ ngữ 'Du' và bỏ đuôi '-st': geh<s>st</s>",
            step3: "Kết quả: Geh!",
            imperativ: "Geh nach Hause!", tr: "Hãy đi về nhà đi!",
            note: "Quy tắc tiêu chuẩn: bỏ du, bỏ đuôi -st."
        },
        {
            verb: "essen", type: "vowel_e_to_i", praesens: "Du isst", ruleType: "Biến âm e ➔ i (GIỮ biến âm)",
            step1: "Chia ngôi du ở Hiện tại: 'Du isst' (đã biến âm e ➔ i)",
            step2: "Bỏ 'Du' và đuôi '-t': is<s>t</s>",
            step3: "Kết quả: Iss!",
            imperativ: "Iss mehr Obst!", tr: "Hãy ăn nhiều trái cây hơn!",
            note: "Du isst ➔ bỏ du và đuôi -t ➔ Iss! (động từ đổi e ➔ i nên giữ i)."
        },
        {
            verb: "fahren", type: "vowel_a_to_ae", praesens: "Du fährst", ruleType: "Biến âm a ➔ ä (Về nguyên âm gốc)",
            step1: "Chia ngôi du ở Hiện tại: 'Du fährst' (có dấu hai chấm ä)",
            step2: "Bỏ 'Du', bỏ '-st' VÀ trở về nguyên âm gốc 'a'",
            step3: "Kết quả: Fahr!",
            imperativ: "Fahr langsamer!", tr: "Hãy lái xe chậm hơn!",
            note: "Động từ đổi a ➔ ä (hoặc au ➔ äu) ở ngôi du thì Imperativ ngôi du trở về nguyên âm gốc: fährst ➔ Fahr!, schläfst ➔ Schlaf!, läufst ➔ Lauf!."
        },
        {
            verb: "warten", type: "stem_d_t", praesens: "Du wartest", ruleType: "Gốc kết thúc bằng -t/-d hoặc phụ âm + m/n (Thêm -e)",
            step1: "Chia ngôi du ở Hiện tại: 'Du wartest'",
            step2: "Bỏ 'Du' và bỏ '-st' ➔ còn 'warte'",
            step3: "Kết quả: Warte!",
            imperativ: "Warte hier auf mich!", tr: "Hãy đợi tôi ở đây!",
            note: "Gốc kết thúc bằng -t/-d hoặc phụ âm + m/n (như arbeit- ➔ Arbeite!, atm- ➔ Atme!, öffn- ➔ Öffne!, zeichn- ➔ Zeichne!) bắt buộc thêm đuôi -e để phát âm được."
        },
        {
            verb: "schlafen", type: "vowel_a_to_ae", praesens: "Du schläfst", ruleType: "Biến âm a ➔ ä (MẤT biến âm)",
            step1: "Chia ngôi du ở Hiện tại: 'Du schläfst'",
            step2: "Bỏ 'Du', bỏ '-st' và bỏ biến âm ä",
            step3: "Kết quả: Schlaf!",
            imperativ: "Schlaf gut!", tr: "Hãy ngủ ngon nhé!",
            note: "Biến âm a ➔ ä bị triệt tiêu ở câu mệnh lệnh ngôi du."
        },
        {
            verb: "sein", type: "irregular", praesens: "Du bist", ruleType: "Ngoại lệ đặc biệt (Bất quy tắc)",
            step1: "Hiện tại: 'Du bist'",
            step2: "Không áp dụng công thức bỏ -st từ 'bist', mà dùng gốc 'Sei'",
            step3: "Kết quả: Sei!",
            imperativ: "Sei vorsichtig!", tr: "Hãy cẩn thận!",
            note: "Động từ sein có dạng Imperativ đặc biệt: du ➔ Sei!, ihr ➔ Seid!, Sie ➔ Seien Sie!"
        }
    ];

    let currentV3Index = 0;

    function b12_renderImperativMachineSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v3-container");
        if (!c) return;
        const cur = V3_VERB_ITEMS[currentV3Index] || V3_VERB_ITEMS[0];

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-300 font-bold text-xs">
                            Sơ đồ V3: Imperativ Machine
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Máy Chế Tạo Mệnh Lệnh Ngôi du (3 Bước)</h4>
                    </div>
                    <span class="text-xs text-slate-400">💡 Chọn động từ để xem quy tắc biến âm được xử lý tự động</span>
                </div>

                <!-- Thanh chọn động từ -->
                <div class="flex flex-wrap gap-2">
                    ${V3_VERB_ITEMS.map((item, idx) => `
                        <button type="button" onclick="b12_selectV3Verb(${idx})" class="px-3 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer flex items-center gap-1.5 ${idx === currentV3Index ? 'bg-amber-500 text-slate-950 font-black shadow-md' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}">
                            <span>${item.verb}</span>
                            <span class="text-[10px] opacity-75 font-normal">(${item.ruleType.split(' ')[0]})</span>
                        </button>
                    `).join('')}
                </div>

                <!-- Sơ đồ 3 Bước Chế tạo (Step 1 -> Step 2 -> Step 3) -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <!-- Bước 1 -->
                    <div class="p-4 rounded-2xl bg-slate-950/70 border border-slate-800 space-y-2 relative">
                        <div class="flex items-center justify-between">
                            <span class="w-6 h-6 rounded-full bg-slate-800 text-slate-300 font-bold text-xs flex items-center justify-center">1</span>
                            <span class="text-[10px] text-slate-400 font-semibold uppercase">Hiện tại Präsens</span>
                        </div>
                        <div class="text-xs text-slate-400">${cur.step1}</div>
                        <div class="text-lg font-mono font-bold text-indigo-300">„${cur.praesens}“</div>
                    </div>

                    <!-- Bước 2 -->
                    <div class="p-4 rounded-2xl bg-slate-950/70 border border-amber-500/40 space-y-2 relative">
                        <div class="flex items-center justify-between">
                            <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 font-bold text-xs flex items-center justify-center border border-amber-400/40">2</span>
                            <span class="text-[10px] text-amber-400 font-semibold uppercase">Áp dụng Luật</span>
                        </div>
                        <div class="text-xs text-slate-300">${cur.step2}</div>
                        <div class="text-xs font-semibold text-amber-300">Nhóm: ${cur.ruleType}</div>
                    </div>

                    <!-- Bước 3 -->
                    <div class="p-4 rounded-2xl bg-gradient-to-br from-amber-950/50 to-slate-950 border-2 border-amber-500 text-white space-y-2 relative shadow-lg">
                        <div class="flex items-center justify-between">
                            <span class="w-6 h-6 rounded-full bg-amber-500 text-slate-950 font-black text-xs flex items-center justify-center">3</span>
                            <span class="text-[10px] text-amber-300 font-bold uppercase">Mệnh lệnh chuẩn</span>
                        </div>
                        <div class="text-xs text-slate-300">${cur.step3}</div>
                        <div class="text-xl font-mono font-black text-amber-400">„${cur.imperativ.split(' ')[0]}“</div>
                    </div>
                </div>

                <!-- Thẻ giải thích chi tiết & Câu hoàn chỉnh -->
                <div class="p-4 rounded-2xl bg-slate-800/90 border border-slate-700/80 space-y-2.5">
                    <div class="flex items-center justify-between flex-wrap gap-2">
                        <div class="space-y-0.5">
                            <div class="text-xs text-amber-300 font-bold uppercase tracking-wider">Câu Mệnh Lệnh Thực Tế:</div>
                            <div class="text-base sm:text-lg font-black text-white">👉 „${cur.imperativ}“</div>
                            <div class="text-xs text-slate-300">📖 Dịch nghĩa: ${cur.tr}</div>
                        </div>
                        <button type="button" onclick="speakGerman('${cur.imperativ.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                            🔊 Nghe câu lệnh
                        </button>
                    </div>
                    <div class="text-xs text-slate-400 pt-1 border-t border-slate-700/60">
                        💡 <b>Ghi chú cốt lõi:</b> ${cur.note}
                    </div>
                </div>
            </div>
        `;
    }

    function b12_selectV3Verb(idx) {
        currentV3Index = idx;
        b12_renderImperativMachineSvg();
    }

    // =========================================================================
    // V4: SO SÁNH 3 NGÔI MỆNH LỆNH (DU - IHR - SIE)
    // =========================================================================
    const V4_COMPARISON_VERBS = [
        {
            verb: "trinken", vi: "uống",
            du: { form: "Trink!", ex: "Trink viel Wasser!", tr: "Hãy uống nhiều nước!" },
            ihr: { form: "Trinkt!", ex: "Trinkt viel Wasser!", tr: "Các bạn hãy uống nhiều nước!" },
            sie: { form: "Trinken Sie!", ex: "Trinken Sie viel Wasser!", tr: "Xin Ngài hãy uống nhiều nước!" }
        },
        {
            verb: "nehmen", vi: "lấy; uống thuốc",
            du: { form: "Nimm!", ex: "Nimm diese Tablette!", tr: "Hãy uống viên thuốc này!" },
            ihr: { form: "Nehmt!", ex: "Nehmt diese Tabletten!", tr: "Các bạn hãy uống những viên thuốc này!" },
            sie: { form: "Nehmen Sie!", ex: "Nehmen Sie diese Tablette!", tr: "Xin Ngài hãy uống viên thuốc này!" }
        },
        {
            verb: "bleiben", vi: "ở lại",
            du: { form: "Bleib!", ex: "Bleib im Bett!", tr: "Hãy nằm yên trên giường!" },
            ihr: { form: "Bleibt!", ex: "Bleibt im Bett!", tr: "Các bạn hãy nằm yên trên giường!" },
            sie: { form: "Bleiben Sie!", ex: "Bleiben Sie im Bett!", tr: "Xin Ngài hãy nằm yên trên giường!" }
        },
        {
            verb: "helfen", vi: "giúp đỡ",
            du: { form: "Hilf!", ex: "Hilf mir bitte!", tr: "Hãy giúp tôi với!" },
            ihr: { form: "Helft!", ex: "Helft mir bitte!", tr: "Các bạn hãy giúp tôi với!" },
            sie: { form: "Helfen Sie!", ex: "Helfen Sie mir bitte!", tr: "Xin Ngài hãy giúp tôi với!" }
        },
        {
            verb: "sein", vi: "thì, là",
            du: { form: "Sei!", ex: "Sei ruhig!", tr: "Hãy giữ bình tĩnh! (hoặc: giữ trật tự)" },
            ihr: { form: "Seid!", ex: "Seid ruhig!", tr: "Các bạn hãy giữ bình tĩnh! (hoặc: giữ trật tự)" },
            sie: { form: "Seien Sie!", ex: "Seien Sie ruhig!", tr: "Xin Ngài hãy giữ bình tĩnh! (hoặc: giữ trật tự)" }
        }
    ];

    let currentV4Index = 0;

    function b12_renderImperativComparisonSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v4-container");
        if (!c) return;
        const cur = V4_COMPARISON_VERBS[currentV4Index] || V4_COMPARISON_VERBS[0];

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-400/40 text-emerald-300 font-bold text-xs">
                            Sơ đồ V4: 3-Personen Imperativ
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">So Sánh Trực Quan 3 Ngôi Mệnh Lệnh (du / ihr / Sie)</h4>
                    </div>
                    <span class="text-xs text-slate-400">💡 Bấm nút 🔊 ở từng cột để so sánh âm điệu ra lệnh</span>
                </div>

                <!-- Chọn động từ -->
                <div class="flex flex-wrap gap-2">
                    ${V4_COMPARISON_VERBS.map((v, idx) => `
                        <button type="button" onclick="b12_selectV4Verb(${idx})" class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer ${idx === currentV4Index ? 'bg-indigo-600 text-white shadow-md font-black' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}">
                            ${v.verb} (${v.vi})
                        </button>
                    `).join('')}
                </div>

                <!-- 3 Cột song song -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <!-- Cột 1: du -->
                    <div class="p-4 rounded-2xl bg-amber-950/40 border border-amber-500/50 space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="px-2.5 py-0.5 rounded-md bg-amber-500/20 text-amber-300 font-bold text-xs">Ngôi du (Bạn - 1 người)</span>
                            <span class="text-[11px] text-amber-400 font-mono font-bold">Thân mật</span>
                        </div>
                        <div class="space-y-1">
                            <div class="text-xs text-slate-400">Công thức: Bỏ du, bỏ -st</div>
                            <div class="text-xl font-black text-amber-300 font-mono">${cur.du.form}</div>
                        </div>
                        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1">
                            <div class="text-xs font-bold text-white">„${cur.du.ex}“</div>
                            <div class="text-[11px] text-slate-400">${cur.du.tr}</div>
                            <button type="button" onclick="speakGerman('${cur.du.ex.replace(/'/g, "\\'")}', 0.9)" class="w-full mt-2 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold transition flex items-center justify-center gap-1 cursor-pointer">
                                🔊 Nghe ngôi du
                            </button>
                        </div>
                    </div>

                    <!-- Cột 2: ihr -->
                    <div class="p-4 rounded-2xl bg-indigo-950/40 border border-indigo-500/50 space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="px-2.5 py-0.5 rounded-md bg-indigo-500/20 text-indigo-300 font-bold text-xs">Ngôi ihr (Các bạn - Nhiều người)</span>
                            <span class="text-[11px] text-indigo-400 font-mono font-bold">Bạn bè</span>
                        </div>
                        <div class="space-y-1">
                            <div class="text-xs text-slate-400">Công thức: Chia như ihr, bỏ ihr</div>
                            <div class="text-xl font-black text-indigo-300 font-mono">${cur.ihr.form}</div>
                        </div>
                        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1">
                            <div class="text-xs font-bold text-white">„${cur.ihr.ex}“</div>
                            <div class="text-[11px] text-slate-400">${cur.ihr.tr}</div>
                            <button type="button" onclick="speakGerman('${cur.ihr.ex.replace(/'/g, "\\'")}', 0.9)" class="w-full mt-2 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition flex items-center justify-center gap-1 cursor-pointer">
                                🔊 Nghe ngôi ihr
                            </button>
                        </div>
                    </div>

                    <!-- Cột 3: Sie -->
                    <div class="p-4 rounded-2xl bg-emerald-950/40 border border-emerald-500/50 space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="px-2.5 py-0.5 rounded-md bg-emerald-500/20 text-emerald-300 font-bold text-xs">Ngôi Sie (Ngài / Quý vị)</span>
                            <span class="text-[11px] text-emerald-400 font-mono font-bold">Lịch sự</span>
                        </div>
                        <div class="space-y-1">
                            <div class="text-xs text-slate-400">Công thức: Đảo Động từ + Sie</div>
                            <div class="text-xl font-black text-emerald-300 font-mono">${cur.sie.form}</div>
                        </div>
                        <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 space-y-1">
                            <div class="text-xs font-bold text-white">„${cur.sie.ex}“</div>
                            <div class="text-[11px] text-slate-400">${cur.sie.tr}</div>
                            <button type="button" onclick="speakGerman('${cur.sie.ex.replace(/'/g, "\\'")}', 0.9)" class="w-full mt-2 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition flex items-center justify-center gap-1 cursor-pointer">
                                🔊 Nghe ngôi Sie
                            </button>
                        </div>
                    </div>
                </div>

                <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800 text-xs text-slate-400">
                    💡 <b>Quy tắc quan trọng:</b> Chủ ngữ <code>du</code> và <code>ihr</code> thường lược bỏ; chỉ thêm khi muốn nhấn mạnh hoặc đối lập (ví dụ: <i>Komm du mal her!</i>). Dạng có chủ ngữ (<i>Gehst du!</i> / <i>Geht ihr!</i>) thường không dùng ➔ Tiêu chuẩn là: <i>Geh!</i> / <i>Geht!</i>. Riêng ngôi <code>Sie</code> bắt buộc phải có chữ <code>Sie</code> đi ngay sau động từ (<i>Gehen Sie!</i>).
                </div>
            </div>
        `;
    }

    function b12_selectV4Verb(idx) {
        currentV4Index = idx;
        b12_renderImperativComparisonSvg();
    }

    // =========================================================================
    // V5: BẢNG ĐIỀU KHIỂN MODALVERB DÜRFEN (SỰ CHO PHÉP / CẤM ĐOÁN)
    // =========================================================================
    const V5_SUBJECTS = [
        { label: "ich (tôi)", conj: "darf", pronoun: "ich" },
        { label: "du (bạn)", conj: "darfst", pronoun: "du" },
        { label: "er / sie (anh/cô ấy)", conj: "darf", pronoun: "er" },
        { label: "wir (chúng tôi)", conj: "dürfen", pronoun: "wir" },
        { label: "ihr (các bạn)", conj: "dürft", pronoun: "ihr" },
        { label: "Sie (Ngài / họ)", conj: "dürfen", pronoun: "Sie" },
        { label: "man (người ta)", conj: "darf", pronoun: "man" }
    ];

    const V5_ACTIONS = [
        { label: "hier rauchen", verb: "rauchen", noun: "hier", vi: "hút thuốc ở đây", icon: "🚭" },
        { label: "hier parken", verb: "parken", noun: "hier", vi: "đỗ xe ở đây", icon: "🅿️" },
        { label: "Computer spielen", verb: "spielen", noun: "Computer", vi: "chơi máy tính", icon: "💻" },
        { label: "Alkohol trinken", verb: "trinken", noun: "Alkohol", vi: "uống rượu bia", icon: "🍷" },
        { label: "Fotos machen", verb: "machen", noun: "Fotos", vi: "chụp ảnh", icon: "📷" },
        { label: "nach Hause gehen", verb: "gehen", noun: "nach Hause", vi: "đi về nhà", icon: "🏠" }
    ];

    let currentV5Subj = 6; // man (mặc định)
    let currentV5Action = 0; // hier rauchen
    let currentV5Mode = "verbot"; // "verbot" (cấm) hoặc "erlaubnis" (cho phép)

    function b12_renderDuerfenControlSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v5-container");
        if (!c) return;

        const subj = V5_SUBJECTS[currentV5Subj];
        const act = V5_ACTIONS[currentV5Action];
        const isVerbot = currentV5Mode === "verbot";

        // Xếp câu theo khung Satzklammer: [Chủ ngữ] + [dürfen chia] + [hành động / nicht] + [Động từ nguyên thể cuối]
        let sentenceDe = "";
        let sentenceVi = "";

        if (isVerbot) {
            sentenceDe = `${subj.pronoun.charAt(0).toUpperCase() + subj.pronoun.slice(1)} ${subj.conj} ${act.noun ? act.noun + ' ' : ''}nicht ${act.verb}.`;
            sentenceVi = `${subj.label.split(' ')[0]} không được phép ${act.vi}.`;
        } else {
            sentenceDe = `${subj.pronoun.charAt(0).toUpperCase() + subj.pronoun.slice(1)} ${subj.conj} ${act.noun ? act.noun + ' ' : ''}${act.verb}.`;
            sentenceVi = `${subj.label.split(' ')[0]} được phép ${act.vi}.`;
        }

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-rose-500/20 border border-rose-400/40 text-rose-300 font-bold text-xs">
                            Sơ đồ V5: Modalverb dürfen
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Bảng Điều Khiển Modalverb dürfen (Satzklammer)</h4>
                    </div>
                    <!-- Chuyển chế độ: Cấm đoán vs Cho phép -->
                    <div class="flex items-center rounded-xl bg-slate-950 p-1 border border-slate-800">
                        <button type="button" onclick="b12_setV5Mode('verbot')" class="px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${isVerbot ? 'bg-rose-600 text-white shadow-xs' : 'text-slate-400 hover:text-white'}">
                            🚫 Cấm đoán (nicht dürfen)
                        </button>
                        <button type="button" onclick="b12_setV5Mode('erlaubnis')" class="px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${!isVerbot ? 'bg-emerald-600 text-white shadow-xs' : 'text-slate-400 hover:text-white'}">
                            ✅ Cho phép (dürfen)
                        </button>
                    </div>
                </div>

                <!-- Bộ điều khiển lựa chọn -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Chọn Chủ ngữ -->
                    <div class="space-y-1.5">
                        <label class="text-xs font-bold text-slate-300">1. Chọn Chủ ngữ (Subjekt):</label>
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-1.5">
                            ${V5_SUBJECTS.map((s, idx) => `
                                <button type="button" onclick="b12_selectV5Subj(${idx})" class="p-2 rounded-xl text-xs font-bold transition text-left cursor-pointer ${idx === currentV5Subj ? 'bg-indigo-600 text-white shadow-sm border border-indigo-400' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}">
                                    <div>${s.label.split(' ')[0]}</div>
                                    <div class="text-[10px] text-amber-300 font-mono font-bold">${s.conj}</div>
                                </button>
                            `).join('')}
                        </div>
                    </div>

                    <!-- Chọn Hành động -->
                    <div class="space-y-1.5">
                        <label class="text-xs font-bold text-slate-300">2. Chọn Hành động (Aktion):</label>
                        <div class="grid grid-cols-2 sm:grid-cols-3 gap-1.5">
                            ${V5_ACTIONS.map((a, idx) => `
                                <button type="button" onclick="b12_selectV5Action(${idx})" class="p-2 rounded-xl text-xs font-bold transition text-left cursor-pointer flex items-center gap-1.5 ${idx === currentV5Action ? 'bg-rose-600 text-white shadow-sm border border-rose-400' : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'}">
                                    <span class="text-base">${a.icon}</span>
                                    <div class="truncate text-[11px]">${a.label}</div>
                                </button>
                            `).join('')}
                        </div>
                    </div>
                </div>

                <!-- Khung câu Satzklammer sinh ra -->
                <div class="p-4 rounded-2xl ${isVerbot ? 'bg-rose-950/50 border-2 border-rose-500/60' : 'bg-emerald-950/50 border-2 border-emerald-500/60'} space-y-3 shadow-lg">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold uppercase tracking-wider ${isVerbot ? 'text-rose-300' : 'text-emerald-300'}">
                            ${isVerbot ? '🚫 Câu Cấm Đoán (Verbot)' : '✅ Câu Cho Phép (Erlaubnis)'} — Khung Satzklammer
                        </span>
                        <span class="text-2xl">${act.icon}</span>
                    </div>

                    <!-- Hiển thị từng vị trí trong khung câu -->
                    <div class="flex items-center gap-2 flex-wrap text-sm sm:text-base font-mono">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-700 text-white font-bold">${subj.pronoun}</span>
                        <span class="px-2.5 py-1 rounded-lg bg-amber-500/20 border border-amber-400/40 text-amber-300 font-black">[V1: ${subj.conj}]</span>
                        ${act.noun ? `<span class="px-2 py-1 rounded-lg bg-slate-900 border border-slate-700 text-slate-300">${act.noun}</span>` : ''}
                        ${isVerbot ? '<span class="px-2 py-1 rounded-lg bg-rose-500/20 border border-rose-400/40 text-rose-300 font-bold">nicht</span>' : ''}
                        <span class="px-2.5 py-1 rounded-lg bg-emerald-500/20 border border-emerald-400/40 text-emerald-300 font-black">[V-cuối: ${act.verb}]</span>
                    </div>

                    <div class="p-3 rounded-xl bg-slate-950 border border-slate-800 flex items-center justify-between gap-3 flex-wrap">
                        <div class="space-y-0.5">
                            <div class="text-base sm:text-lg font-black text-white">„${sentenceDe}“</div>
                            <div class="text-xs text-slate-300">📖 Dịch: ${sentenceVi}</div>
                        </div>
                        <button type="button" onclick="speakGerman('${sentenceDe.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                            🔊 Nghe câu này
                        </button>
                    </div>
                </div>
            </div>
        `;
    }

    function b12_selectV5Subj(idx) {
        currentV5Subj = idx;
        b12_renderDuerfenControlSvg();
    }

    function b12_selectV5Action(idx) {
        currentV5Action = idx;
        b12_renderDuerfenControlSvg();
    }

    function b12_setV5Mode(mode) {
        currentV5Mode = mode;
        b12_renderDuerfenControlSvg();
    }

    // =========================================================================
    // V6: HOẠT CẢNH PHÒNG KHÁM BÁC SĨ (BEIM HAUSARZT)
    // =========================================================================
    const V6_DIALOGUE = [
        { speaker: "doctor", name: "Frau Weber (Lễ tân)", de: "Guten Tag! Waren Sie schon mal bei uns?", vi: "Xin chào! Ngài đã từng đến chỗ chúng tôi chưa?", audio: "Guten Tag! Waren Sie schon mal bei uns?" },
        { speaker: "patient", name: "Herr Linh (Bệnh nhân)", de: "Nein, ich bin neu hier. Mein Name ist Linh.", vi: "Chưa, tôi là người mới. Tên tôi là Linh.", audio: "Nein, ich bin neu hier. Mein Name ist Linh." },
        { speaker: "doctor", name: "Frau Weber (Lễ tân)", de: "Ich brauche bitte Ihre Versichertenkarte.", vi: "Tôi xin phép cần thẻ bảo hiểm y tế của ngài.", audio: "Ich brauche bitte Ihre Versichertenkarte." },
        { speaker: "patient", name: "Herr Linh (Bệnh nhân)", de: "Hier, bitte sehr.", vi: "Dạ đây, xin mời cô.", audio: "Hier, bitte sehr." },
        { speaker: "doctor", name: "Dr. Müller (Bác sĩ)", de: "Guten Tag, Herr Linh! Was fehlt Ihnen denn?", vi: "Chào anh Linh! Anh bị làm sao vậy?", audio: "Guten Tag, Herr Linh! Was fehlt Ihnen denn?" },
        { speaker: "patient", name: "Herr Linh (Bệnh nhân)", de: "Mein Hals tut mir sehr weh und ich habe Husten.", vi: "Họng tôi rất đau và tôi bị ho.", audio: "Mein Hals tut mir sehr weh und ich habe Husten." },
        { speaker: "doctor", name: "Dr. Müller (Bác sĩ)", de: "Machen Sie bitte den Mund auf und sagen Sie 'A'!", vi: "Xin anh hãy mở miệng ra và nói 'A'!", audio: "Machen Sie bitte den Mund auf und sagen Sie A!" },
        { speaker: "doctor", name: "Dr. Müller (Bác sĩ)", de: "Sie haben eine Entzündung. Ich verschreibe Ihnen Tabletten.", vi: "Anh bị viêm rồi. Tôi sẽ kê đơn thuốc viên cho anh.", audio: "Sie haben eine Entzündung. Ich verschreibe Ihnen Tabletten." },
        { speaker: "doctor", name: "Dr. Müller (Bác sĩ)", de: "Nehmen Sie die Tabletten täglich und bleiben Sie im Bett!", vi: "Hãy uống thuốc mỗi ngày và hãy nằm nghỉ ngơi trên giường!", audio: "Nehmen Sie die Tabletten täglich und bleiben Sie im Bett!" },
        { speaker: "patient", name: "Herr Linh (Bệnh nhân)", de: "Vielen Dank, Herr Doktor!", vi: "Cảm ơn bác sĩ rất nhiều!", audio: "Vielen Dank, Herr Doktor!" }
    ];

    let currentV6Step = 0;
    let showV6Translation = true;

    function b12_renderKlinikSceneSvg(containerId) {
        const c = document.getElementById(containerId || "b12-svg-v6-container");
        if (!c) return;

        const cur = V6_DIALOGUE[currentV6Step];
        const isDoctor = cur.speaker === "doctor";

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-xl space-y-5">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-cyan-500/20 border border-cyan-400/40 text-cyan-300 font-bold text-xs">
                            Sơ đồ V6: Beim Hausarzt
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Hoạt Cảnh Phòng Khám Bác Sĩ & Nhà Thuốc</h4>
                    </div>
                    <div class="flex items-center gap-2">
                        <button type="button" onclick="b12_toggleV6Translation()" class="px-3 py-1 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition cursor-pointer">
                            ${showV6Translation ? 'Ẩn bản dịch' : 'Hiện bản dịch'}
                        </button>
                        <span class="text-xs text-slate-400 font-mono">Lượt ${currentV6Step + 1} / ${V6_DIALOGUE.length}</span>
                    </div>
                </div>

                <!-- Khu vực Đối thoại trực quan (Speech Bubbles) -->
                <div class="min-h-[190px] p-5 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col justify-center space-y-4">
                    <div class="flex items-center gap-3 ${isDoctor ? '' : 'flex-row-reverse'}">
                        <!-- Avatar -->
                        <div class="w-12 h-12 rounded-2xl flex items-center justify-center text-2xl shrink-0 shadow-md ${isDoctor ? 'bg-cyan-600 text-white border border-cyan-400' : 'bg-emerald-600 text-white border border-emerald-400'}">
                            ${isDoctor ? '🩺' : '🤒'}
                        </div>

                        <!-- Bóng nói -->
                        <div class="max-w-xl p-4 rounded-3xl ${isDoctor ? 'bg-cyan-950/70 border border-cyan-500/50 rounded-tl-none' : 'bg-emerald-950/70 border border-emerald-500/50 rounded-tr-none'} space-y-1 shadow-lg">
                            <div class="text-[11px] font-bold ${isDoctor ? 'text-cyan-400' : 'text-emerald-400'} uppercase tracking-wider">
                                ${cur.name}
                            </div>
                            <div class="text-base sm:text-lg font-black text-white leading-snug">
                                „${cur.de}“
                            </div>
                            ${showV6Translation ? `<div class="text-xs text-slate-300 pt-0.5">📖 ${cur.vi}</div>` : ''}
                        </div>
                    </div>
                </div>

                <!-- Bảng điều khiển chuyển lượt & phát âm -->
                <div class="flex items-center justify-between flex-wrap gap-2 pt-1 border-t border-slate-800">
                    <div class="flex items-center gap-2">
                        <button type="button" onclick="b12_prevV6Step()" ${currentV6Step === 0 ? 'disabled' : ''} class="px-3.5 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-white transition flex items-center gap-1 cursor-pointer">
                            ◀ Lượt trước
                        </button>
                        <button type="button" onclick="b12_nextV6Step()" ${currentV6Step === V6_DIALOGUE.length - 1 ? 'disabled' : ''} class="px-3.5 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed text-white transition flex items-center gap-1 cursor-pointer">
                            Lượt kế tiếp ▶
                        </button>
                    </div>

                    <button type="button" onclick="speakGerman('${cur.audio.replace(/'/g, "\\'")}', 0.9)" class="px-5 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-black text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer">
                        🔊 Nghe lượt thoại này
                    </button>
                </div>
            </div>
        `;
    }

    function b12_prevV6Step() {
        if (currentV6Step > 0) {
            currentV6Step--;
            b12_renderKlinikSceneSvg();
        }
    }

    function b12_nextV6Step() {
        if (currentV6Step < V6_DIALOGUE.length - 1) {
            currentV6Step++;
            b12_renderKlinikSceneSvg();
        }
    }

    function b12_toggleV6Translation() {
        showV6Translation = !showV6Translation;
        b12_renderKlinikSceneSvg();
    }

    // =========================================================================
    // KHỞI TẠO TẤT CẢ SƠ ĐỒ
    // =========================================================================
    function b12_initGesundheitSvgDiagrams() {
        if (typeof currentLesson !== 'undefined' && currentLesson && currentLesson.id !== 26) {
            return;
        }
        b12_renderKoerperkarteSvg();
        b12_renderAkkDativFlowchartSvg();
        b12_renderImperativMachineSvg();
        b12_renderImperativComparisonSvg();
        b12_renderDuerfenControlSvg();
        b12_renderKlinikSceneSvg();
    }

    // Export ra Window (B12 isolated namespace to prevent collision with B11)
    global.b12_renderKoerperkarteSvg = b12_renderKoerperkarteSvg;
    global.b12_selectV1BodyPart = b12_selectV1BodyPart;
    global.b12_renderAkkDativFlowchartSvg = b12_renderAkkDativFlowchartSvg;
    global.b12_selectV2Item = b12_selectV2Item;
    global.b12_renderImperativMachineSvg = b12_renderImperativMachineSvg;
    global.b12_selectV3Verb = b12_selectV3Verb;
    global.b12_renderImperativComparisonSvg = b12_renderImperativComparisonSvg;
    global.b12_selectV4Verb = b12_selectV4Verb;
    global.b12_renderDuerfenControlSvg = b12_renderDuerfenControlSvg;
    global.b12_selectV5Subj = b12_selectV5Subj;
    global.b12_selectV5Action = b12_selectV5Action;
    global.b12_setV5Mode = b12_setV5Mode;
    global.b12_renderKlinikSceneSvg = b12_renderKlinikSceneSvg;
    global.b12_prevV6Step = b12_prevV6Step;
    global.b12_nextV6Step = b12_nextV6Step;
    global.b12_toggleV6Translation = b12_toggleV6Translation;
    global.b12_initGesundheitSvgDiagrams = b12_initGesundheitSvgDiagrams;
    global.initGesundheitSvgDiagrams = b12_initGesundheitSvgDiagrams;

})(typeof window !== 'undefined' ? window : this);
