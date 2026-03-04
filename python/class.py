import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
max_attempts = 4

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Loop for a maximum number of attempts
for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Take a guess: "))

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"🎉 Correct! You guessed the number {secret_number} in {attempt} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")

else:
    print(f"❌ Sorry, you've used all your attempts. The number was {secret_number}.")
