import pandas as pd

def load(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')
    return {"casual": {row['trad']: row['casual'] for _, row in df.iterrows() if pd.notna(row['casual'])},
            "annoy": {row['trad']: row['annoy'] for _, row in df.iterrows() if pd.notna(row['annoy'])}}

char_map = load("zhengzi/char_map.csv")

while True:
    mode = input("Choose mode ('casual' or 'annoy'): ").strip().lower()
    if mode not in char_map: print("Invalid mode. Choose 'casual' or 'annoy'."); continue
    text = input("Enter your text: ")
    converted_text = ''.join([char_map[mode].get(char, char) for char in text])
    print(f"Converted text: {converted_text}")
    if input("Type 'exit' to quit or press Enter to continue: ").strip().lower() == 'exit': break

# Sample input: 下週已約好去吃麵，聽說那家店的花椒牛肉麵真不錯，強烈推薦！吃完順便去前面的花市逛逛，聽說最近花開得特別好。