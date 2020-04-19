
from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("New Guitar", 2019, 4999.99)

print("{} get_age() - Expected 98. Got {}".format(guitar1.name, guitar1.get_age()))
print("{} get_age() - Expected 1. Got {}".format(guitar2.name, guitar2.get_age()))
print("{} get_age() - Expected True. Got {}".format(guitar1.name, guitar1.is_vintage()))
print("{} get_age() - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))
