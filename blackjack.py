import random
import sys

class Deck:
    def __init__(self):
        self.cards = []

        # Load deck with numbered cards
        for i in range(2, 11):
            self.cards.extend([str(i)] * 4)

        # Load deck with lettered cards
        for rank in ["A", "J", "Q", "K"]:
            self.cards.extend([rank] * 4)

    def draw_card(self):
        deck_size = len(self.cards)

        if deck_size == 0:
            raise Exception("Deck is empty")

        card = self.cards.pop(random.randrange(deck_size))

        return card


def calc_score(hand):
    score = 0
    ace_counter = 0
    for card in hand:
        if card == "A":
            ace_counter += 1
        elif card in ["J", "Q", "K"]:
            score += 10
        else:
            score += int(card)

    # Score the Aces
    for i in range(ace_counter, 0, -1):
        if i == 1 and score <= 10:
            score += 11
        else:
            score += 1

    return score


def play_blackjack():
    dealer = []
    player = []

    deck = Deck()

    # Start game by dealing 2 cards to dealer and player
    dealer.append(deck.draw_card())
    dealer.append(deck.draw_card())

    player.append(deck.draw_card())
    player.append(deck.draw_card())

    # Player plays
    while True:
        player_score = calc_score(player)
        print("Dealer has: " + dealer[0] + " ? = ?")
        print("Player has: " + " ".join(player) + " = " + str(player_score))

        if player_score > 21:
            print("Player busts with " + str(player_score))
            print("Dealer wins")
            sys.exit()
        elif player_score == 21:
            print("Player wins!")
            print("Blackjack!")
            sys.exit()
        else:
            inp = input("Would you like to (H)it or (S)tand? ")
            while inp not in ["H", "S"]:
                inp = input("Invalid input. Please type H to hit or S to stand. ")

            if inp == "H":
                card = deck.draw_card()
                print()
                print("Player hits and draws " + card + "\n")
                player.append(card)
            else:
                print()
                print(
                    "Player stands with: "
                    + " ".join(player)
                    + " = "
                    + str(player_score)
                    + "\n"
                )
                break

    # Dealer plays
    while True:
        dealer_score = calc_score(dealer)
        print("Dealer has: " + " ".join(dealer) + " = " + str(dealer_score))

        if dealer_score < 17:
            card = deck.draw_card()
            dealer.append(card)
            print()
            print("Dealer hits and draws " + card + "\n")
        elif dealer_score == 21:
            print("Dealer wins with a Blackjack :(")
            sys.exit()
        elif dealer_score > 21:
            print("Dealer busts with " + str(dealer_score))
            print("Player wins!")
            sys.exit()
        else:
            print("Dealer stands \n")
            break

    # Evaluate and display game result
    if player_score > dealer_score:
        print("Player wins!")
        print(
            " ".join(player)
            + " = "
            + str(player_score)
            + " to Dealer's "
            + " ".join(dealer)
            + " = "
            + str(dealer_score)
        )
    elif player_score < dealer_score:
        print("Dealer wins :(")
        print(
            " ".join(dealer)
            + " = "
            + str(dealer_score)
            + " to Player's "
            + " ".join(player)
            + " = "
            + str(player_score)
        )
    else:
        print("It's a tie")
        print(
            "Player's "
            + " ".join(player)
            + " = "
            + str(player_score)
            + " to Dealer's "
            + " ".join(dealer)
            + " = "
            + str(dealer_score)
        )

if __name__ == "__main__":
    play_blackjack()

