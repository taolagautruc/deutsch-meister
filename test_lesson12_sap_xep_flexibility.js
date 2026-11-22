const assert = require('assert');

function normalizeGermanEquiv(str) {
    if (!str || typeof str !== 'string') return '';
    return str
        .toLowerCase()
        .normalize('NFC')
        .replace(/ä/g, 'ae')
        .replace(/ö/g, 'oe')
        .replace(/ü/g, 'ue')
        .replace(/ß/g, 'ss')
        .replace(/\s+/g, ' ')
        .trim();
}

function checkSapXepAnswer(userAnswer, candidates) {
    if (!userAnswer || typeof userAnswer !== 'string') return false;
    const raw = userAnswer.trim();
    if (/[.,!?:;]\s*[.,!?:;]/.test(raw)) {
        return false;
    }
    const normUser = normalizeGermanEquiv(raw);
    const userNoEnd = normUser.replace(/[.!?]+$/, '').trim();
    if (/[.!?]/.test(userNoEnd)) return false;

    for (const cand of candidates) {
        if (!cand) continue;
        const normCand = normalizeGermanEquiv(cand);
        if (normUser === normCand) return true;
        const candNoEnd = normCand.replace(/[.!?]+$/, '').trim();
        if (userNoEnd === candNoEnd) return true;
    }
    return false;
}

