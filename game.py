from player import Player
from deck import Deck
from random import shuffle as shuffle_list


class Game:
    def __init__(self, p1='Lars', p2='Nils'):
        self.deck = Deck()
        self.players = [Player(p1, self.deck), Player(p2, self.deck)]

    @staticmethod
    def swap_list(player_list):
        return [player_list[1], player_list[0]]

    @staticmethod
    def choose(choices):
        while True:
            for i, choice in enumerate(choices):
                print(f"{i:3}: {choice}")
            choice = input("Which card do you want to play? ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(len(choices)):
                    return choice
            else:
                print("Invalid choice.")

    def play(self):
        shuffle_list(self.players)

        print('Playing order has been chosen:')
        for i, player in enumerate(self.players, start=1):
            print(f"Player {i} will be {player.name}.")

        winner = False
        while not winner:

            plays = list() # [player.play(0) for player in self.players]
            for player in self.players:
                print(f"{player.name}, it's your turn.")
                if len(player.won_cards)>0:
                    print("You have these cards in your stash:")
                    for card in player.won_cards:
                        print(card)
                print("You have these cards on your hand:")
                plays.append(player.play(self.choose(player.hand)))

            for i, player in enumerate(self.players):
                print(f"{player.name} plays a {plays[i]} ")

            if plays[0] > plays[1]:
                print(f"{self.players[0].name} wins the round!")
                self.players[0].add_won_card(plays[0])
            elif plays[0] < plays[1]:
                print(f"{self.players[1].name} wins the round!")
                self.players[1].add_won_card(plays[1])
                self.players = self.swap_list(self.players)
            else:
                # TODO: A draw could result in the next winner gets to
                # TODO: choose either card from the draw pile
                print('It was a draw! Both cards are discarded.')

            for player in self.players:
                if player.winner():
                    print(f"{player.name} won these cards:")
                    print(f"{player.wins()}")
                    print(f"The winner is {player.name}")
                    winner = True

            if not winner and len(self.deck.cards) == 0 and len(self.players[0].hand) == 0:
                winner = True
                print(f"There is no winner. What even is the purpose?")

            if len(self.deck.cards) > 1:
                for player in self.players:
                    player.draw(self.deck)
