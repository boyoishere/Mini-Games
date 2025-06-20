import random

# List of all Ideographic Description Characters (IDCs)
idc_chars = [
    "⿰", "⿱", "⿲", "⿳", "⿴", 
    "⿸", "⿹", "⿺", "⿽"
]
# If you want to re-add the omitted ones later:
# "⿾", "⿻", "⿿", "⿵", "⿶", "⿷", "⿼"

def generate_idc_sequence(num_chars):
    # Randomly choose `num_chars` IDCs from the list (with replacement)
    return ' '.join(random.choices(idc_chars, k=num_chars))

def main():
    print("Ideographic Description Character (IDC) Sequence Generator")
    try:
        num = int(input("Enter the number of characters to generate: "))
        if num <= 0:
            print("Please enter a positive integer.")
            return
        sequence = generate_idc_sequence(num)
        print(f"Generated sequence:\n{sequence}")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()
