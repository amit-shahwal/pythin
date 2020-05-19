import json
from difflib import get_close_matches

data= json.load(open('./data.json','r'))


def getmeaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        cs=input(f"'{get_close_matches(word,data.keys())[0]}' intead of {word}? if yes press 'Y' else 'N: ")
        if cs == "y" or cs == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return 'word not exist , please try again'
    else:
        return 'word not exist , please try again'


word=input("enter word: ")
k=getmeaning(word)
if type(k)== list:
    for i in k:
        print(i)
        
else:
    print(k)





