from card import Card
from random import choice as random_choice


class Deck:
    def __init__(self):
        colours = ['blue', 'red', 'green', 'yellow']
        values = list(range(1, 11))
        elements = ['FIRE', 'ICE', 'WATER']
        self.cards = [Card(element, colour, value) for value in values for element in elements for colour in colours]

    def __str__(self):
        all_cards = [f"{card}" for card in self.cards]
        return '\n'.join(all_cards)

    def num_cards(self):
        return len(self.cards)

    def draw(self):
        choice = random_choice(list(range(self.num_cards())))
        chosen_card = self.cards.pop(choice)
        return chosen_card
