from collections import Counter


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
            colours = Counter()
            for card in self.won_cards:
                colours[str(card.element()+card.colour())] += 1
            elements = {card.element() for card in self.won_cards}
            if 3 in colours.values():
                # Win if you have 3 colours from one element.
                return True
            if len(elements) > 2:
                # Win of you have collected all 3 elements.
                return True
        return False

    def __str__(self):
        return '\n'.join([self.name] + [str(card) for card in self.hand])
