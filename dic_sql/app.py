import mysql.connector
from difflib import get_close_matches

con=mysql.connector.connect(
    user='ardit700_student',
    password='ardit700_student',
    host='108.167.140.122',
    database='ardit700_pm1database'
)
# word=input("WORD: ")
cursor=con.cursor()
# fetching all the words and meanings inside list
querystring=(f"select * from Dictionary ")

cursor.execute(querystring)
results=cursor.fetchall()

word=input("WORD:  ")

for d in results:
        if word in d:
            querystring=(f"select * from Dictionary WHERE Expression = '{word}' ")
            cursor.execute(querystring) 
            resul_t=cursor.fetchall()
            for re in resul_t:
                print(re[1])
            exit(0)

# creating list of all the keys
ll=[]           

for d in results:
    ll.append(d[0])

if len(get_close_matches(word,ll))>0:

    yesorno=input(f"'{get_close_matches(word,ll)[0]}' intead of {word}? if yes press 'Y' else 'N: ")
    if yesorno =='y' or yesorno == 'Y':
        querystring=(f"select * from Dictionary WHERE Expression = '{get_close_matches(word,ll)[0]}' ")
        cursor.execute(querystring) 
        resul__t=cursor.fetchall()
        for res in resul__t:
            print(res[1])
        



   
    

