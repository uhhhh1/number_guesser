import random
name = input("Type your name: ")

print(f"Welcome, {name}")
print("Guess a number between 1-10")
number_to_guess = random.randint(1, 10)
guess = int(input("Enter your guess: "))
print(number_to_guess)

if guess == number_to_guess:
    print("You guessed the number!!! ")

elif guess > number_to_guess:
    print(f"Too high, the number was {number_to_guess}")

else: 
    print(f"Too low, the numer was {number_to_guess}")