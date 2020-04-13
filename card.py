class Card:
    def __init__(self, element, colour, value):
        self._element = element
        self._colour = colour
        self._value = value

    def __str__(self):
        return f"{self._colour:6} {self._value:3} of {self._element}"

    def __gt__(self, other):
        if self._element == other.element():
            return self._value > other.value()
        elements = {'FIRE': 'ICE', 'ICE': 'WATER', 'WATER': 'FIRE'}  # key beats value
        for element in elements:
            if self._element == element and other.element() == elements.get(element):
                return True
            else:
                return False

    def value(self):
        return self._value

    def colour(self):
        return self._colour

    def element(self):
        return self._element
