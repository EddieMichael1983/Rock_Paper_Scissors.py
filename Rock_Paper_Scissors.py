print ('Rock Paper Scissors')

user_choice = input('Choose rock, paper, or scissors: ') #the computer asks the user for their choice


import random

rps = ['rock', 'paper', 'scissors']  #defining random values for the computer to choose from


choice = random.choice(rps) #the computer randomly chooses rock, paper, or scissors
print(choice)

if user_choice == 'rock' and choice == 'rock':
    print('tie')
elif user_choice == 'rock' and choice == 'paper':
    print('paper covers rock, you lose')
elif user_choice == 'rock'and choice == 'scissors':
    print('rock smashes scissors, you win')
elif user_choice == 'paper' and choice == 'rock':
    print('paper covers rock, you win')
elif user_choice == 'paper' and choice == 'paper':
    print('tie')
elif user_choice == 'paper' and choice == 'scissors':
    print('scissors cuts paper, you lose')
elif user_choice == 'scissors' and choice == 'rock':
    print('rock smashes scissors, you lose')
elif user_choice == 'scissors' and choice == 'paper':
    print('scissors cuts paper, you win')
elif user_choice == 'scissors' and user_choice == 'scissors':
    print('tie')     #determines who won and tells the user
