import string
import random
from itertools import product
from tqdm import tqdm  # install via: pip install tqdm
from colorama import Fore, Style, init  # install via: pip install colorama
import time

init(autoreset=True)  # Auto reset colors after print


BANNER = r"""
 __        __   _                            _     _ _           
 \ \      / /__| | ___ ___  _ __ ___   ___  | |   (_) |_ ___     
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | |   | | __/ _ \    
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | |___| | ||  __/    
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_____|_|\__\___|    
                                                                
      Advanced Wordlist Generator — by ChatGPT                 
"""

GUIDELINE = """
GUIDELINES:
- Generates wordlists combining digits, special characters, pet names, uppercase & lowercase letters.
- Multiple customizable patterns supported.
- Pet names auto-capitalized (lower, Capitalized, UPPER).
- Progress bar to monitor generation.
- Output file is shuffled for randomness.
- Use `max_lines` param to limit wordlist size.
- Install required packages: `pip install tqdm colorama`
"""

def print_pattern_summary_colored(pattern, completed, total, elapsed_seconds, speed):
    check = Fore.GREEN + "✔" + Style.RESET_ALL
    pattern_text = Fore.CYAN + pattern + Style.RESET_ALL
    minutes = int(elapsed_seconds // 60)
    seconds = int(elapsed_seconds % 60)
    time_str = f"{minutes:02}:{seconds:02}"
    speed_str = f"{int(speed):,} it/s"
    
    print(f"[{check}] Pattern: {pattern_text:<30} | Completed {completed:>7,} / {total:<7,} | Time: {time_str} | Speed: {speed_str}")


class WordlistGenerator:
    def __init__(self, 
                 digits=string.digits, 
                 special_chars='"!@$%^&*()', 
                 pet_names=None,
                 patterns=None,
                 capitalize_pets=True,
                 shuffle_output=True,
                 max_lines=None,
                 filename='wordlist_advanced.txt'):
        
        self.digits = digits
        self.special_chars = special_chars
        self.pet_names = pet_names or ["max","charlie","cooper","jack","rocky","bear","roxy","lucy","duke","toby"]
        self.patterns = patterns or [
            "{digit}{special}{pet}{upper}{lower}",
            "{pet}{digit}{special}{lower}{upper}",
            "{upper}{pet}{special}{digit}{lower}",
            "{special}{pet}{digit}{upper}{lower}",
        ]
        self.capitalize_pets = capitalize_pets
        self.shuffle_output = shuffle_output
        self.max_lines = max_lines
        self.filename = filename
    
    def _get_pet_variations(self):
        pets = set()
        for pet in self.pet_names:
            pets.add(pet.lower())
            if self.capitalize_pets:
                pets.add(pet.capitalize())
                pets.add(pet.upper())
        return sorted(pets)
    
    def generate(self):
        pets = self._get_pet_variations()
        
        pools = {
            'digit': list(self.digits),
            'special': list(self.special_chars),
            'pet': pets,
            'upper': list(string.ascii_uppercase),
            'lower': list(string.ascii_lowercase)
        }
        
        # Estimate total combinations for info
        est_total = 0
        for pattern in self.patterns:
            keys = []
            temp = pattern
            while True:
                start = temp.find("{")
                if start == -1:
                    break
                end = temp.find("}", start)
                key = temp[start+1:end]
                keys.append(key)
                temp = temp[end+1:]
            count = 1
            for key in keys:
                count *= len(pools[key])
            est_total += count
        
        print(BANNER)
        print(GUIDELINE)
        print(f"Estimated total words to generate: ~{est_total:,}")
        print(f"Output file: {self.filename}")
        print(f"Max lines: {'Unlimited' if not self.max_lines else self.max_lines}")
        print("Starting generation...\n")
        
        written = 0
        with open(self.filename, 'w') as file:
            for pattern in self.patterns:
                keys = []
                temp = pattern
                while True:
                    start = temp.find("{")
                    if start == -1:
                        break
                    end = temp.find("}", start)
                    key = temp[start+1:end]
                    keys.append(key)
                    temp = temp[end+1:]
                
                total_for_pattern = 1
                for k in keys:
                    total_for_pattern *= len(pools[k])
                
                start_time = time.time()
                for combo in tqdm(product(*(pools[key] for key in keys)), total=total_for_pattern, desc=f"Pattern: {pattern}"):
                    word = pattern
                    for key, val in zip(keys, combo):
                        word = word.replace(f"{{{key}}}", val, 1)
                    
                    file.write(word + "\n")
                    written += 1
                    if self.max_lines and written >= self.max_lines:
                        break
                elapsed = time.time() - start_time
                speed = total_for_pattern / elapsed if elapsed > 0 else total_for_pattern
                print_pattern_summary_colored(pattern, min(written, total_for_pattern), total_for_pattern, elapsed, speed)
                if self.max_lines and written >= self.max_lines:
                    print(f"\nReached max lines limit: {self.max_lines}\n")
                    break
        
        if self.shuffle_output:
            print("\nShuffling the wordlist for randomness...")
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            random.shuffle(lines)
            with open(self.filename, 'w') as f:
                f.writelines(lines)
        
        print(f"\n✅ Wordlist generation complete! Total entries: {written:,}")
        print(f"Saved to: {self.filename}\n")


if __name__ == "__main__":
    # Customize parameters here:
    wg = WordlistGenerator(max_lines=500000)  # Set None for unlimited size
    wg.generate()
