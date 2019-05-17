isMale = True
isTall = True

if isMale and isTall:
    print("You are male and tall")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("You are not male but are tall")
else:
    print("You are not male and not tall")

def maxNum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(maxNum(300,40,5))