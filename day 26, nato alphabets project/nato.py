import pandas as pd



f_df = pd.read_csv("day 26/nato_phonetic_alphabet.csv")


##                                ********** one way of doing it ************
# letter = f_df.letter

# code = f_df.code


# #the zip function creates a list of tupples
# dict = {l:c for (l,c) in zip(letter,code)}
# print(dict)

# string = input("Enter your word: ")

# for s in string:
#     print(dict[f"{s.upper()}"])



#                             ************* Second way of doing it!!! *************
dict = f_df.to_dict()

string = input("Enter a word: ")

for s in string:
    value = {i for i in dict["letter"] if dict["letter"][i] == f"{s}"}
    for i in value:
        print(dict["code"][i])