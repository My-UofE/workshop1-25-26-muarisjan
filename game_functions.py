import random

#Now it picks the middle value to help choose binary search method which is more optimal
def pick_value(poss_values):
    mid_val = len(poss_values)//2
    return poss_values[mid_val]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    #if higher (h) predicted corr
    if next_val > current_val and user_input == 'h':
        return True
    #if lower (l) predicted corr
    elif next_val < current_val and user_input =='l':
        return True
    #wrong prediction
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    #set flag to process if found or not;
    flag = False
    #checking guessed letter against board loop 
    for i in range(len(word)):
        if word[i]== letter:
            board[i]= letter
            flag = True
    
    if flag:
        print(f"Well done! {letter} is in the word")
        return True
    else:
        print(f"Sorry, {letter} is not in the word")
        return False

    