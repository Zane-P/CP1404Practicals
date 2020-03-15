age = 0
passed = 0

while passed == 0:
    try:
        age = int(input("What is your age? "))
        while age < 0:
            print("Please enter a non-negative age.")
            age = int(input("What is your age? "))
        passed = 1
    except ValueError:
        print("Please enter an integer age.")

if age % 2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")