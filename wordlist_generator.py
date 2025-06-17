
import string
import random
from tqdm import tqdm

def print_banner():
    banner = """
╔══════════════════════════════════════════════╗
║      🔐 Advanced Wordlist Generator 🔐       ║
║   Generates human-like passwords similar to  ║
║   real-world leaks (rockyou-style)           ║
║   Developed by: Tawfique Elahey              ║              
╚══════════════════════════════════════════════╝
"""
    print(banner)

def generate_rockyou_style_wordlist(
    output_file='wordlist.txt',
    num_passwords=100_000,
    shuffle=True
):
    pet_names = [
        "max", "charlie", "cooper", "jack", "rocky", "bear",
        "roxy", "lucy", "duke", "toby", "bella", "milo"
    ]

    common_words = [
        "password", "admin", "welcome", "letmein", "dragon",
        "qwerty", "football", "monkey", "hello", "sunshine"
    ]

    years = ["2020", "2021", "2022", "2023", "2024", "2025"]
    suffixes = ["123", "!", "@", "#1", "1234", "321", "12"]
    digits = string.digits
    symbols = "!@#$%&*"

    patterns = [
        lambda w: w + random.choice(suffixes),
        lambda w: w.capitalize() + random.choice(years),
        lambda w: w + random.choice(digits) + random.choice(symbols),
        lambda w: random.choice(symbols) + w + random.choice(digits),
        lambda w: w,
        lambda w: w + random.choice(years),
        lambda w: w.capitalize() + random.choice(suffixes),
    ]

    base_words = pet_names + common_words
    wordlist = []

    print(f"\nGenerating {num_passwords:,} passwords...\n")

    for _ in tqdm(range(num_passwords), desc="Creating passwords", unit="pwd"):
        base = random.choice(base_words)
        pattern = random.choice(patterns)
        password = pattern(base)
        wordlist.append(password)

    if shuffle:
        random.shuffle(wordlist)

    with open(output_file, 'w') as file:
        for pwd in tqdm(wordlist, desc="Saving to file", unit="pwd"):
            file.write(pwd + '\n')

    print(f"\n✅ Wordlist saved to: {output_file}\n")

# ========== MAIN ==========
if __name__ == "__main__":
    print_banner()
    generate_rockyou_style_wordlist()

