import json

data = json.load(open('data.json'))
"""
created a function which fetches data from json file and gives the meaning of word
""" 
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "please enter a valid word"

word = input("Enter a word: ")
print(translate(word))