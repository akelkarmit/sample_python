"""this is a full fledged blackjack program that can be
run in codeskulptor.org a browser based python interpretter
go to www.codeskulptor.org, enter this code and press run
and play blackjack"

# Mini-project #6 - Blackjack

import simplegui
import random


# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    



# initialize some useful global variables
in_play = False
outcome = ""
score = 0



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        self.ans = ''
        
        for Card in self.cards:
            self.ans = self.ans + " " + str(Card.__str__())
        
        return "Hand contains" + self.ans
                                      
    def add_card(self, card):
        self.card = card
        self.cards.append(card)

    
    def get_value(self):
        hand_value = 0
        
        for card in self.cards:
            hand_value = hand_value + VALUES[card.get_rank()]
        
        for card in self.cards:
            if card.get_rank() != 'A':
                return hand_value
            else:
                
                if hand_value + 10 <= 21:
                    hand_value = hand_value + 10
                    return hand_value
                else:
                    return hand_value
    
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,[pos[0]+100*self.cards.index(card),pos[1]])
            #pos[0] = pos[0] + 100*self.cards.index(card)
            
        # draw a hand on the canvas, use the draw method for cards
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.card = Card(suit, rank)# **deck becomes a list of Card types not srtings
                self.deck.append(self.card)
                random.shuffle(self.deck)
    
    def __str__(self):
        self.ans = ''
        
        for Card in self.deck:
            self.ans = self.ans + " " + str(Card.__str__())
        
        return "Deck contains" + self.ans
    
    
    def deal_card(self):
        return self.deck.pop() 

    def shuffle(self):
        return random.shuffle(self.deck)

    


#define event handlers for buttons
def deal():
    global game_deck, player_hand, dealer_hand, in_play,outcome, score
    
    if in_play == True:
    # Hitting the "Deal" button while hand is in play results in decrementing
    # the score.
        score -= 1 
       
    in_play = True
    game_deck.shuffle()
    # how to reset the player_hand and dealer_hand here
    player_hand = Hand()
    dealer_hand = Hand()

    
    
    for i in range (2):
        player_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
    outcome = "Hit or Stand?"
    print "Player ", player_hand.__str__()
    print "Dealer ", dealer_hand.__str__()
    


    

def hit():
    global player_hand, in_play, score, outcome
    if player_hand.get_value() <= 21:
        player_hand.add_card(game_deck.deal_card())
        print "Player ", player_hand.__str__()
        outcome = "Hit or Stand?"
        if player_hand.get_value() > 21:
            print "Mr. Player you have busted - you got greedy"
            in_play = False
            score = score - 1
            outcome = "Player Busted - New Deal?"
            
    else:
        in_play = False
        score = score - 1
        print "You have busted"
        outcome = "Player Busted - New Deal?"
    
    #if in_play == False:
    #    deal()
    
    
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, dealer_hand, player_hand, score, outcome
    
    in_play = False
    #    print  "Dear Player you have busted"
    #else:
    while (dealer_hand.get_value() <= 17):
        dealer_hand.add_card(game_deck.deal_card())
        dealer_hand.get_value()
        print "Dealer ", dealer_hand.__str__()
    if dealer_hand.get_value() > 21:
        print " Player you win"
        outcome = "Player you win - New Deal?"
        score = score + 1
        #in_play = False
    else:
        if dealer_hand.get_value() >= player_hand.get_value():
            print " Dealer has won"
            outcome = "Dealer wins - New Deal?"
            score = score - 1
            #in_play = False
        else:
            print " Player has won"
            outcome = "Player you win - New Deal?"
            #in_play = False
    
    #if in_play == False:
    #    deal()
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global outcome, score
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    
    dealer_hand.draw(canvas,[100,200])
    player_hand.draw(canvas,[100,400])
    
    canvas.draw_text("Blackjack", (250, 45), 35, 'Black','serif')
    canvas.draw_text("Player", (100, 550), 25, 'Black','serif')
    canvas.draw_text("Dealer", (100, 350), 25, 'Black','serif')
    
    canvas.draw_text(outcome, (300, 550), 25, 'Black','serif')
    canvas.draw_text("Score", (500, 65), 25, 'Black','serif')
    canvas.draw_text(str(score), (520, 90), 25, 'Black','serif')

    if in_play == True:
        canvas.draw_image(card_back, (35.5,48),(71, 96),(100+35.5,200+49),(71,96))

            
    
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
game_deck = Deck()
#player_hand = Hand()
#dealer_hand = Hand()

deal()
frame.start()


# remember to review the gradic rubric