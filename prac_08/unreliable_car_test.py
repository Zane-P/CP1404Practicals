from prac_08.unreliable_car import UnreliableCar

new_car = UnreliableCar('Lemon', 100, 50)

while new_car.fuel > 0:
    print('{} || {}'.format(new_car.drive(30), new_car.fuel))
