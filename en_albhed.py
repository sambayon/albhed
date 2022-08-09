albhed ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"
alphabet ="epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ"
text = input('Translate your Al Bhed text to English: ')

def translator(text):
    result = ""
    for letter in text:
        if letter in albhed:
            result += alphabet[albhed.find(letter)]
        else:
            result += letter
    return result

print(translator(text))