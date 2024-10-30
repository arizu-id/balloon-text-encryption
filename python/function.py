import json
import random

# Fungsi untuk menghasilkan string acak
def rand_str(length, var='oO0'):
    return ''.join(random.choice(var) for _ in range(length))

# Fungsi untuk membuat hash enkripsi baru
def ozero_new_encryption():
    with open("words.json", "r", encoding="utf-8") as f:
        json_array = json.load(f)

    words = {}
    words_hash = {}

    while True:
        rand = rand_str(10)
        if rand in words_hash:
            print("[!] Some hashed value already added, trying..")
            continue  # Ulangi jika nilai hash sudah ada

        # Tambahkan string acak baru dan kunci yang sesuai
        for key in json_array.keys():
            words[key] = rand
            words_hash[rand] = key
            break  # Keluar dari loop setelah menambahkan hash yang unik

    # Simpan hasil ke dalam file
    with open('words_hash.json', 'w', encoding='utf-8') as f:
        json.dump(words_hash, f, ensure_ascii=False, indent=4)
    with open('words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=4)

    return True

# Fungsi untuk meng-hash teks yang diberikan
def ozero_hash(text):
    with open("words.json", "r", encoding="utf-8") as f:
        json_array = json.load(f)

    return_str = ""
    for char in text:
        return_str += json_array.get(char, '')  # Tangani karakter yang tidak terdefinisi
    return return_str

# Fungsi untuk mendekode teks yang di-hash
def ozero_decode(text):
    with open("words_hash.json", "r", encoding="utf-8") as f:
        json_array = json.load(f)

    characters = [text[i:i + 10] for i in range(0, len(text), 10)]  # Bagi menjadi potongan 10 karakter
    return_str = ""
    for char in characters:
        return_str += json_array.get(char, '')  # Tangani karakter yang tidak terdefinisi
    return return_str

# ozero_new_encryption()  # Uncomment untuk membuat data kunci hash baru
text = "Ini Teks Apa Njir?"
hashed = ozero_hash(text)
unhash = ozero_decode(hashed)

print(f"Text : {text}")
print(f"Encrypted : {hashed}")
print(f"Decrypted : {unhash}")
