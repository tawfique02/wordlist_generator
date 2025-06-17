# Advanced Wordlist Generator

An advanced password wordlist generator that creates human-like, rockyou-style password lists.  
Ideal for penetration testing, password auditing, and security research.

---

## Features

- Generates realistic passwords using pet names, common leaked passwords, years, digits, and symbols.
- Randomized patterns to simulate real-world password usage.
- Generates large wordlists (default 100,000 passwords) quickly.
- Progress bars for generation and saving using `tqdm`.
- Output saved as `wordlist.txt` by default.
- Easy to customize word sources, patterns, and output size.

---
Start by cloning this repository to unlock powerful wordlist generation and kick off your password cracking journey:
```
git clone 
```
## Requirements
- Python 3.x
- `tqdm` package (for progress bars)

Install requirements with:

```bash

pip install -r requirements.txt
```
🚀 Termux Setup & Run Commands for Wordlist Generator
1. Update Termux packages
```
pkg update -y && pkg upgrade -y
Install Python and pip
pkg install python -y
cd wordlist-generator
python3 wordlist_generator.py
```
Wait for the generation to complete. The wordlist will be saved as:
```
wordlist.txt
```
🚀 Linux Setup & Run Commands for Wordlist Generator
1. Update system packages
```
sudo apt update && sudo apt upgrade -y
```
2. Install Python3 and pip
```
sudo apt install python3 python3-pip -y
pip3 install -r requirements.txt
cd wordlist-generator
python3 wordlist_generator.py
```



Example Output:
```
graphql
Copy
Edit
charlie123
lucy2024
password!
@duke3
rocky321
football@2024
admin123
```
## License
This tool is provided as-is under the [MIT License]()

## Disclaimer
Use responsibly. This tool is intended for ethical penetration testing and educational purposes only. Unauthorized use against systems you do not own or have permission to test is illegal.

Author
Created by [Md Tawfique Elahey]

Feel free to contribute or report issues!
---
