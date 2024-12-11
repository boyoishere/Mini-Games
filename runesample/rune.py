def load_rune_mapping(filename):
    rune_map = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        for i in range(0, len(lines), 2):
            eng_letter = lines[i].strip()  # Read letter
            rune = lines[i+1].strip()      # Read corresponding rune
            rune_map[eng_letter] = rune    # Add to mapping
            
    return rune_map

def english_to_runes(text, rune_map):
    return ''.join([rune_map.get(char.lower(), char) for char in text])

# Load the rune mapping from the file
rune_map = load_rune_mapping('runesample/rune_mapping.txt')
print(rune_map)
# Example usage:
# input_text = input(str('what do you wanna convert? '))
# runic_text = english_to_runes(input_text, rune_map)
# print("Original:", input_text)
# print("Runic:", runic_text)
