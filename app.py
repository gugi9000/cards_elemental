import random


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


class Deck:
    def __init__(self):
        colours = ['blue', 'red', 'green', 'yellow']
        values = list(range(1, 11))
        elements = ['FIRE', 'SNOW', 'WATER']
        self.cards = [Card(element, colour, value) for value in values for element in elements for colour in colours]

    def __str__(self):
        all_cards = [f"{card}" for card in self.cards]
        return '\n'.join(all_cards)

    def num_cards(self):
        return len(self.cards)

    def draw(self):
        choice = random.choice(list(range(self.num_cards())))
        chosen_card = self.cards.pop(choice)
        return chosen_card


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]
        self.won_cards = []

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


game_deck = Deck()
player1 = Player('Lars', game_deck)
player2 = Player('Nils', game_deck)
players = [player1, player2]

for player in players:
    print(player)

winner = False
while not winner:
    plays = [player.play() for player in players]
    for i, player in enumerate(players):
        print(f"{player.name} play a {plays[i]} ")

    if plays[0] > plays[1]:
        print(f"{players[0].name} wins the round!")
        players[0].add_won_card(plays[0])
    else:
        print(f"{players[1].name} wins the round!")
        players[1].add_won_card(plays[1])
    if len(game_deck.cards) > 1:
        for player in players:
            player.draw(game_deck)

    for player in players:
        if player.winner():
            print(f"{player.name} won these cards:")
            print(f"{player.wins()}")
            print(f"The winner is {player.name}")
            winner = True

    if not winner and len(game_deck.cards) == 0 and len(player1.hand) == 0:
        winner = True
        print(f"There is no winner. What even is the purpose?")
