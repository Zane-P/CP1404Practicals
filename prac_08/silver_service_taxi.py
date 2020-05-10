from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km*fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        return super().get_fare() + self.flag_fall

    def start_fare(self):
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        return distance_driven
