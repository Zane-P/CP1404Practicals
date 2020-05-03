
from prac_06.guitar import Guitar

print("My guitars!")

guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print("{} added.".format(guitars[-1]))
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    print("Guitar {}: {:>{}} ({}), worth ${:10,.2f}{}".format(i, guitar.name, len(guitar.name), guitar.year,
                                                              guitar.cost,
                                                              " (vintage)" if guitar.is_vintage() == True else ""))
