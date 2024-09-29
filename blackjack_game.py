import random

logo_blackjack = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo_blackjack)    

user_score = -1
comp_score = -1

def defl_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card



def check(user_score, comp_score):
    if user_score == 21 or comp_score == 21:
        return 0
    
def calc_score(user_cards , comp_cards):
    user_score = sum(user_cards)
    comp_score = sum(comp_cards)
    return user_score, comp_score


user_cards = []
comp_cards = []

play = input("Do you want to play black jack: (y/n)").lower()



if play == "y" or play == True:
    play == True
    for i in range(2):
        user_cards.append(defl_card())
        comp_cards.append(defl_card())

else:
    play == False

user_score , comp_score = calc_score(user_cards, comp_cards)


game = check(user_score, comp_score)

print(f"Your cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards[0]}")

while user_score < 17:
    user_cards.append(defl_card())
    user_score = sum(user_cards)

while comp_score < 17:
    comp_cards.append(defl_card())
    comp_score = sum(comp_cards)

print(f"Your cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards[0]}")

while play:





    if game == 0 or user_score > 21:
        print("Game Over")
        play = False
        if user_score <= 21 and user_score > comp_score:
            print(f"You win! \nYour cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards}, Computer Score= {comp_score}")

        elif user_score == comp_score:
            print(f"Its a Draw! \nYour cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards}, Computer Score= {comp_score}")

        else:
            
            print(f"You lose! \nYour cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards}, Computer Score= {comp_score}")


    else:
        choice = input("Do you want to draw another card? (y/n): ").lower()
        if choice == "y":
            user_cards.append(defl_card())
            comp_cards.append(defl_card())
            user_score, comp_score = calc_score(user_cards, comp_cards)
            game = check(user_score, comp_score)
            print(f"Your cards: {user_cards}, Your Score: {user_score} \nComputer Card = {comp_cards[0]}")

        else:
            game = 0

        

    