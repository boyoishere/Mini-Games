import pandas as pd

# creating character mapping
def load(file_path):
    char_map = {"kangxi": {}, "all": {}}
    df = pd.read_csv(file_path, encoding='utf-8')
    for _, row in df.iterrows():
        trad = row['trad']
        kangxi = row['kangxi'] if pd.notna(row['kangxi']) else ''
        all = row['all'] if pd.notna(row['all']) else ''
        # Store the mappings in the dictionary
        if kangxi:
            char_map["kangxi"][trad] = kangxi
        if all:
            char_map["all"][trad] = all
    return char_map

char_map = load("zhengzi/char_map.csv")

while True:
    mode = input("Choose mode ('1' for kangxi or '2' for Vexing): ").strip().lower()
    if mode == '1': mode_key = 'kangxi'
    elif mode == '2': mode_key = 'all'
    else:
        print("Invalid mode. Choose '1' for kangxi or '2' for vexing.")
        continue
    text = input("READY >  ")
    replacements = char_map[mode_key]
    output = ''
    for char in text:
        if char in replacements:
            output += replacements[char]
        else:
            output += char
    # output = ''.join([char_map[mode_key].get(char, char) for char in text])
    print("=======================================")
    print(f"OUTPUT > {output}")
    exit_code = input("Type '3' to quit or press Enter to continue: ").strip().lower()
    if exit_code == '3':
        break

# Sample input: 下週已約好去吃麵，聽說那家店的花椒牛肉麵真不錯，強烈推薦！吃完順便去前面的花市逛逛，聽說最近花開得特別好。