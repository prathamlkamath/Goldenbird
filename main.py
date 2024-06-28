import random

words = ["spiderman", "batman", "shakthiman", "hanuman", "ironman", "pratham"]
stages = [
    '''
  +---+
  |   |
  ☠️   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  😢  |
 /|\  |
 /    |
      |
=========

''', '''
  +---+
  |   |
  😢  |
 /|\  |
      |
      |
=========

''', '''
  +---+
  |   |
  😢  |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  😢  |
  |   |
      |
      |
=========

''', '''
  +---+
  |   |
  😢  |
      |
      |
      |
=========

''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
chosen_word = random.choice(
    words).lower()  #i have done this to make the word in lower case
display = ["_"] * len(chosen_word)

word_length = len(chosen_word)
print(display)
attempts_left = 7  #you can change as per your need. I will allow only 5 attempts
incorrect_guesses = []

while attempts_left > 0:
  guess = input("Guess a letter: ").lower()

  if guess in chosen_word:
    for position in range(word_length):
      if chosen_word[position] == guess:
        display[position] = guess
  else:  #if your guesseed letter not in choosen word then this part will be executed
    if guess not in incorrect_guesses:  #we are checking if the guessed letter is not in the list of incorrect guesses. If already present then we will not add it to the list of incorrect guesses.
      print(stages[attempts_left - 1])
      attempts_left -= 1  #decrement the attempt left each time for wrong input
      incorrect_guesses.append(guess)

      print(f"Incorrect guess. You have {attempts_left} attempts left.")
    else:
      print("You already guessed that letter. Try a different one.")

  print("\n", display)

  if "_" not in display:  #if all the letters are guessed correctly then just print you win
    print("\nYou win!")
    break
else:
  print("\nYou lose! The word was:", chosen_word)
