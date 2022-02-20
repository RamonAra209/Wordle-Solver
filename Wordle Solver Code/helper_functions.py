from cgi import print_form
import os, random, re
from collections import defaultdict

def generate_correct_answer() -> str: #* Works
    word = None
    with open('possible_answers.txt', 'r') as f:
        lines = f.readlines()
        word = lines[random.randint(0, len(lines))]
        f.close()
    return word

def initial_guess() -> list:
    initial_guess = None
    with open('guesses.txt', 'r') as f:
        lines = f.readlines()
        initial_guess = lines[random.randint(0, len(lines))]
        f.close()
    initial_guess = initial_guess[0:5]
    return initial_guess
        
def subsequent_guesses(possible_words:list) -> str:
    return possible_words[random.randint(0, len(possible_words) - 1)]



#########* Guess Checking Functions
def check_guess(guess:str, answer:str) -> dict: #* Works
    guess_dict = {} #? dict {letter : [indexes] }
    for i in guess:
        index_positions = []
        if i in answer:
            for j, letter in enumerate(answer):
                if i == letter:
                    index_positions.append(j)
        elif i not in answer:
            index_positions.append(-1)
        guess_dict[i] = index_positions
        
    # print(f"CHECK GUESS(): {guess_dict}")
    return guess_dict

def refine_guess(guess_dict):
    good_guess = {} # structure = letter: index
    bad_guess = []
    for key, val in guess_dict.items():
        if guess_dict[key][0] == -1:
            bad_guess.append(key)
        else:
            good_guess[key] = val
            
    for letter in good_guess.keys():
        if letter in bad_guess:
            bad_guess.pop(letter)
    
    return good_guess, bad_guess

#########* Sifting for Possible words
def possible_words(good_letters: dict, bad_letters: list, possible_words=None) -> list:
    # print("\n\tPossible_words() Input")
    # print(f"\t\t Good Words: {good_letters} \n \t\t Bad Letters: {bad_letters}")
    word = [".", ".", ".", ".", "."]

    # print(f"\tWord before good letter: \n \t\t{word} \n")
    ####? Good letter
    for key, val in good_letters.items():
        print(f"\t\tGood Letter: {key}")
        for index in val:
            word[index] = key
    
    # print(f"\tWord after good letter: \n \t\t{word} \n")
    
    for index, val in enumerate(word):
        if val == ".":
            word[index] = "[^]"
            
    # print(f"\tWord after [^]: \n \t\t{word}\n")
    
    #### Bad Letters
    for index, val in enumerate(word):
        if val[0] == "[":
            for letter in bad_letters:
                word[index] = word[index][:2] + letter + word[index][1:]
    # print(f"\tWord after bad letter: \n \t\t{word}\n")
    
    ####? Possible word in word bank
    regex_word = "".join(word)
    regex_list = []
    
    if possible_words == None:
        with open('guesses.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line[0:5]
                val = re.findall(regex_word, line)
                if len(val) > 0:
                    regex_list.append(val)
            f.close()
    else:
        for word in possible_words:
            val = re.findall(regex_word, word[0])
            if len(val) > 0:
                regex_list.append(val)
                
    return regex_list


def merge_dicts(base_dict, dict_two) -> dict:
    return base_dict | dict_two

def merge_lists(base_list, list_two) -> list:
    return base_list + list_two

