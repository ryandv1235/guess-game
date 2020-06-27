import random

inGame = True

while inGame:
	number = input("Type a number for a upper bound: ")

	if number.isdigit():
		print("Let the game begin")
		number = int(number)
		inGame = False

	else:
		print("Invalid input! Try Again!")

secret = random.randint(1, number)
guess = None
count = 1

while guess != secret:
	guess = input("Pls type a number between 1 and " + str(number) + ": ")
	if guess.isdigit():
		guess = int(guess)

	if guess == secret:
		print("You got it!")
	else:
		print("Wrong! Try again!")
		count += 1

print("It took you " + str(count) + " Times.")
print("GG well played!")