from player import Player
from deck import Deck


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
