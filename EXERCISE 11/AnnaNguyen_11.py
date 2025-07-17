import random

class Deck():
    def __init__(self, size):
        ranks = ['2','3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.card_temp_list = [i for i in range(size)]
        self.card_list = []
        for i in range(len(self.card_temp_list)):
            d = self.card_temp_list[i]
            r = d % 13
            s = d // 13
            self.card_list.append(f"{ranks[r]} of {suits[s]}")
                       
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling...!!!")
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

    def display_hand(self):
        print("\nYour hand:")
        for i, card in enumerate(self.cards_in_play_list, start=1):
            print(f"{i}: {card}")


    def replace_card(self, replace_indexes):
        for i in replace_indexes:
            if 0 <= i < 5:
                self.cards_in_play_list[i] = self.card_list.pop()
            

        
# Creating a deck of 52 cards and shuffling
my_deck = Deck(52)
# Getting five cards
for i in range(5):
    my_deck.deal()
# Displaying cards in hand
my_deck.display_hand()

# Prompt user to choose cards to replace
replace_input = input("\nEnter the numbers of the cards to replace (e.g., 1 3 5), or press Enter to keep all: ")
replace_indexes = []

if replace_input.strip():
    try:
        if 1 > int(replace_input.strip()) or int(replace_input.strip()) > 5:
            print("Invalid input. No cards will be replaced.")
        replace_indexes = [int(x) - 1 for x in replace_input.split() if 1 <= int(x) <= 5]
        my_deck.replace_card(replace_indexes)
        my_deck.display_hand()
        print("\nThis is your final hand.")
    except ValueError:
        print("Invalid input. No cards will be replaced.")
        replace_indexes = []
            


