#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
guessedRight = False

while not guessedRight and word_length != 0:
  guess = input("Guess a letter: ").lower()
  correct_guess = False
  #Check guessed letter
  if guess not in display:
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            correct_guess = True

    if correct_guess:
      print(display)
      if "_" not in display:
        print('You won.')
        guessedRight = True

    else:
      word_length -= 1
      print(f"Wrong, {word_length} attempt(s) left")
      if (word_length == 0):
        print("YOU LOSER")

  else:
    print("The character is already in.")
      


  