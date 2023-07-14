from textblob import TextBlob

def correct_word(word):
    blob = TextBlob(word)
    corrected_word = blob.correct()
    return str(corrected_word)

input_word = input("Enter a word: ")
corrected_word = correct_word(input_word)

print(f"Corrected word: {corrected_word}")
