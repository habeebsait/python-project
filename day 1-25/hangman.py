print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
''')

name = input("Enter a movie: ")
print('''
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .
      .


''')

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
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
''']

n =7
 
vowels = ['a','e','i','o','u',' ']
blank =[]
for i in name:
    if i in vowels:
        blank += i
    else:
        blank += ["_"]

print("movie:  ", end= "")
for i in blank:
    print(f"{i}", end= "")

n=0

guessed =[]

while "_" in blank:

    print("\n")
    print("Guessed words are: ",end=" ")
    print(guessed)

    guess = input("Guess the movie!!: ")
    guessed += guess
    if n==6:
        print(hangman[n])
        break

    elif guess not in name:
        print(hangman[n])
        print("Oops! Letter not in the word! Try again")
        n+=1


    
    else:
        for i in range(len(blank)):
            if guess == name[i]:
                blank[i] = guess
        print("movie:  ", end="")
        for i in blank:
            print(i, end="")
        
if "_" in blank:
    print("Game over! You lose")

else:
    print("\nYou win!")