# from collections import Counter


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]
        self.won_cards = list()  # Counter()

    def add_won_card(self, card):
        self.won_cards.append(card)

    def draw(self, deck):
        self.hand.append(deck.draw())

    def wins(self):
        return '\n'.join([str(card) for card in self.won_cards])

    def play(self):
        return self.hand.pop()

    def winner(self):
        if len(self.won_cards) > 0:
            colours = {card.colour() for card in self.won_cards}
            elements = {card.element() for card in self.won_cards}
            if len(colours) > 2 or len(elements) > 2:
                return True
        return False

    def __str__(self):
        return '\n'.join([self.name] + [str(card) for card in self.hand])
