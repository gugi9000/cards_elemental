import unittest
import deck


class TestDeck(unittest.TestCase):
    def test_init(self):
        my_deck = deck.Deck()
        self.assertEqual(len(my_deck.cards), 120)
        self.assertEqual(my_deck.num_cards(), 120)

    def test_draw(self):
        my_deck = deck.Deck()
        self.assertEqual(my_deck.num_cards(), 120)
        for x in range(my_deck.num_cards()):
            _ = my_deck.draw()
        self.assertEqual(my_deck.num_cards(), 0)


if __name__ == '__main__':
    unittest.main()
