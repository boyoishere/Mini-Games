# English to Chinese mapping based on the provided chart
translation_map = {
    "i": "俉", "me": "侎", "my": "亻萬", "mine": "僈",
    "you": "儞", "your": "爾", "yours": "𧭉",
    "he": "他", "him": "扡", "his": "倛",
    "she": "她", "her": "妸", "hers": "𫱊",
    "it": "其", "its": "之",
    "we": "偎", "us": "亻亞", "our": "𬿪", "ours": "𬤡・䜒",
    "they": "𫣓", "them": "𠎬", "their": "代", "theirs": "㑀"
}

def enzi(text):
    words = text.split()  # Split the input into words
    translated_words = [translation_map.get(word, word) for word in words]
    return ' '.join(translated_words)

# MIAIN
input_text = str(input("Input here: ")).lower()
translated_text = enzi(input_text)

# Result
print("Original text:", input_text)
print("Translated text:", translated_text)
