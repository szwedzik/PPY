def ceaserCipher(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''
    for character in message:
        if character.lower() in alphabet:
            position = (alphabet.index(character.lower()) + key) % len(alphabet)
            if character.isupper():
                newMessage += alphabet[position].upper()
            else:
                newMessage += alphabet[position]
        else:
            newMessage += character
    print(newMessage)

message = input("Podaj wiadomość: ")
key = int(input("Podaj klucz: "))
ceaserCipher(message, key)