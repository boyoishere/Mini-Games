#--------------------------------------
import pandas as pd
#--------------------------------------
# FUNCTION
#--------------------------------------
def load(file_path):
    char_map = {"boyo": {}, "all": {}}
    df = pd.read_csv(file_path, encoding='utf-8')
    for _, row in df.iterrows():
        trad = row['trad']
        boyo = row['boyo'] if pd.notna(row['boyo']) else ''
        all = row['all'] if pd.notna(row['all']) else ''
        # Store the mappings in the dictionary
        if boyo:
            char_map["boyo"][trad] = boyo
        if all:
            char_map["all"][trad] = all
    return char_map

char_map = load("zhengzi/char_map.csv")

while True:
    mode = input("===\nChoose mode ('1' for boyo Standards or '2' to be annoying): ").strip().lower()
    if mode == '1': mode_key = 'boyo'
    elif mode == '2': mode_key = 'all'
    else:
        print("Invalid mode. Choose '1' for boyo Standards or '2' to be annoying): ")
        continue
    text = input("\nREADY >  ")
    replacements = char_map[mode_key]
    output = ''
    i = 0  # Initialize index to process the text
    while i < len(text):
        # Look for multi-character replacements starting at the current position
        for j in range(i + 1, len(text) + 1):
            term = text[i:j]
            if term in replacements:
                output += replacements[term]  # Replace the term
                i = j  # Move the index past the replaced term
                break
        else:
            # If no multi-character match is found, replace single character
            output += text[i]
            i += 1  # Move index forward for the next character
    print(f"OUTPUT > {output}\n")
    exit_code = input("Type '3' to quit or press Enter to continue: ").strip().lower()
    if exit_code == '3':
        break