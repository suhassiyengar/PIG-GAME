import random


def rsndomis_():
    min_=1
    max_=6
    roll=random.randint(min_,max_)
    
    return roll


while True:
    players=input("How many players are there(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            print("\nthe players in game is:\n ",players,)
            break
        
        else:
            print("players must be btw 2-4")

    else:
        print("invalid input")

max_score=10

players_scores=[0 for i in range(players)]

while max(players_scores)<max_score:
    for i in range(players):
        print("player no ",i+1,"has just started.\n")
        print("\nyour total score is: ",players_scores[i],"\n")
        current_score=0

        while True:
            rol_l=input("do you wanna roll(y):")
            if rol_l.lower()!="y":
                break
            
            value=rsndomis_()
            if value==1:
                print("u rolled a 1! your turn ends")
                current_score=0
                break
            else:
                print("you rolled:",value)
                current_score+=value
            print("your current score: ",current_score)
        players_scores[i]+=current_score
winner_score=max(players_scores)
winner=players_scores.index(winner_score)

if max(players_scores)>=max_score:
    print("\n GAME HAS ENDED!\n")
    print("WINNER is player no ",winner+1)







        

