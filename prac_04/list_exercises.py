
# 1
numbers = []

for i in range(5):
    numbers.append(int(input("Number: ")))

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers)/len(numbers))

# 2
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = str(input("Enter your username: "))
access = False

for username in usernames:
    if name == username:
        access = True

if access is True:
    print("Access Granted.")
else:
    print("YOU SHALL NOT PASS!")