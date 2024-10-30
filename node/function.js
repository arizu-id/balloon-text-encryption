const fs = require('fs');

// Function to generate a random string
function randStr(length, varStr = 'oO0') {
    let string = '';
    for (let i = 0; i < length; i++) {
        const pos = Math.floor(Math.random() * varStr.length);
        string += varStr[pos];
    }
    return string;
}

// Function to create a new encryption hash
function ozeroNewEncryption() {
    const jsonArray = JSON.parse(fs.readFileSync("words.json", "utf8"));
    let words = {};
    let wordsHash = {};

    while (true) {
        const rand = randStr(10);
        if (wordsHash[rand]) {
            console.log("[!] Some hashed value already added, trying..");
            continue; // Retry if the hashed value already exists
        }
        // Add the new random string and its corresponding key
        words[rand] = rand;
        wordsHash[rand] = Object.keys(jsonArray).length; // Using the key as the index
        break; // Exit the loop if a unique hash is added
    }

    // Save the results to the files
    fs.writeFileSync('words_hash.json', JSON.stringify(wordsHash, null, 4));
    fs.writeFileSync('words.json', JSON.stringify(words, null, 4));
    return true;
}

// Function to hash a given text
function ozeroHash(text) {
    const jsonArray = JSON.parse(fs.readFileSync("words.json", "utf8"));
    const characters = text.split('');
    let returnStr = "";
    for (const char of characters) {
        returnStr += jsonArray[char] || ''; // Handle undefined characters
    }
    return returnStr;
}

// Function to decode a hashed text
function ozeroDecode(text) {
    const jsonArray = JSON.parse(fs.readFileSync("words_hash.json", "utf8"));
    const characters = text.match(/.{1,10}/g) || []; // Split into chunks of 10
    let returnStr = "";
    for (const char of characters) {
        returnStr += jsonArray[char] || ''; // Handle undefined characters
    }
    return returnStr;
}

// ozeroNewEncryption(); // to make new hash key data
const text = "Ini Teks Apa Njir?";
const hashed = ozeroHash(text);
const unhash = ozeroDecode(hashed);
console.log(`Text : ${text}`);
console.log(`Encrypted : ${hashed}`);
console.log(`Decrypted : ${unhash}`);
