def sentencemakers(x):
    z=('how','what','why')
    y=x.capitalize()
    if(x.startswith(z) or y.startswith(z)):
        return (f"{y}?") #f stands for format
    else:
        return (f"{y}.")


# print(sentencemakers('what is your name'))

result=[]
while True:
    userinput=input(" say something: ")
    if userinput == "/end":
        break
    else:
        result.append(sentencemakers(userinput))

print(' '.join(result))  