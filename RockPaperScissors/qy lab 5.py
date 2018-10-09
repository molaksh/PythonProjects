# A Python program for the Rock, Paper, Scissors game. 
from random import randint

def rock_paper_scissors():

    t = ["rock", "paper", "scissors"]
    

    win = 0
    lose = 0

    points = int(input("\nHow many points does it take to win? "))
    print()
    
    i =1
    while (win < points and lose < points):
        print("********************* ROUND #",i," *********************")
        player = input("\nPick your throw: [r]ock, [p]aper, or [s]cissors? ")
        computer = t[randint(0,2)]
        if(player =='r'):
            player = "rock"
        elif(player == 'p'):
            player = "paper"
        elif(player == 's'):
            player = "scissors"



        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("Computer threw ", computer," you lose!")
                lose +=1
            else:
                print("Computer threw ",computer," you win!")
                win += 1
        elif player == "paper":
            if computer == "scissors":
                print("Computer threw ",computer," you lose!")
                lose +=1
            else:
                print("Computer threw ",computer," you win!")
                win+=1
        elif player == "scissors":
            if computer == "rock":
                print("Computer threw ",computer," you lose!")
                lose+=1
            else:
                print("Computer threw ",computer," you win!")
                win+=1
        else:
            print("That's not a valid play. Check your spelling!")

        print()
        print("\nYour score: ",win)
        print("Computer’s score: ",lose)
        print()
        i=i+1

    print("********************* GAME OVER ********************")
    print()
    if(win>lose):
        print("You win!")
    elif(win<lose):
        print("Computer wins!")
        
    
    ''' Write your code for playing Rock Paper Scissors here. '''

def main(): 
    print('ROCK PAPER SCISSORS in Python')
    print()
    print('Rules: 1) Rock wins over Scissors.')
    print('       2) Scissors wins over Paper.')
    print('       3) Paper wins over Rock.')
    
    rock_paper_scissors()
    
main()
