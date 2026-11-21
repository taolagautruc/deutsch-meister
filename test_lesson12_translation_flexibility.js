const fs = require('fs');
const path = require('path');

// Mock browser window/global
const mockWindow = {};
global.window = mockWindow;

// Read and evaluate gesundheit_svg.js
const gesundheitCode = fs.readFileSync(path.join(__dirname, 'static/js/gesundheit_svg.js'), 'utf-8');
const evaluateScript = new Function('global', 'window', gesundheitCode);
evaluateScript(mockWindow, mockWindow);

const evaluateLesson12DVTranslation = mockWindow.evaluateLesson12DVTranslation;
const evaluateLesson12VDTranslation = mockWindow.evaluateLesson12VDTranslation;

if (typeof evaluateLesson12DVTranslation !== 'function' || typeof evaluateLesson12VDTranslation !== 'function') {
    console.error('FAIL: Functions not properly exported!');
    process.exit(1);
}

const testCases = [
    // --- VIỆT -> ĐỨC (Q81 - Q86) ---
    {
        qNum: 81,
        type: 'VD',
        name: 'Câu 81: Ngài hãy uống nhiều nước!',
        valid: [
            'Trinken Sie viel Wasser!',
            'Trinken Sie viel Wasser',
            'Trinken Sie bitte viel Wasser!',
            'Trinken Sie viel Wasser, bitte!',
            'Bitte trinken Sie viel Wasser!',
            'trinken sie viel wasser'
        ],
        invalid: [
            'Trink viel Wasser!',
            'Trinkt viel Wasser!',
            'Sie trinken viel Wasser.',
            'Trinken Sie bitte viel Milch!'
        ]
    },
    {
        qNum: 82,
        type: 'VD',
        name: 'Câu 82: Ở đây người ta không được phép hút thuốc.',
        valid: [
            'Hier darf man nicht rauchen.',
            'Hier darf man nicht rauchen',
            'Man darf hier nicht rauchen.',
            'Man darf hier nicht rauchen',
            'hier darf man nicht rauchen'
        ],
        invalid: [
            'Hier man darf nicht rauchen.',
            'Hier darf man rauchen.',
            'Hier muss man nicht rauchen.',
            'Hier darf man nicht trinken.'
        ]
    },
    {
        qNum: 83,
        type: 'VD',
        name: 'Câu 83: Hãy làm bài tập về nhà của bạn! (ngôi du)',
        valid: [
            'Mach deine Hausaufgaben!',
            'Mach deine Hausaufgaben',
            'Mach bitte deine Hausaufgaben!',
            'Mach deine Hausaufgaben, bitte!',
            'Bitte mach deine Hausaufgaben!'
        ],
        invalid: [
            'Macht deine Hausaufgaben!',
            'Machen Sie deine Hausaufgaben!',
            'Mach die Hausaufgaben!',
            'Mach seine Hausaufgaben!'
        ]
    },
    {
        qNum: 84,
        type: 'VD',
        name: 'Câu 84: Tôi bị đau đầu dữ dội.',
        valid: [
            'Ich habe starke Kopfschmerzen.',
            'Ich habe starke Kopfschmerzen',
            'Ich habe sehr starke Kopfschmerzen.',
            'Mein Kopf tut mir sehr weh.',
            'Mein Kopf tut mir weh.',
            'Ich habe Kopfschmerzen.'
        ],
        invalid: [
            'Ich bin starke Kopfschmerzen.',
            'Mein Kopf tut mich weh.',
            'Ich habe Bauchschmerzen.',
            'Mein Kopf ist sehr weh.'
        ]
    },
    {
        qNum: 85,
        type: 'VD',
        name: 'Câu 85: Các bạn hãy ăn nhiều rau hơn!',
        valid: [
            'Esst mehr Gemüse!',
            'Esst mehr Gemüse',
            'Esst mehr Gemuese!',
            'Esst bitte mehr Gemüse!',
            'Bitte esst mehr Gemüse!',
            'Esst mehr Gemüse, bitte!'
        ],
        invalid: [
            'Iss mehr Gemüse!',
            'Essen Sie mehr Gemüse!',
            'Esst viel Gemüse!',
            'Ihr esst mehr Gemüse.'
        ]
    },
    {
        qNum: 86,
        type: 'VD',
        name: 'Câu 86: Hãy nghỉ ngơi đi! (ngôi du)',
        valid: [
            'Ruh dich aus!',
            'Ruh dich aus',
            'Ruh dich bitte aus!',
            'Bitte ruh dich aus!',
            'Ruh dich aus, bitte!',
            'Ruhe dich aus!'
        ],
        invalid: [
            'Ruh aus!',
            'Ruh dir aus!',
            'Ruht euch aus!',
            'Ruhen Sie sich aus!'
        ]
    },

    // --- ĐỨC -> VIỆT (Q87 - Q92) ---
    {
        qNum: 87,
        type: 'DV',
        name: 'Câu 87: Atmen Sie bitte tief ein und aus!',
        valid: [
            'Xin ngài hãy hít vào và thở ra thật sâu!',
            'Xin hãy hít vào và thở ra thật sâu!',
            'Hãy hít vào và thở ra thật sâu!',
            'Hãy hít vào và thở ra sâu!',
            'Làm ơn hãy hít vào và thở ra thật sâu!',
            'Hít vào và thở ra thật sâu!',
            'Bác hãy hít vào thở ra thật sâu',
            'xin hay hit vao va tho ra that sau'
        ],
        invalid: [
            'Xin ngài hãy uống thuốc đều đặn!',
            'Hãy thở đều và ngủ đi!',
            'Bác hãy nằm xuống nghỉ ngơi!'
        ]
    },
    {
        qNum: 88,
        type: 'DV',
        name: 'Câu 88: Der Rücken tut ihm weh.',
        valid: [
            'Lưng của anh ấy bị đau.',
            'Lưng anh ấy bị đau.',
            'Anh ấy bị đau lưng.',
            'Ông ấy bị đau lưng.',
            'Cậu ấy bị đau lưng.',
            'Lưng của ông ấy bị đau.',
            'Lưng anh ấy đau.',
            'lung anh ay bi dau'
        ],
        invalid: [
            'Cô ấy bị đau lưng.',
            'Bụng của anh ấy bị đau.',
            'Tôi bị đau lưng.',
            'Anh ấy bị đau đầu.'
        ]
    },
    {
        qNum: 89,
        type: 'DV',
        name: 'Câu 89: Darf ich hier fotografieren?',
        valid: [
            'Tôi có được phép chụp ảnh ở đây không?',
            'Tôi có được chụp ảnh ở đây không?',
            'Tôi có thể chụp ảnh ở đây không?',
            'Tôi chụp ảnh ở đây được không?',
            'Mình có được chụp hình ở đây không?',
            'Ở đây tôi có được chụp ảnh không?',
            'toi co duoc phep chup anh o day khong'
        ],
        invalid: [
            'Tôi không được phép chụp ảnh ở đây.',
            'Anh ấy có được chụp ảnh ở đây không?',
            'Tôi có được hút thuốc ở đây không?',
            'Cấm chụp ảnh ở đây.'
        ]
    },
    {
        qNum: 90,
        type: 'DV',
        name: 'Câu 90: Bleib heute im Bett!',
        valid: [
            'Hôm nay hãy nằm nghỉ trên giường!',
            'Hôm nay hãy ở lại trên giường!',
            'Hôm nay hãy nằm lại trên giường!',
            'Hãy nằm nghỉ trên giường hôm nay!',
            'Hôm nay hãy nghỉ trên giường!',
            'Hôm nay hãy ở trên giường nhé!',
            'Hôm nay hãy nằm trên giường!',
            'hom nay hay nam nghi tren giuong'
        ],
        invalid: [
            'Ngày mai hãy ở lại trên giường!',
            'Hôm nay hãy ra khỏi giường!',
            'Hôm nay hãy đi làm nhé!'
        ]
    },
    {
        qNum: 91,
        type: 'DV',
        name: 'Câu 91: Wir sehen uns jeden Morgen im Bus.',
        valid: [
            'Chúng ta gặp nhau mỗi sáng trên xe buýt.',
            'Chúng tôi gặp nhau mỗi sáng trên xe buýt.',
            'Chúng mình gặp nhau mỗi sáng trên xe buýt.',
            'Chúng ta gặp nhau mỗi buổi sáng trên xe buýt.',
            'Chúng tôi gặp nhau mỗi buổi sáng ở xe buýt.',
            'Chúng ta gặp nhau mỗi sáng trên xe bus.',
            'chung ta gap nhau moi sang tren xe buyt'
        ],
        invalid: [
            'Chúng ta gặp nhau mỗi tối trên xe buýt.',
            'Chúng ta gặp nhau mỗi sáng trên tàu hỏa.',
            'Họ gặp nhau mỗi sáng trên xe buýt.'
        ]
    },
    {
        qNum: 92,
        type: 'DV',
        name: 'Câu 92: Zeigen Sie mir bitte Ihre Zunge!',
        valid: [
            'Xin ngài hãy cho tôi xem lưỡi của ngài!',
            'Xin hãy cho tôi xem lưỡi của ngài!',
            'Hãy cho tôi xem lưỡi của ngài!',
            'Hãy cho tôi xem lưỡi của bạn!',
            'Làm ơn cho tôi xem lưỡi của ngài!',
            'Vui lòng cho tôi xem lưỡi của ngài!',
            'Xin hãy thè lưỡi ra!',
            'Hãy thè lưỡi ra!',
            'xin hay cho toi xem luoi cua ngai'
        ],
        invalid: [
            'Xin ngài hãy cho tôi xem mắt!',
            'Xin ngài hãy há to miệng ra!',
            'Hãy đưa tay cho tôi xem!'
        ]
    }
];

