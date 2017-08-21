# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:33:22 2017

@author: Animesh
"""
import numpy as np #for matrix multiplication

matrix = []
keyMatrix = []

key = input("Enter key(key length should be 9)")
plainText = input("Enter plain text")

for char in key:
    matrix.append(ord(char)-97)

for e in range(3):
    keyMatrix.append('')
    
keyMatrix[0] = matrix[0:3]
keyMatrix[1] = matrix[3:6]
keyMatrix[2] = matrix[6:9]

print(keyMatrix)

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
    
if len(message) % 3 is 1:
    message.append('x')
    message.append('x')

if len(message) % 3 is 2:
    message.append('x')
    
messageNumberArray = []

for x in message:
    messageNumber = ord(x) - 97
    messageNumberArray.append(messageNumber)
    
i = 0
digraphArray = []    
for x in range(len(message) // 3):
    digraphArray.append(message[i:i+3])
    i = i + 3

i = 0
digraphNumberArray = []    
for x in range(len(messageNumberArray) // 3):
    digraphNumberArray.append(messageNumberArray[i:i+3])
    i = i + 3
    
cipherDigraphNumberArray = []

for x in range(len(digraphNumberArray)):
    tempArray = digraphNumberArray[x]
    cipherDigraphNumberArray.append(((np.dot(tempArray, keyMatrix)) % 26 + 97).tolist())
    

cipherDigraph = []
for x in range(len(digraphNumberArray)):
    for y in range(3):
        cipherDigraph.append(chr((cipherDigraphNumberArray[x][y])))

cipherText = ""
cipherText = cipherText.join(cipherDigraph)

print(cipherText)



    