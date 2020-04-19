import random

# game levels
level_one = random.randint(1, 10)
level_two = random.randint(1, 20)
level_three = random.randint(1, 50)

guess_count = 0 # used to keep track of guess attempts
print('''
Hi, Welcome to the number guessing game.
Here are the available levels:
E --- Easy
M --- Medium
H --- Hard
''')

difficulty = input("Please, pick a level [E; M; or H]: ").upper()
# setting conditions for each level
if difficulty == "E":
    guess_limit = 6
    secret_number = level_one
    print("Okay, I have set a number between 1 and 10")
elif difficulty == "M":
    guess_limit = 4
    secret_number = level_two
    print("Okay, I have set a number between 1 and 20")
else:
    if difficulty == "H":
        guess_limit = 3
        secret_number = level_three
        print("Okay, I have set a number between 1 and 50")

# running the game until user exhaust their life lines
while guess_count < guess_limit:
    try: # using the try/ecxept ErrorValue to ensure user inputs a number
        guess = int(input('Take a guess: '))
        guess_count += 1
        if guess < secret_number or guess > secret_number:
            print(f'''That was wrong! You have  {guess_limit - guess_count} guesses left!

*****************************************
        ''')
        else:
            if guess == secret_number:
                break
    except ValueError:
        print('Please, enter a number.')
        continue
if guess == secret_number: # this happens if user guess is right
    guess_count = str(guess_count)
    print('YOU GOT IT RIGHT! It took you ' + guess_count + ' guesses!')
else:
    if guess != secret_number: # if user wrong/exhausted life line
        secret_number = str(secret_number)
        print('GAME OVER! The correct guess is ' + secret_number)
