#Gabriel Harrison
#1.4 project
import random

#menu
def menu():
    play = input("Would you like to \n1 Play The Number Guessing Game\n2 Play Custom Game\n3 Play Coin Flip Game\n4 Read The Credits\n5 Exit?\n")
    if play == "1":
        main_game()
    elif play == "4":
        print("""Guessing games by
Gabriel Harrison
Colton Miller
Made 11/2/2018""")
        menu()
        
    elif play == "5":
        quit_x()
    elif play == "2":
        custom_game()
    elif play == "3":
        coin_game()
    else:
        print( play ,"is not a valid option please type 1, 2, or 3.")
        menu()
    
#main game
def main_game():
    guess=0
    guess_amount=5
    secret_number=random.randint(1,100)
##    print(secret_number)
    
    while guess_amount > 0:
        guess = float(input("guess the number 1 to 100: "))
        if guess == secret_number:
            print("YOU WIN!","The secret number is", secret_number)
            break
        elif guess > secret_number:
            guess_amount += 1
            print("Your guess was too high guess lower")
        elif guess < secret_number:
            guess_amount -= 1
            print("Your guess was too low guess higher")
            
       
       
    else:
        print("You ran out of guesses You Lose","The secret number is", secret_number)

#coin game
def coin_game():
    coin=random.randint(1,2)
    print(coin)
    #You needed an int before the input to keep it from making a string
    user_coin=int(input("Heads(1) or tails(2)"))
    if user_coin!=1 or user_coin!=2:
        print("That is not a number")
        menu()
    if user_coin==coin:
        print("You win", "The name was", coin)
    else:
        print("You lost")
#monster attack
def custom_game():
    win=0   
    monster_health= 100
    player_health= 100
    print("you are at 100 health", "and so is the monster")
    choice =input("attack or run")
    if choice!="attack" or choice!="run":
        ("I'm not sure what you said")
       
        

   
    

    while choice=="attack":
        
        print("you attack the monster")
        player_damage=random.randrange(0,25)
        monster_damage=random.randrange(0,50)
        monster_health-= player_damage
        
        if monster_health>0:
            print("monster attacks you for", monster_damage)
            player_health -= monster_damage
        if player_health<=0:
            win=0
            print("You died")
            break
        elif monster_health<=0:
            win= 1
            print("you have killed the monster")
            break
        if choice=="run":
            print("You are a coward")
        elif player_health >=0 and monster_health>=0:
            print("you have",player_health,"health")
            print("the monster has", monster_health, "health")
            choice=input("attack or run")
        if choice!= "attack" or choice !="run":
            print("I'm not sure what that was")
            continue
        else:
            continue

    if choice=="run":
        print("you are a coward")
        menu()

    
    if win==0:
        print("game over")
        menu()
    else:
        print("you win")
#quit    
def quit_x():
    ask_again=input("Are you sure?")
    if ask_again=="yes" or ask_again=="Yes":
        exit
    else:
        menu()
            

menu()
