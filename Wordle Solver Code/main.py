# Command to get todays answer: (new window.wordle.bundle.GameApp).solution 
# Paste into developer view console in Chrome inspect element

import re, random
import helper_functions as help_funcs

# word_to_solve = help_funcs.generate_correct_answer()
word_to_solve = "tacit"
num_guess = 1
next_guess = None
possible_words = None
final_guess = None

dict_good_letters = {}
list_of_bad_letters = []

print(f"Correct Word: {word_to_solve}")
guess_list = []
while num_guess <= 6:
    print(f"Iteration: {num_guess}")
    if num_guess == 1:
        next_guess = help_funcs.initial_guess()
        guess_list.append(next_guess)
        check_guess = help_funcs.check_guess(next_guess, word_to_solve)
        
        good_letters, bad_letters = help_funcs.refine_guess(check_guess)
        print(f"\tGood Letters: {good_letters}")
        print(f"\tBadLetters: {bad_letters}")
        
        dict_good_letters = help_funcs.merge_dicts(dict_good_letters, good_letters)
        list_of_bad_letters = help_funcs.merge_lists(list_of_bad_letters, bad_letters)
        
        possible_words = help_funcs.possible_words(dict_good_letters, list_of_bad_letters)
    if num_guess >= 1:
        guess_index = random.randint(0, len(possible_words) - 1)
        next_guess = possible_words[guess_index][0] #! Was possible words - 1
        guess_list.append(next_guess)
        
        
        print(f"\t Good Letters: {dict_good_letters}")
        print(f"\t Bad Letters: {list_of_bad_letters}")
        
        check_guess = help_funcs.check_guess(next_guess, word_to_solve)
        if next_guess == word_to_solve:
            final_guess = next_guess
            print("\n\n\n### GUESSED CORRECTLY ###")
            print(f"### {next_guess} == {word_to_solve} ###\n\n\n")
            num_guess += 1
            break
        
        good_letters, bad_letters = help_funcs.refine_guess(check_guess)
        list_of_bad_letters = help_funcs.merge_lists(list_of_bad_letters, bad_letters)
        dict_good_letters = help_funcs.merge_dicts(dict_good_letters, good_letters)
        possible_words = help_funcs.possible_words(dict_good_letters, list_of_bad_letters, possible_words)
        # print(possible_words)
        
    num_guess += 1

print(f"Wordle of the day: {word_to_solve}")
print("Guesses taken:")
for i, guess in enumerate(guess_list):
    print(f"\t{i+ 1}. {guess}")
print(f"Final Guess: {final_guess} ") 
print(f"Took {num_guess} guesses to solve")

