import pandas as pd

def load(file_path):
    # Initialize a dictionary to store casual and annoy character mappings
    char_map = {"casual": {}, "annoy": {}}
    
    # Read the CSV file using pandas
    df = pd.read_csv(file_path, encoding='utf-8')

    # Iterate over the rows in the DataFrame
    for _, row in df.iterrows():
        trad = row['trad']
        casual = row['casual'] if pd.notna(row['casual']) else ''
        annoy = row['annoy'] if pd.notna(row['annoy']) else ''
        
        # Store the mappings in the dictionary
        if casual:
            char_map["casual"][trad] = casual
        if annoy:
            char_map["annoy"][trad] = annoy
    
    return char_map

# Load the character mappings from the CSV file
char_map = load("zhengzi/char_map.csv")

while True:
    # Prompt user to select a mode: 'casual' or 'annoy'
    mode = input("Choose mode ('casual' or 'annoy'): ").strip().lower()

    # Ensure the mode is valid
    if mode not in char_map:
        print("Invalid mode. Choose 'casual' or 'annoy'.")
        continue

    # Get the text to process
    text = input("Enter your text: ")

    # Get the dictionary of replacements for the selected mode
    replacements = char_map[mode]

    # Replace traditional characters with their corresponding casual/annoy versions
    converted_text = ''
    for char in text:
        # If a replacement exists in the selected mode, replace it
        if char in replacements:
            converted_text += replacements[char]
        else:
            # If no replacement exists, keep the character unchanged
            converted_text += char

    # Output the converted text
    print(f"Converted text: {converted_text}")

    # Check if the user wants to exit
    exit_code = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
    if exit_code == 'exit':
        break

# Sample input: 下週已約好去吃麵，聽說那家店的花椒牛肉麵真不錯，強烈推薦！吃完順便去前面的花市逛逛，聽說最近花開得特別好。