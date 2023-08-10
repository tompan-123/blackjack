import unittest
import blackjack as bj


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = bj.Deck()

    def test_deck(self):
        self.assertEqual(self.deck.cards.count("A"), 4)
        self.assertEqual(self.deck.cards.count("J"), 4)
        self.assertEqual(self.deck.cards.count("Q"), 4)
        self.assertEqual(self.deck.cards.count("K"), 4)
        self.assertEqual(self.deck.cards.count("2"), 4)
        self.assertEqual(self.deck.cards.count("3"), 4)
        self.assertEqual(self.deck.cards.count("4"), 4)
        self.assertEqual(self.deck.cards.count("5"), 4)
        self.assertEqual(self.deck.cards.count("6"), 4)
        self.assertEqual(self.deck.cards.count("7"), 4)
        self.assertEqual(self.deck.cards.count("8"), 4)
        self.assertEqual(self.deck.cards.count("9"), 4)
        self.assertEqual(self.deck.cards.count("10"), 4)

    def test_draw_single(self):

        card = self.deck.draw_card()
        self.assertTrue(
            card in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"}
        )
        self.assertEqual(len(self.deck.cards), 51)

    def test_draw_all(self):

        drawn_cards = []
        for i in range(52):
            drawn_cards.append(self.deck.draw_card())

        self.assertEqual(drawn_cards.count("A"), 4)
        self.assertEqual(drawn_cards.count("J"), 4)
        self.assertEqual(drawn_cards.count("Q"), 4)
        self.assertEqual(drawn_cards.count("K"), 4)
        self.assertEqual(drawn_cards.count("2"), 4)
        self.assertEqual(drawn_cards.count("3"), 4)
        self.assertEqual(drawn_cards.count("4"), 4)
        self.assertEqual(drawn_cards.count("5"), 4)
        self.assertEqual(drawn_cards.count("6"), 4)
        self.assertEqual(drawn_cards.count("7"), 4)
        self.assertEqual(drawn_cards.count("8"), 4)
        self.assertEqual(drawn_cards.count("9"), 4)
        self.assertEqual(drawn_cards.count("10"), 4)
        self.assertEqual(len(self.deck.cards), 0)
        with self.assertRaises(Exception):
            self.deck.draw_card()


class CalcScoreTest(unittest.TestCase):
    def test_score_no_face_or_ace(self):
        hand = ["1", "5", "8"]
        self.assertEqual(bj.calc_score(hand), 14)

    def test_score_face_cards(self):
        hand = ["J", "Q", "5"]
        self.assertEqual(bj.calc_score(hand), 25)

    def test_score_only_ace(self):
        hand = ["A", "A"]
        self.assertEqual(bj.calc_score(hand), 12)

    def test_ace_is_11_with_other_cards(self):
        hand = ["5", "3", "A"]
        self.assertEqual(bj.calc_score(hand), 19)

    def test_multiple_ace_is_1_with_other_cards(self):
        hand = ["9", "9", "A", "A", "A"]
        self.assertEqual(bj.calc_score(hand), 21)

    def test_instant_blackjack(self):
        hand = ["K", "A"]
        self.assertEqual(bj.calc_score(hand), 21)


if __name__ == "__main__":
    unittest.main()
