import random

print("🎮 Number Guessing Game")
print("Guess a number between 1 and 10")

secret_number = random.randint(1, 10)

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Congratulations! You guessed correctly.")
else:
    print(f"❌ Wrong guess! The number was {secret_number}")