import random
import resources

def are_all_blanks_filled():
  if chosen_word_in_blanks.find("_") == -1:
    return True
  else:
    return False

def has_run_out_of_lives():
  if guess_count == max_guess_count:
    return True
  else:
    return False
    
chosen_word = random.choice(resources.word_list)
max_guess_count = len(chosen_word) + 2
guess_count = 0

chosen_word_in_blanks = ""
for char in chosen_word:
  chosen_word_in_blanks += "_"

print(f"{resources.logo}\n\n")
print(f"Your word is: {chosen_word_in_blanks}")
print(f"You have {max_guess_count} guesses.")

while not are_all_blanks_filled() and not has_run_out_of_lives():
  guess = input("Guess a letter: ").lower()

  if len(guess) > 1:
    print(f"You can only guess one letter at a time.")
  elif len(guess) == 0:
    print(f"You didn't enter any letter. Try again.")
  elif chosen_word_in_blanks.find(guess) != -1:
    print(f"You've already guessed the letter: {guess}")
  else:
    guess_count += 1
    
    chosen_word_in_blanks_list = list(chosen_word_in_blanks)
    for idx, char in enumerate(chosen_word):
      if guess == char:
        chosen_word_in_blanks_list[idx] = guess
    chosen_word_in_blanks = "".join(chosen_word_in_blanks_list)
    
    if has_run_out_of_lives():
      print(f"Oh no! You lost.")
      print(f"\nYour word was: {chosen_word}")
    elif are_all_blanks_filled():
      print(f"\nYour word is: {chosen_word_in_blanks}")
      print(f"You won!")
    else:
      print(f"\nYour word is: {chosen_word_in_blanks}")
      print(f"You have {max_guess_count - guess_count} guesses left.")