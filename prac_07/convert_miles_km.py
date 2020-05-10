from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.609344


class ConvertMilesKm(App):
    km_output = StringProperty()

    def build(self):
        Window.size = (600, 250)
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self, text):
        miles = self.convert_input_to_number(text)
        self.km_output = "{:.3f}".format(miles * MILES_TO_KM)

    def handle_increment(self, text, increment):
        if text == '':
            text = 0.0
        incremented_miles = self.convert_input_to_number(text) + increment
        self.root.ids.miles_input.text = str(incremented_miles)

    @staticmethod
    def convert_input_to_number(text):
        try:
            number = float(text)
            return number
        except ValueError:
            return 0.0


ConvertMilesKm().run()
