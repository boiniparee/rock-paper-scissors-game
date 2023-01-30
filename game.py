import random
import time
print("hello player")
time.sleep(1)
print("welcome to Rock, Paper, Sicssors game")
time.sleep(1)
while True:
    print("enter your choice a number\n 1.Rock\n 2.paper\n 3.scissors")
    choice=int(input("enter a number "))
    
    while choice>3 and choice<1:
        choice=int(input("enter a valid input"))
        time.sleep(1)
    if choice==1:
        choicename="Rock"
    elif choice==2:
        choicename="Paper"
    else:
        choicename="Scissors"
 
    print("player choice is",choicename)
    print("computer is picking..................... ")
    time.sleep(0.5)
    computerchoice=random.randint(1,3)
    if computerchoice==1:
        computerchoicename="Rock"
    elif computerchoice==2:
        computerchoicename="Paper"
    else:
        computerchoicename="Sicssors"
    print("computer choosen name",computerchoicename)
    
    if choice==computerchoice:
        time.sleep(1)
        print("its a draw!")
    elif choice==1 and computerchoice==3:
        time.sleep(1)
        print("you win!")
    elif choice==2 and computerchoice==1:
        time.sleep(1)
        print("you win!")
    elif choice==3 and computerchoice==2:
        time.sleep(1)
        print("you win!")
    else:
        time.sleep(1)
        print(" you lose and computer win!")
        time.sleep(1)
    print("would to like to play again(Y/N) ")
    playagain=input().lower()
    if playagain=="n":
        break;
        