let totalPassed = 0;
let totalFailed = 0;

for (const tc of testCases) {
    console.log(`\nTesting ${tc.name} [Type: ${tc.type}, Q${tc.qNum}]`);
    const evalFn = tc.type === 'VD' ? evaluateLesson12VDTranslation : evaluateLesson12DVTranslation;

    // Check valid variants
    for (const v of tc.valid) {
        const result = evalFn(v, tc.qNum);
        if (result === true) {
            totalPassed++;
        } else {
            totalFailed++;
            console.error(`  ❌ Expected PASS but got FAIL for valid input: "${v}"`);
        }
    }

    // Check invalid variants
    for (const inv of tc.invalid) {
        const result = evalFn(inv, tc.qNum);
        if (result === false) {
            totalPassed++;
        } else {
            totalFailed++;
            console.error(`  ❌ Expected FAIL but got PASS for invalid input: "${inv}"`);
        }
    }
    console.log(`  -> Passed ${tc.valid.length} valid tests and ${tc.invalid.length} invalid tests.`);
}

console.log(`\n========================================`);
console.log(`SUMMARY: ${totalPassed} PASSED, ${totalFailed} FAILED`);
console.log(`========================================`);

if (totalFailed > 0) {
    process.exit(1);
} else {
    console.log('ALL TESTS PASSED WITH 100% SUCCESS!');
    process.exit(0);
}
