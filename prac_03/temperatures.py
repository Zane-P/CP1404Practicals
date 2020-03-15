

def main():

    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()

    def celsius_to_fahrenheit(celsius):
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit

    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    while choice != "Q":
        if choice == "C":
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(float(input("Celsius: ")))))
        elif choice == "F":
            print("Result: {:.2f} C".format(fahrenheit_to_celsius(float(input("Fahrenheit: ")))))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()

    print("Thank you.")


main()

