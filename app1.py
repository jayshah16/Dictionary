import json
from difflib import get_close_matches

data = json.load(open('data.json'))
"""
created a function which fetches data from json file and gives the meaning of word
 

elif  will check nearest possiblity of the word that exist in the dictionary if the user
misspells the word
get close matches is the method in which w is the word that user inputs, data.keys() finds the nearest
word to that word and len>0 check the length of word is greater than 0
"""
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) >0 :
        yn = input("Did you mean %s instead? Enter Y if yes , or N if no :" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist"
        else:
            return "We did not understand your query"

    else:
        return"Please Enter a Valid Word"

word = input("Enter a word: ")
output= translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)