const testSuites = [
    {
        name: "Câu 93: Nehmen Sie bitte die Tabletten nach dem Essen!",
        candidates: [
            "Nehmen Sie bitte die Tabletten nach dem Essen!",
            "Bitte nehmen Sie die Tabletten nach dem Essen!",
            "Nehmen Sie die Tabletten bitte nach dem Essen!",
            "Nehmen Sie nach dem Essen bitte die Tabletten!",
            "Bitte nehmen Sie nach dem Essen die Tabletten!"
        ],
        validTests: [
            "Nehmen Sie bitte die Tabletten nach dem Essen!",
            "Nehmen Sie bitte die Tabletten nach dem Essen",
            "nehmen sie bitte die tabletten nach dem essen!",
            "Bitte nehmen Sie die Tabletten nach dem Essen!",
            "bitte nehmen sie die tabletten nach dem essen",
            "Nehmen Sie die Tabletten bitte nach dem Essen!",
            "Nehmen Sie nach dem Essen bitte die Tabletten!",
            "Bitte nehmen Sie nach dem Essen die Tabletten!"
        ],
        invalidTests: [
            "Nehmen Sie bitte die Tabletten nach dem Essen ! !",
            "Nehmen Sie bitte die Tabletten nach dem Essen!!",
            "Nehmen Sie bitte die Tabletten nach dem Essen auf",
            "Nehmen Sie bitte die Tabletten"
        ]
    },
    {
        name: "Câu 94: Räumt eure Zimmer auf!",
        candidates: [
            "Räumt eure Zimmer auf!"
        ],
        validTests: [
            "Räumt eure Zimmer auf!",
            "Räumt eure Zimmer auf",
            "Raeumt eure Zimmer auf!",
            "raeumt eure zimmer auf",
            "RÄUMT EURE ZIMMER AUF!"
        ],
        invalidTests: [
            "Räumt eure Zimmer auf ! !",
            "Räumt eure Zimmer auf!!",
            "Räumt eure Zimmer auf auf",
            "Räumt eure Zimmer"
        ]
    },
    {
        name: "Câu 95: Iss weniger Schokolade!",
        candidates: [
            "Iss weniger Schokolade!"
        ],
        validTests: [
            "Iss weniger Schokolade!",
            "Iss weniger Schokolade",
            "iss weniger schokolade!",
            "iss weniger schokolade"
        ],
        invalidTests: [
            "Iss weniger Schokolade ! !",
            "Iss weniger Schokolade!!",
            "Iss weniger Schokolade mehr",
            "Iss Schokolade"
        ]
    },
    {
        name: "Câu 96: Im Wartezimmer darf man nicht telefonieren.",
        candidates: [
            "Im Wartezimmer darf man nicht telefonieren.",
            "Man darf im Wartezimmer nicht telefonieren.",
            "Man darf nicht im Wartezimmer telefonieren."
        ],
        validTests: [
            "Im Wartezimmer darf man nicht telefonieren.",
            "Im Wartezimmer darf man nicht telefonieren",
            "im wartezimmer darf man nicht telefonieren.",
            "Man darf im Wartezimmer nicht telefonieren.",
            "man darf im wartezimmer nicht telefonieren",
            "Man darf nicht im Wartezimmer telefonieren."
        ],
        invalidTests: [
            "Im Wartezimmer darf man nicht telefonieren . .",
            "Im Wartezimmer darf man nicht telefonieren..",
            "Im Wartezimmer darf man telefonieren",
            "Im Wartezimmer darf man nicht rauchen"
        ]
    },
    {
        name: "Câu 97: Ich vermisse dich jeden Tag.",
        candidates: [
            "Ich vermisse dich jeden Tag.",
            "Jeden Tag vermisse ich dich.",
            "Dich vermisse ich jeden Tag."
        ],
        validTests: [
            "Ich vermisse dich jeden Tag.",
            "Ich vermisse dich jeden Tag",
            "ich vermisse dich jeden tag",
            "Jeden Tag vermisse ich dich.",
            "jeden tag vermisse ich dich",
            "Dich vermisse ich jeden Tag.",
            "dich vermisse ich jeden tag"
        ],
        invalidTests: [
            "Ich vermisse dich jeden Tag . .",
            "Ich vermisse dich jeden Tag dich",
            "Ich vermisse dich"
        ]
    },
    {
        name: "Câu 98: Die Hausärztin gibt mir eine Salbe.",
        candidates: [
            "Die Hausärztin gibt mir eine Salbe.",
            "Mir gibt die Hausärztin eine Salbe.",
            "Eine Salbe gibt mir die Hausärztin."
        ],
        validTests: [
            "Die Hausärztin gibt mir eine Salbe.",
            "Die Hausärztin gibt mir eine Salbe",
            "Die Hausaerztin gibt mir eine Salbe.",
            "die hausaerztin gibt mir eine salbe",
            "Mir gibt die Hausärztin eine Salbe.",
            "Eine Salbe gibt mir die Hausärztin."
        ],
        invalidTests: [
            "Die Hausärztin gibt mir eine Salbe . .",
            "Die Hausärztin gibt mir eine Salbe mir",
            "Die Hausärztin gibt mir"
        ]
    },
    {
        name: "Câu 99: Mein Bruder hat Bauchschmerzen.",
        candidates: [
            "Mein Bruder hat Bauchschmerzen.",
            "Bauchschmerzen hat mein Bruder."
        ],
        validTests: [
            "Mein Bruder hat Bauchschmerzen.",
            "Mein Bruder hat Bauchschmerzen",
            "mein bruder hat bauchschmerzen",
            "Bauchschmerzen hat mein Bruder.",
            "bauchschmerzen hat mein bruder"
        ],
        invalidTests: [
            "Mein Bruder hat Bauchschmerzen . .",
            "Mein Bruder hat Bauchschmerzen hat",
            "Mein Bruder hat"
        ]
    },
    {
        name: "Câu 100: Darf ich im Bett frühstücken?",
        candidates: [
            "Darf ich im Bett frühstücken?",
            "Darf ich frühstücken im Bett?"
        ],
        validTests: [
            "Darf ich im Bett frühstücken?",
            "Darf ich im Bett frühstücken",
            "Darf ich im Bett fruehstuecken?",
            "darf ich im bett fruehstuecken",
            "Darf ich frühstücken im Bett?",
            "darf ich fruehstuecken im bett"
        ],
        invalidTests: [
            "Darf ich im Bett frühstücken ? ?",
            "Darf ich im Bett frühstücken??",
            "Darf ich im Bett frühstücken heute",
            "Darf ich frühstücken"
        ]
    }
];

let totalPassed = 0;
let totalFailed = 0;

testSuites.forEach(suite => {
    console.log(`\nTesting ${suite.name}`);
    let passCount = 0;
    suite.validTests.forEach(test => {
        const res = checkSapXepAnswer(test, suite.candidates);
        if (res) {
            passCount++;
            totalPassed++;
        } else {
            console.error(`  FAIL valid: "${test}"`);
            totalFailed++;
        }
    });

    suite.invalidTests.forEach(test => {
        const res = checkSapXepAnswer(test, suite.candidates);
        if (!res) {
            passCount++;
            totalPassed++;
        } else {
            console.error(`  FAIL invalid (should reject): "${test}"`);
            totalFailed++;
        }
    });
    console.log(`  -> Passed ${passCount} / ${suite.validTests.length + suite.invalidTests.length} tests.`);
});

console.log(`\n========================================`);
console.log(`TOTAL: ${totalPassed} PASSED, ${totalFailed} FAILED`);
console.log(`========================================`);
if (totalFailed > 0) process.exit(1);
