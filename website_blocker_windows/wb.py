from datetime import datetime as dt
import time
host_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
wb_list=["www.fb.com","fb.com",]
host_temp="hosts"
# f= open(host_path,"r")
# print(f.read(-1))

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt(dt.now().year,dt.now().month,dt.now().day,2):
        print("Working Hour..")
        with open(host_temp,'r+') as file:
            content=file.read()
            for w in wb_list:
                if w in content:
                    pass
                else:
                    file.write(redirect+" "+w+"\n")

    else:
        with open(host_temp,'r+') as file:
            con=file.readlines()
            file.seek(0)
            for line in con:
                if not any(w in line for w in wb_list):
                    file.write(line)
            # file.seek(0)
            file.truncate()
            
        print("fun")
    time.sleep(5)


    
