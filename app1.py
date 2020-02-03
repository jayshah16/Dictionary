import json

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "please enter a valid word"

word = input("Enter a word: ")
print(translate(word))