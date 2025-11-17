# -------------------------------------------
# Assuming Section 11.5 Card and Deck classes:
# -------------------------------------------

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in Deck.suits
                      for rank in Deck.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


# ------------------------------------------------
# FUNCTIONS FOR THE POKER GAME
# ------------------------------------------------

def deal_hand(deck, n=5):
    """Deals n cards and returns them as a list."""
    return [deck.deal() for _ in range(n)]


def display_hand(hand):
    """Prints the hand with numbered positions."""
    print("\nYour hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}. {card}")


def replace_cards(deck, hand, replace_list):
    """Replaces selected cards in the hand with new ones."""
    for index in replace_list:
        hand[index - 1] = deck.deal()
    return hand


# ------------------------------------------------
# MAIN GAME LOGIC
# ------------------------------------------------

def main():
    deck = Deck()
    deck.shuffle()

    # Deal first hand
    hand = deal_hand(deck)
    display_hand(hand)

    # Ask user which cards to replace
    user_input = input(
        "\nEnter card numbers to replace (e.g. 1, 3, 5) or press Enter to keep all: "
    ).strip()

    if user_input:
        replace_list = [int(num) for num in user_input.split(",")]
        hand = replace_cards(deck, hand, replace_list)

    # Show final hand
    print("\nAfter the draw:")
    display_hand(hand)


# Run the program
if __name__ == "__main__":
    main()
