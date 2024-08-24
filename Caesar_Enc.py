
def Enc(text, shift):
    new_word = ""
    for i in text:
        if i.isalpha():
            start = ord('A') if i.isupper() else ord('a')

            new_char = chr((ord(i) - start + shift) % 26 + start)
            new_word += new_char
        else:
            new_word += i
    return new_word





