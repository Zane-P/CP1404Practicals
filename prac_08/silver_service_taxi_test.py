from prac_08.silver_service_taxi import SilverServiceTaxi

new_fancy_taxi = SilverServiceTaxi('Fancy Car', 100, 2)

print(new_fancy_taxi.__str__())
print(new_fancy_taxi.get_fare())
new_fancy_taxi.drive(18)
print(new_fancy_taxi.__str__())
print(new_fancy_taxi.get_fare())
new_fancy_taxi.start_fare()
new_fancy_taxi.drive(32)
print(new_fancy_taxi.__str__())
print(new_fancy_taxi.get_fare())
new_fancy_taxi.drive(100)
print(new_fancy_taxi.__str__())
print(new_fancy_taxi.get_fare())
