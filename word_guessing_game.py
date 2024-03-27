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
		# Conert '_' into the guessed letter if its in word
		for i in range(len(word)):
			if word[i] == guess:
				show[i] = guess
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
	return

main()
