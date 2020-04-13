from player import Player
from deck import Deck


class Game:
    def __init__(self, p1='Lars', p2='Nils'):
        self.deck = Deck()
        self.players = [Player(p1, self.deck), Player(p2, self.deck)]

    def play(self):
        for player in self.players:
            print(player)

        winner = False
        while not winner:
            plays = [player.play() for player in self.players]
            for i, player in enumerate(self.players):
                print(f"{player.name} play a {plays[i]} ")

            if plays[0] > plays[1]:
                print(f"{self.players[0].name} wins the round!")
                self.players[0].add_won_card(plays[0])
            elif plays[0] < plays[1]:
                print(f"{self.players[0].name} wins the round!")
                self.players[0].add_won_card(plays[0])
            else:
                # TODO: A draw could result in the next winner gets to choose either card from
                # TODO: from the draw pile
                print('It was a draw! Both cards are discarded.')

            if len(self.deck.cards) > 1:
                for player in self.players:
                    player.draw(self.deck)

            for player in self.players:
                if player.winner():
                    print(f"{player.name} won these cards:")
                    print(f"{player.wins()}")
                    print(f"The winner is {player.name}")
                    winner = True

            if not winner and len(self.deck.cards) == 0 and len(self.players[0].hand) == 0:
                winner = True
                print(f"There is no winner. What even is the purpose?")
