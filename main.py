
# Online Python - IDE, Editor, Compiler, Interprete
def sum(a, b):
   return (a + b)
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
print(f'Sum of {a} and {b} is {sum(a, b)}')
import random
def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors:")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    return choices  
def check_win(player, computer):
    print(f"you chose {player} , computer chose {computer}" )
    if player == computer:
        return "round tied"      
    elif player == "rock":
        if computer == "paper":
            return "you loose"
        else :
            return "you win"          
    elif player == "scissors":
        if computer == "paper":
            return "you win"
        else :
            return "you loose"          
    elif player == "paper":
        if computer == "rock":
            return "you win"
        else :
            return "you loose"  
print (result)
result = check_win(choises["player"], choises["computer"])
choises = get_choices()

n = 8
ar = [ 1, 2, 1, 1, 3, 4, 2, 3 ]

def sockMerchant(n, ar):
    # Write your code here
    main_count=0
    count=0
    i=j=0
    for x in ar :
        for y in ar:
            if x==y:
                count+=count
            

