# __Deck of Cards__
## **Create a Deck of cards and hand Player:**
* The project consist in creating a deck of cards and the widraw system. The project has been built on the idea of Object oriented programming and class separation of concern. The project work around, mainly, the deck structure. I created a Deck class and `__init__` with 2 parameters, suites and value. In this class I created a function(Method) show, whick allow to print the deck cards.
* The second step, its to build a real deck. a `__init__` make sure the class start initialized with a card list array `self.cards = []` and a `self.build()`. The build() attribute will loop trough 4 figures `(Clubs, Hearts, Diamonds, Spades)` and for each of those, will create 13 cards. A `Show()` Method will assure that we can display all the cards. A `Shuffle()` Method has been created to shuffle the card orders, so they wont display always following a specific pattern.
````
    def shuffle(self):
        #Decrement the cards starting from the last element going to 0 with a step of -1
        for i in range(len(self.cards)-1, 0, -1):
            #generate a random number between 0 and the max len of the array(keep decrementing)
            r = random.randint(0, i)
            #swap the cards positions
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
````

draw_card
````
    def draw_card(self):
        #Take the last card in the deck and return it to what ever method is gonna call the draw Method
        return self.cards.pop()
````
* The last and Final Step os creating the player and the player Hand.
The class has been `__init__` with a `self.name = name` and `self.hand = []` making sure to have a full hand of card and a player name to begin with. The `draw()` will call and fire the `deck.draw_card()` Method from the Deck class and append the content  to the hand empty list. The show had will target and loop through the `self.hand` and show all the cards passed from the previous method. And the last function `Discard_card` will get the last card in the hand and discard it
## **Blockers, Problems, Bugs, Solutions:**
* __Blockers:__ I had some concept design when I had to build the shuffle function, finding hard to find a simple idea to build it and shiffle the deck in a way that wont have so often 2 similar suits next to each other
* __Problems:__ N/A
* __Bugs:__ Shuffle System
* __Solutions:__
    * __Problems:__N/A
    * __Bugs:__N.A


## **Outcomes:**
Its been a nice challenge to build this idea. I learned how to work with OOP and try to dont repeat my code to get to the semplest solution.