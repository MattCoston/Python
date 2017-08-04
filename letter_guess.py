
import os
import random


list = [apple, tree, pear, grape]

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def draw(bad_guesses, good_guesses, secret_word):
	clear()

	print("strikes: {}/7".format(len(bad_guesses)))
	print('')

	for letter in bad_guesses:
		print(letter, end=' ')
	print("\n\n")


	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_', end='')
	print('')
			
while True:
	start = input("Press enter to start, or enter Q to quit")
	if start.lower() =='q':
		break

	secret_word = random.choice(list)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):

	

		guess = input("Guess a letter: ").lower()

		if len(guess) != 1:
			print("You can only guess a single letter: ")
			continue
		elif guess in bad_guesses or guess in good_guesses:
			print("You've already guessed that letter: ")
			continue
		elif not guess.isalpha():
			print("You can only guess letters: ")
			continue		

		if guess in secret_word:
			good_guesses.append(guess)
			if len(good_guesses) == len(list(secret_word))
				print("You win!")
				break
		else:
			bad_guesses.append(guess)
	else:
		print("You didnt guess it!  Word was " + str(secret_word))
