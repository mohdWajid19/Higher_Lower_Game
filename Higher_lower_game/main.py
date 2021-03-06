from replit import clear
from art import logo,vs
from data import data
import random

def give_opponent():
    '''returns the data of some random person from data list of dictionaries'''
    return random.choice(data)

def print_opponent(opponent, sno):
    '''prints the opponent's data'''
    print(f"\n competant : {sno}", end=". ")
    print(opponent['name'],end = ', ')
    print(opponent['follower_count'],end = ', ')
    print(opponent['description'],end = ', ')
    print(opponent['country'],end = "\n\n")

def compare_opponents(opponent1, opponent2):
    if opponent1['follower_count'] > opponent2['follower_count']:
        return 1
    elif opponent1['follower_count'] < opponent2['follower_count']:
        return 2 
    else:
        return 0

def user_voted(string):
    if string == '1':
        return 1
    elif string == '2':
        return 2
    else: #this one is if user entered anything other than 1 or 2
        return 0

def play_game():
    '''the actual game engine of higher or lower game'''
    score = 0
    is_correct = True
    opponent_1 = give_opponent()
    while is_correct:
        clear()
        print(logo)
        print(f'You got it correct, score = {score}')
        print_opponent(opponent_1 ,1)
        print(vs)
        opponent_2 = give_opponent()
        print_opponent(opponent_2,2)
        user_guess = input("GUESS WHICH COMPETANT HAS GOT MORE FOLLOWERS HIGHER ONE OR LOWER ONE \n (Enter 1 or 2) :: ")
        user_guessed = user_voted(user_guess)
        more_famous = compare_opponents(opponent_1,opponent_2)
        if user_guessed != 0 and user_guessed == more_famous:
            score += 1
            opponent_1 = opponent_2
        elif more_famous == 0:
            score += 1
            print("You got lucky, they both got same followers")
        else:
            if user_guessed == 0:
                print("you tried entering wrong value,")
            print(f"You Played well, \n Your Guess was wrong, your score is {score}")
            is_correct = False
    if input("wanna play again (y/n): ") == 'y':
        play_game()


play_game()
    
