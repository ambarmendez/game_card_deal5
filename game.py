from random import randint
import csv


class Deck:
    def __init__(self):
        self.all_cards = []
        for court in ['heart', 'spade', 'diamond', 'club']:
            for value in range(1,13):
                self.all_cards.append(Card(court, value))

    def shuffle(self):
        shuffle_cards = []

        while len(self.all_cards):
            random_position = randint(0, len(self.all_cards)-1)
            random_card = self.all_cards.pop(random_position)

            shuffle_cards.append(random_card)

        self.all_cards = shuffle_cards

    def deal(self, n_cards):
        cards = []

        for _ in range(n_cards):
            cards.append(self.all_cards.pop())

        return cards


class Hand:
    def __init__(self, cards):
        self.given_cards = cards

    def points_value(self):
        tot = 0
        for card in self.given_cards:
            #print(card)
            tot = tot + card.value

        return tot

    def printing(self):
        for card in self.given_cards:
            print(card.name, card.court)


class Card:
    def __init__(self, court, value):
        self.court = court
        self.value = value
        self.name = str(value)

        if value == 1:
            self.name = 'A'
        elif value == 10:
            self.name = 'Jack'
        elif value == 11:
            self.name = 'Queen'
        elif value == 12:
            self.name = 'King'

    def __repr__(self):
        return f'Card({self.court},{self.value})'


def get_previous_hand():
    cards = []
    with open('previous_points.csv', newline='') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            cards.append(Card(row[1], int(row[0])))

    return cards


def save_hand(cards):
    with open('previous_points.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for card in cards:
            writer.writerow([card.value,card.court])


def print_menu():
    menu_options = {
        1: 'Create New Deck',
        2: 'Shuffle Deck',
        3: 'Deal New Hand',
        4: 'Display Hand Total Points',
        5: 'Exit',
    }

    print('Menu options:')
    for key in menu_options.keys():
        print(key, ':', menu_options[key])


def option_selection():
    option = input('Enter your choice: ')
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        pass
    elif option == '5':
        pass
    else:
        print('Invalid option. Please enter a number between 1 and 5.')
        return

    return int(option)


deck = Deck()
hand = Hand(get_previous_hand())

while True:
    print_menu()
    option = option_selection()

    if option == 1:
        deck = Deck()
    elif option == 2:
        deck.shuffle()
    elif option == 3:
        hand = Hand(deck.deal(5))
    elif option == 4:
        hand.printing()
        print('Total points:' , hand.points_value())
    elif option == 5:
        save_hand(hand.given_cards)
        exit()
