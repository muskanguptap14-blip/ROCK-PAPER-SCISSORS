import random
options=("ROCK","PAPER","SCISSORS")

running=True 
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("Enter the option:").upper()
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player is not options:
            print("Please Enter correct options!!!")
        elif player==computer:
            print("ITS A TIE!!!")
        elif player=="ROCK" and computer=="SCISSORS":
            print("YOU wins!!!")
        elif player=="SCISSORS" and computer=="PAPER":
            print("YOU wins!!!")   
        elif player=="PAPER" and computer=="ROCK" :  
            print("YOU wins!!!") 
        else:
            print("you lose")   
        if not input("Play again ?(y/n):").lower()=="y":
            running=False

print("******************THANKS FOR PLAYING****************")            