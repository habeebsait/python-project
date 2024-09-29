place = "[name]"
names = []
with open("/Users/habeebsait/Desktop/Python/file_handling/text") as file:
    names = file.readlines()


with open("file_handling/letter.txt") as file:
    letter_content = file.read()
    for name in names:
        new_letter = letter_content.replace(place,name)
        with open(f"file_handling/{name}", "w") as f:
            f.write(new_letter)

