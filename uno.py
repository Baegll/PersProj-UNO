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

#  Create Hands (2 player)
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

# discard/topdeck:
discard_pile = []
# get first card, randomly from deck
discard_pile.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
print(discard_pile)

#  Gameplay Setup
noWinner = True
player = 1
direction = True
while(noWinner):
    if player == 1: # then it is the user, not AI
        hasCard = False
        # Check if player has card that matches topdeck
            #if no, force draw
            #if yes, continue
        for card in Player_Hand:
            # Check Color
            if card[0] == discard_pile[-1][0]:
                hasCard = True
            elif card[0] == 'Wild':
                hasCard = True
                
            # Check Number
            if card[1] == discard_pile[-1][1]:
                hasCard = True
        
        if hasCard == False:
            # Draw a card from deck
            Player_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
        if Player_Hand[-1][0] == discard_pile[-1][0]:
            hasCard = True
        elif Player_Hand[-1][0] == 'Wild':
            hasCard = True
        elif Player_Hand[-1][1] == discard_pile[-1][1]:
            hasCard = True
        
        print(f"Your Hand:\n{Player_Hand}")
        if hasCard == True:
            # Allow user to play card
            print("What card color do you want to play:?")
            IColor = input()
            print("What card number do you want to play:?")
            INumber = input()
            index = Player_Hand.index([IColor, INumber])
            CardToPlay = Player_Hand.pop(index)
            discard_pile.append(CardToPlay) #new topdeck
            # Resolve Effects
            # did they win
            if len(Player_Hand) == 0:
                noWinner = False
                print("Congratulations you have won!")
            
            elif CardToPlay[1] == 10:  #card is skip
                if direction == True:
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
                WildCardReplacementIndex = Shared_Deck.index([IColor],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
                
            elif CardToPlay[1] == 14:  #card is +4, set color
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                AI_Hand.append(Shared_Deck.pop(random.randint(0, len(Shared_Deck)-1)))
                
                CInput = input()
                WildCardReplacementIndex = Shared_Deck.index([IColor],any)
                WildCardReplacement = Shared_Deck.pop(WildCardReplacementIndex)
                discard_pile.append(WildCardReplacement)
                
        else:
            print("No card to play, going to next turn.")
    
    else:   # then it is the AI turn
        pass
    
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




    
    

