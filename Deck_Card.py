import random

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def show(self):
        print("{} of {} ".format(self.value, self.suite))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #Loop through card array suit
        for cardsuite in ["Clubs", "Hearts", "Diamonds", "Spades"]:
            #for each card suit create 13 cards
            for val in range(1, 14):
                #take the result and append it to the cards list
                self.cards.append(Card(cardsuite,val))

    def show(self):
        #Show every single card in the array
        for c in self.cards:
            c.show()

    def shuffle(self):
        #Decrement the cards starting from the last element going to 0 with a step of -1
        for i in range(len(self.cards)-1, 0, -1):
            #generate a random number between 0 and the max len of the array(keep decrementing)
            r = random.randint(0, i)
            #swap the cards positions
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        #Take the last card in the deck and return it to what ever method is gonna call the draw Method
        return self.cards.pop()



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        #return slef so we can chain this method when we call it
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard_card(self):
        return self.hand.pop()



# #card = Card("Clubs", 6)
# #card.show()
#
deck = Deck()
deck.shuffle()
#deck.show()

# #card = deck.draw_card()
# #card.show()

player = Player("Hamza")
player.draw(deck).draw(deck).draw(deck).draw(deck)
player.show_hand()



