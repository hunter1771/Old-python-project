# Hunter 
#RockPaperScissers.py

import random
choices = ["rock","paper","scissors"]
print("rock crushes scissors. scissors cut paper.papercovers rock.")
player = input("do you want tobe rock,paper,or scissors (or quit)?")
while player != "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("you chose" +player+",and the computer chose " +computer+ ".")
    if player == computer:
        print9"its a tie!")

    elif player == "rock":
        if computer == "scissors":
            print("you win!")
        else:
            print("computer wins")
        elif player == "paper":
            if computer == "rock"
                print("you win"
            else:
                 print("computer wins")
        elif player == "scissors":
            if computer == "paper":
                      print("you win")
            else:
                print("computer!")

         else:
              print("ithink there was some sort of error...")

# notes: I made this almost a year ago and i cant remember a lot of the commands and some of the senta errors i dont understand..the class i was takeing was basicly
# reading out of a programing book and typeing up the code...
            
                      
        

            
