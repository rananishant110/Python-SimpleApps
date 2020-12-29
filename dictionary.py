import json
from difflib import get_close_matches

data = json.load(open("data.json"))

#Function to translate the word
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Enter y for yes and n for no : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("This word is not in the Dictionary")
        else :
            return ("Wrong input, please enter y or n:")
    else :
        print("This Word is not present in the Dictionary")

#Taking the user input
word = input("Please enter the word you want to search : ")

#calling our Function
output = translate(word)

#condition to seperate if more than one meanings
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
