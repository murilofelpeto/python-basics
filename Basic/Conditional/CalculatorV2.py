num1 = float(input("Enter first value: "))
operator = input("Enter operator")
num2 = float(input("Enter second number: "))

if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    print (num1 / num2)
else:
    print ("ERROR! OPERATOR NOT RECOGNIZED.\nTRY (+,-,*,/)")