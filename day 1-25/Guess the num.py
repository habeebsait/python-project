import random

def check(guess):
        
        global ATTEMPT
        if guess < num:
            print("Too low!")
            ATTEMPT -= 1
            print(f"You have {ATTEMPT} attempts remaining")
            return 

        elif guess > num:
            print("Too high!")
            ATTEMPT -= 1
            print(f"You have {ATTEMPT} attempts remaining")

        elif guess == num:
            print("You guessed the right number!")
            ATTEMPT = 0


print("Welcome to the number guessing game! \nI am thinking of a number between 1 to 100!")
num = random.randint(1,100)
print(num)
choice = input("Choose difficulty: (Easy / Hard): ").lower()

if choice == "easy":
    ATTEMPT = 10

else:
    ATTEMPT = 5

print(f"You have {ATTEMPT} attempts")

guess = 100000

while ATTEMPT != 0:
    guess = int(input("Enter your guess: "))
    check(guess)


if guess != num:
    print(f"You loose the number was {num}")

