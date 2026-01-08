from bot import correct_english

while True:
    text = input("Enter a sentence (or 'exit'): ")
    if text.lower() == "exit":
        break

    corrected = correct_english(text)
    print("Corrected:", corrected)
