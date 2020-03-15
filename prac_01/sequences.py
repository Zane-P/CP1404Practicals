"""
A program to show 3 different sequences from x to y
"""

while True:
    varX, varY = input("Enter x and y values (x, y): ").split(', ')
    try:
        varX, varY = (int(varX), int(varY))
    except ValueError:
        print("Please enter whole numbers only.")
    else:
        if varX > varY:
            print("x should be less than y.")
        else:
            break

print("Your values are: x = %i, y = %i" % (varX, varY))

while True:
    print("\nPlease select an option: ",
          "\n1. Show even numbers from %i to %i" % (varX, varY),
          "\n2. Show the odd numbers from %i to %i" % (varX, varY),
          "\n3. Show the squares from %i to %i" % (varX, varY),
          "\n4. Exit the program")
    option = int(input("\n>>>"))
    if 1 > option or option > 4:
        print("Please select an option from 1 to 4.")
    elif option == 1:
        print("The even numbers from %i to %i are:" % (varX, varY))
        for i in range(varX+(varX % 2), varY+1, 2):
            print(i)
    elif option == 2:
        print("The odd numbers from %i to %i are:" % (varX, varY))
        for i in range(varX+(1-(varX % 2)), varY+1, 2):
            print(i)
    elif option == 3:
        print("The squares of numbers from %i to %i are:" % (varX, varY))
        for i in range(varX, varY+1):
            print(i*i)
    elif option == 4:
        print("Thank you, come again.")
        break
