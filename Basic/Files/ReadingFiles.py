#MODE: r = read / w = overwrite a file /  a = append (modify and add new information) / r+ = read-write


with open("employees.txt", "r") as employeeFile:
    for line in employeeFile.readlines():
        print(line)
    # print(employeeFile.read())
employeeFile.close()

#Append new file

with open("employees1.txt", "w") as employeeFile:
    employeeFile.write("\nKelly - Customer Service")
employeeFile.close()

#Append
with open("employees.txt", "a") as employeeFile:
    employeeFile.write("\nKelly - Customer Service")
employeeFile.close()