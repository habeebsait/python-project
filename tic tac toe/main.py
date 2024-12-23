import os

def print_dict():
    for i in dicto:
        print(dicto[i], end = "")
        if i%3 == 0:
            print()
            if i != 9:
                print("- - -")
        else:
            print("|", end = "")
    
    print("\n")
    for i in dict:
        print(dict[i], end = "")
        if i%3 == 0:
            print()
            if i != 9:
                print("- - -")
        else:
            print("|", end = "")

def check_win():
    for x in WINS:
        if all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x):
            return "X wins"
    for x in WINS:
        if all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x) or all(m in x_index for m in x):
            return "O wins"
    else:
        return "None"


def x_turn():
    global x_index
    
    pos = int(input("X's Turn\nChoose a position:(1-9): "))
    x_index.append(pos)
    dict[pos] = "X"

def o_turn():
    global y_index
    pos = int(input("O's Turn\nChoose a position:(1-9): "))
    dict[pos] = "O"
    y_index.append(pos)

def clear_terminal():
    os.system("clear") ### cls for windows


x_index = []
y_index = []

WINS = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]



dicto = {key:str(key) for key in range(1,10) } 

print("\n\n")






dict = {key:" " for key in range(1,10) } 


print("\n\n")


game_is_on = True
while game_is_on:
    clear_terminal()

    print_dict()

    print("\n")

    x_turn()
    print("\n\n")
    result = check_win()
    if result == "X wins":
        print_dict()
        print("X wins the game!")
        break

    clear_terminal()

    print_dict()
    print("\n\n")
    

    o_turn()

    result = check_win()
    if result == "Y wins":
        print_dict()
        print("Y wins the game!")
        break