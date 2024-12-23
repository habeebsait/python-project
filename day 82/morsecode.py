MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', ' ': ' ', ' ' : '',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', '@': '.--.-.', ':': '---...', ',': '--..--', '.': '.-.-.-',
    "'": '.----.', '"': '.-..-.', '?': '..--..', '/': '-..-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '!': '-.-.--'
}

query = input("Encode or Decode morse code: ")

if query == "decode":
    decoded = []
    morse_input = input("Enter ur morse code: ")
    morse_list = morse_input.split(" ")
    
    for i in morse_list:
        value_to_find = i
        keys = [key for key, value in MORSE_CODE_DICT.items() if value == value_to_find]
        decoded.append(keys[0])
    
    for i in decoded:
        print(i, end= "")


if query == "encode":
    encoded = []
    word_input = input("Enter the string to be encoded: ")
    word_list = []
    for i in word_input:
        word_list.append(i)

    for i in word_list:
        key_to_find = i
        values = [value for key, value in MORSE_CODE_DICT.items() if key == key_to_find]
        encoded.append(values[0])

    for _ in encoded:
        print(_, end = " ")
