from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
total_bill = 0

print("Let's drive!")
menu_choice = input("q)uit, c)hoose taxi, d)rive \n>>> ").lower()
while menu_choice != 'q':
    if menu_choice == 'c':
        print("Taxis Available: ")
        [print(i, ' - ', taxi) for i, taxi in enumerate(taxis)]
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    if menu_choice == 'd' and current_taxi is not None:
        distance = float(input("Drive how far? "))
        current_taxi.drive(distance)
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
        total_bill += current_taxi.get_fare()
    print("Bill to date: ${:.2f}".format(total_bill))
    menu_choice = input("q)uit, c)hoose taxi, d)rive \n>>> ").lower()
