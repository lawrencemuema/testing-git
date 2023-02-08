import random
print("Welcome to zakdu")
print("Guess a number between 1 - 100")

# number = 45
number = random.randint(1,100)
attempts = 0

# while x:

# guess = int(guess)

while attempts < 5:
    guess = int(input("whats your guess"))
    attempts = attempts + 1
    # attempts += 1
    # guess < number  #! less than
    # guess > number  #! greater than
    # guess <= number #! less than or equal to
    # guess == number #! equal to
    # guess != number #! not equal to


    if guess < number:
        print("Too low, guess again")
    elif guess > number:
        print("Too high, guess again")
    else:
        print("Congratulations, you have guessed correctly")
        break