def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2 , num1 % num2)

def egcd(num1, num2):
    x, prevX = 0, 1
    y, prevY = 1, 0
    while num2 is not 0:
        q = num1 // num2
        num1, num2 = num2, num1 % num2
        x, prevX = prevX - q * x, x
        y, prevY = prevY - q * y, y

    return prevY

num1 = int(input("Enter number you want to find an inverse of: "))
num2 = int(input("Enter the field size: "))

if(gcd(num2, num1) == 1): #inverse exists
    print(egcd(num2, num1))
else:
    print("This number does not have an inverse in this field")
