import json
from difflib import get_close_matches

data= json.load(open('./data.json','r'))


def getmeaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        return (f"'{get_close_matches(word,data.keys())[0]}' intead of {word}")
    else:
        return 'word not exist , please try again'


word=input("enter word: ")
# j=0
# for i in (getmeaning(word)):
#     j=j+1
#     print(f" %s : %s"%(j,i))
print(getmeaning(word))




