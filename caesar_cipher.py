plainText = input("Enter a text: ")
key = int(input("Enter a key: "))
cipherText= ""

for char in plainText:
    if char == ' ':
        cipherText += ' '
        continue
    asciiText = ord(char)
    asciiText -= 97 
    newAscii = (asciiText + key) % 26
    newAscii += 97
    cipherText += chr(newAscii)
    
print(cipherText)
    
    