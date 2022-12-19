import random


#  Create Deck
def CreateDeck():   # Cards 0-9, 10=SKIP, 11=Reverse, 12=+2, 13=Wild, 14=+4
    # 108 playing cards
    Deck = []
    for Card in ColorCard('Red'):
        Deck.append(Card)
    for Card in ColorCard('Blue'):
        Deck.append(Card)
    for Card in ColorCard('Green'):
        Deck.append(Card)
    for Card in ColorCard('Yellow'):
        Deck.append(Card)

    for x in range(0, 4):
        Card = ['Wild', 13]
        Deck.append(Card)
    for x in range(0, 4):
        Card = ['Wild', 14]
        Deck.append(Card)
    
    return Deck


def ColorCard(Color):
    Color_List = []
    
    for Number in range(0, 13):  # Cards 0-9, 10=SKIP, 11=Reverse, 12=+2
        Card = [Color, Number]
        Color_List.append(Card)
    for Number in range(1, 13):  # Cards 1-9, 10=SKIP, 11=Reverse, 12=+2
        Card = [Color, Number]
        Color_List.append(Card)

    return Color_List

# MAIN:

Shared_Deck = CreateDeck()
print(f"Shared Deck: {Shared_Deck}\n")

Player_Hand = []
AI_Hand = []

for card in range(0, 14):   # 7 cards per hand
    random_index = random.randint(0, len(Shared_Deck)-1)
    random_card = Shared_Deck.pop(random_index)
    if card % 2:
        Player_Hand.append(random_card)
    else:
        AI_Hand.append(random_card)

print(f"Player_Hand: {Player_Hand}\n")
print(f"AI_Hand: {AI_Hand}\n")

discard_pile = []
# get first card, randomly from deck
discard_pile.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
# if card is a wildcard, add the card back to deck, get new card
while discard_pile[-1][0] == 'Wild':
    Shared_Deck.append(discard_pile.pop())
    discard_pile.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
print(discard_pile)

#  Gameplay Setup
noWinner = True     # State
direction = True    # State
player = 1          # State
while(noWinner):
    if player == 1: # then it is the user, not AI
        hasCard = False     # State
        # Hand Test
        for card in Player_Hand:
            # Check Color
            if card[0] == discard_pile[-1][0]:
                hasCard = True
            elif card[0] == 'Wild':
                hasCard = True
                
            # Check Number
            if card[1] == discard_pile[-1][1]:
                hasCard = True
        
        # Force Draw
        if hasCard == False:
            forcedCard = Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1))
            Player_Hand.append(forcedCard)
            print(f"You were forced to draw: {forcedCard}\n")
        
        # Hand test
        if Player_Hand[-1][0] == discard_pile[-1][0]:
            hasCard = True
        elif Player_Hand[-1][0] == 'Wild':
            hasCard = True
        elif Player_Hand[-1][1] == discard_pile[-1][1]:
            hasCard = True
        
        print(f"Your Hand:\n{Player_Hand}\n")
        if hasCard:
            print("What card color do you want to play:?")
            IColor = input()
            print("What card number do you want to play:?")
            INumber = input()
            index = Player_Hand.index([IColor, INumber])
            CardToPlay = Player_Hand.pop(index)
            discard_pile.append(CardToPlay) #new topdeck
            
            # Resolve Effects
            if len(Player_Hand) == 0:
                noWinner = False
                print("Congratulations you have won!")
            
            elif CardToPlay[1] == 10:  #card is skip
                if direction:
                    player = player + 1
                else:
                    player = player - 1
            
            elif CardToPlay[1] == 11:  #card is reverse
                direction = not direction
            
            elif CardToPlay[1] == 12:  #card is +2
                # get the next players hand
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
            
            elif CardToPlay[1] == 13:  #card is Wildcard, set color
                CInput = input()
                WildCardReplacementIndex = Shared_Deck.index([CInput],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
                
            elif CardToPlay[1] == 14:  #card is +4, set color
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                
                CInput = input()
                WildCardReplacementIndex = Shared_Deck.index([CInput],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
                
        else:
            print("No card to play, going to next turn.")
    
    else:   # then it is the AI turn
        print(f"===AI Turn===\nHand: {AI_Hand}\n")
        hasColor = False    # State
        hasNumber = False   # State
        hasWild = False     # State
        
        # Card Test
        for card in AI_Hand:
            # Check Color
            if card[0] == discard_pile[-1][0]:
                hasColor = True
                break
            elif card[0] == 'Wild':
                hasWild = True
                break
                
            # Check Number
            if card[1] == discard_pile[-1][1]:
                hasNumber = True
                break
        
        if hasColor == False and hasNumber == False and hasWild == False:
            # Force Draw
            forcedCard = Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1))
            AI_Hand.append(forcedCard)
            print(f"AI forced to draw: {forcedCard}")
            if AI_Hand[-1][0] == discard_pile[-1][0]:
                hasColor = True
            elif AI_Hand[-1][0] == 'Wild':
                hasWild = True
            elif AI_Hand[-1][1] == discard_pile[-1][1]:
                hasCard = True
        
        playedCard = False  # State
        if hasColor:
            IColor = discard_pile[-1][0]
            INumber = any
            index = AI_Hand.index([IColor, INumber])
            CardToPlay = AI_Hand.pop(index)
            discard_pile.append(CardToPlay) #new topdeck
        
        elif hasNumber:
            IColor = any
            INumber = discard_pile[-1][1]
            index = AI_Hand.index([IColor, INumber])
            CardToPlay = AI_Hand.pop(index)
            discard_pile.append(CardToPlay) #new topdeck
        
        elif hasWild:
            IColor = 'Wild'
            INumber = any
            index = AI_Hand.index([IColor, INumber])
            CardToPlay = AI_Hand.pop(index)
            discard_pile.append(CardToPlay) #new topdeck
        
        if playedCard:
            # Resolve Effects
            # did they win
            if len(AI_Hand) == 0:
                noWinner = False
                print("\nThe AI has Won!")
            
            elif CardToPlay[1] == 10:  #card is skip
                if direction == True:
                    player = player + 1
                else:
                    player = player - 1
            
            elif CardToPlay[1] == 11:  #card is reverse
                direction = not direction
            
            elif CardToPlay[1] == 12:  #card is +2
                # get the next players hand
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
            
            elif CardToPlay[1] == 13:  #card is Wildcard, set color
                IColor = random('Red','Blue','Yellow','Green')
                WildCardReplacementIndex = Shared_Deck.index([IColor],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
            
            elif CardToPlay[1] == 14:  #card is +4, set color
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                
                IColor = random('Red','Blue','Yellow','Green')
                WildCardReplacementIndex = Shared_Deck.index([IColor],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
        
        else:
            print("No card to play, going to next turn.")
    
    #next turn/loop
    noWinner = False
    if direction == True:
        player = player + 1
        if player > 2:
            player = 1
    else:
        player = player - 1
        if player < 0:
            player = 2




    
    

