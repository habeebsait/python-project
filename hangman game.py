name = input("Enter a movie: ")


hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

n =7
 
vowels = ['a','e','i','o','u']
blank =[]
for i in name:
    if i in vowels:
        blank += i
    else:
        blank += ["_"]

print(blank)

n=0

while "_" in blank:
    guess = input("Guess the movie!!: ")

    if n==6:
        print(hangman[n])
        break

    elif guess not in name:
        print(hangman[n])
        n+=1

    
    else:
        for i in range(len(blank)):
            if guess == name[i]:
                blank[i] = guess
        print(blank)
        
if "_" in blank:
    print("Game over! You lose")

else:
    print("You win!")
