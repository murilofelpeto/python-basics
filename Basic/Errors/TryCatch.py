try:
    number = int(raw_input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero: " + str(err))
except ValueError as err:
    print("Invalid input: " + str(err))