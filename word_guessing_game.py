#!/usr/bin/env python3

import random

words = [
"alligator",
"python",
"random",
"shrek",
"football",
"calculator",
"business",
"steel",
"holiday",
"florida"
]

def guessing(word, show):
	while True:
		guess = input("Guess a character: ")
		# Convert '_' into the guessed letter if its in word
		for i in range(len(word)):
			if word[i] == guess:
				show[i] = guess
		if (guess not in word and len(guess) == 1) or len(guess)>1:
			print("Whoops! Try again.")

		# Print underscores with revealed letters
		for char in show:
			print(char)
		# If we have no hidden letters, it means the word is discovered
		if "_" not in show:
			break
	return

def main():
	word = words[random.randrange(len(words))]	# Get word picking a random list index
	show = ["_" for _ in range(len(word))]		# List of underscores the size of word

	for char in show:	# Print vertically the hidden letters
		print(char)

	guessing(word, show)

	print(f"Correct! The answer is {word}")

	# Play again if user answers yes
	play_again = input("Want to play again?(Y/N) ").lower()
	if play_again == "y":
		# Clear word and show and run main again
		word = ""
		show = []
		main()

	return

main()

