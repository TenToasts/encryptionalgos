# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 07:39:55 2017

@author: Animesh
"""
#Used to add later values to key matrix
alphabetList = 'abcdefghiklmnopqrstuvwxyz'

Matrix = [] #defining size
keyMatrix = []
            
key = input("Enter a key")
plainText = input("Enter Plain Text")
cipherArray = []
cipherText = ""



#creating key matrix
for char in key:
    if char not in Matrix:
        Matrix.append(char)
        
for char in alphabetList:
    if char not in Matrix:
        Matrix.append(char)
        
for e in range(5): #creating a 2d matrix
    keyMatrix.append('')
        
keyMatrix[0] = Matrix[0:5]
keyMatrix[1] = Matrix[5:10]
keyMatrix[2] = Matrix[10:15]
keyMatrix[3] = Matrix[15:20]
keyMatrix[4] = Matrix[20:25]

#converting key to digraphs
message = []
for char in plainText:
    message.append(char)
    
for unused in range(len(message)):
    if " " in message:
        message.remove(" ")
        
        
i = 0 #creating counter
for char in range(int(len(message) / 2)): #check for repeating letter
    if message[i] == message[i + 1]:
        message.insert(i + 1, 'x')
    
    i = i + 2
    
if len(message) % 2 == 1:
    message.append('x') #add x at end if length of text is even

i = 0
digraphArray = []    
for x in range(len(message) // 2):
    digraphArray.append(message[i:i+2])
    i = i + 2

#converting to cipherText

print(keyMatrix)

for twoLetters in digraphArray:  
    for x in range(5):
        for y in range(5):
            if twoLetters[0] == keyMatrix[x][y]:
                x1 = x
                y1 = y
           
            if twoLetters[1] == keyMatrix[x][y]:
                x2 = x 
                y2 = y
                
    if y1 == y2:
        x1 = (x1+1) % 4
        x2 = (x2+1) % 4
        cipherArray.append(keyMatrix[x1][y1])
        cipherArray.append(keyMatrix[x2][y2])
             
    elif x1 == x2:
        y1 = (y1+1) % 4
        y2 = (y2+1) % 4
        cipherArray.append(keyMatrix[x1][y1])
        cipherArray.append(keyMatrix[x2][y2])
        
    else:
        cipherArray.append(keyMatrix[x1][y2])
        cipherArray.append(keyMatrix[x2][y1])

cipherText = cipherText.join(cipherArray)
        
print(cipherText)

i = 0 #creating counter

newPlainArray = []
cipherDigraphArray = []
newPlainText = ""    
for x in range(len(cipherText) // 2):
    cipherDigraphArray.append(cipherArray[i:i+2])
    i = i + 2

for twoLetters in cipherDigraphArray:  
    for x in range(5):
        for y in range(5):
            if twoLetters[0] == keyMatrix[x][y]:
                x1 = x
                y1 = y
           
            if twoLetters[1] == keyMatrix[x][y]:
                x2 = x 
                y2 = y
                
    if y1 == y2:
        x1 = (x1-1) % 4
        x2 = (x2-1) % 4
        newPlainArray.append(keyMatrix[x1][y1])
        newPlainArray.append(keyMatrix[x2][y2])
             
    elif x1 == x2:
        y1 = (y1-1) % 4
        y2 = (y2-1) % 4
        newPlainArray.append(keyMatrix[x1][y1])
        newPlainArray.append(keyMatrix[x2][y2])
        
    else:
        newPlainArray.append(keyMatrix[x1][y2])
        newPlainArray.append(keyMatrix[x2][y1])

for unused in range(len(newPlainArray)):
    if 'x' in newPlainArray:
        newPlainArray.remove('x')

newPlainText = newPlainText.join(newPlainArray)
        
print(newPlainText)






