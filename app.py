from game import Game


def main():
    print("Welcome to Cards Elemental!")
    print("We need two players.")
    p1 = input("Name a player: ").strip()
    p2 = input("and another one: ").strip()

    game = Game(p1, p2)
    game.play()


if __name__ == '__main__':
    main()
