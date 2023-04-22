import random

cards = [
    ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
    ('J', 10), ('Q', 10), ('K', 10), ('A', 11)
]

class Deck:
    def __init__(self):
        self.cards = cards * 4
        random.shuffle(self.cards)
        self.index = 0

    def draw(self):
        card = self.cards[self.index]
        self.index += 1
        return card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card[1]

        if self.value > 21 and ('A', 11) in self.cards:
            self.value -= 10
            self.cards[self.cards.index(('A', 11))] = ('A', 1)

    def display(self):
        return ', '.join(card[0] for card in self.cards) + f' ({self.value})'

    def is_bust(self):
        return self.value > 21

deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

player_hand.add_card(deck.draw())
dealer_hand.add_card(deck.draw())
player_hand.add_card(deck.draw())
dealer_hand.add_card(deck.draw())

while True:
    print(f"Дилер: {dealer_hand.cards[0][0]}, *")
    print(f"Игрок: {player_hand.display()}")

    if player_hand.is_bust():
        print("У вас перебор!")
        break

    choice = input("Хотите взять еще карту? (Д/н): ")
    if choice.lower() == 'д':
        player_hand.add_card(deck.draw())
    else:
        break

while dealer_hand.value < 17:
    dealer_hand.add_card(deck.draw())

print(f"Дилер: {dealer_hand.display()}")
print(f"Игрок: {player_hand.display()}")

if dealer_hand.is_bust() or (player_hand.value > dealer_hand.value and not player_hand.is_bust()):
    print("Вы выиграли!")
elif player_hand.value == dealer_hand.value:
    print("Ничья.")
else:
    print("Вы проиграли.")
