def raiseToPower(baseNumber, powerNumber):
    result = 1
    for i in range(powerNumber):
        result = result * baseNumber
    return result

print(raiseToPower(2, 2))