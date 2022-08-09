albhed ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"
alphabet ="epstiwknuvgclrybxhmdofzqajEPSTIWKNUVGCLRYBXHMDOFZQAJ"
text = input('Write your text: ')

def translator(text):
    result = ""
    for letter in text:
        if letter in alphabet:
            result += albhed[alphabet.find(letter)]
        else:
            result += letter
    return result

print(translator(text))