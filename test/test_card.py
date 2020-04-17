import unittest
import card


class TestCard(unittest.TestCase):
    def test_combat(self):
        card_fire_10 = card.Card('FIRE', 'blue', 10)
        card_fire_1 = card.Card('FIRE', 'blue', 1)
        card_ice_10 = card.Card('ICE', 'blue', 10)
        card_ice_1 = card.Card('ICE', 'blue', 1)
        card_water_10 = card.Card('WATER', 'blue', 10)
        card_water_1 = card.Card('WATER', 'blue', 1)

        self.assertGreater(card_fire_10, card_fire_1)
        self.assertGreater(card_ice_10, card_ice_1)
        self.assertGreater(card_water_10, card_water_1)

        self.assertLess(card_fire_1, card_fire_10)
        self.assertLess(card_ice_1, card_ice_10)
        self.assertLess(card_water_1, card_water_10)

        self.assertGreater(card_fire_1, card_ice_10)
        self.assertGreater(card_ice_1, card_water_10)
        self.assertGreater(card_water_1, card_fire_10)

        self.assertLess(card_fire_10, card_water_1)
        self.assertLess(card_ice_1, card_fire_1)
        self.assertLess(card_water_1, card_ice_1)


if __name__ == '__main__':
    unittest.main()
