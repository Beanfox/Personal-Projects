import pathlib
import random

print("Welcome To Budget Wordle & Try To Find The 5 Letter Word In 6 Tries")

WORDLIST = pathlib.Path("5_Letter_Words.txt")

words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
word = random.choice(words)

prev_guesses = []

for guess_num in range(1, 7):
    guess = input("\n" + "What is Your Guess: ").upper()
  
    while len(guess) != 5:
      print("Make Sure Your Guess Is 5 Letters Long!", "\n")
      guess = input("What is Your Guess: ").upper()
      if len(guess) == 5:
        break

    while prev_guesses.count(guess):
      print("This Was Already Tried!", "\n")
      guess = input("What is Your Guess: ").upper()
      
    prev_guesses.append(guess)
  
    if guess == word:
        print("Correct")
        break

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

if guess_num == 6:
      print(f"The Word Was {word}")