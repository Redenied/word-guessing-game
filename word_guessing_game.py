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

word = words[random.randrange(len(words))]
answer = False
show = ["_" for _ in range(len(word))]

for char in show:
	print(char)

while not answer:
	guess = input("Guess a character: ")
	for i in range(len(word)):
		if word[i] == guess:
			show[i] = guess
	for char in show:
		print(char)

	if "_" not in show:
		break
print(f"Correct! The answer is {word}")
