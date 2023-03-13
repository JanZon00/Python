import datetime
import time

now = datetime.datetime.now()
while True:
    x = now.second
    sec = ""
    if x < 10 :
        sec = "0" + str(x)
        print(chr(16),"    ", now.hour,":",now.minute,":",sec,"    ",chr(17), end="\r", sep="")
    else:    
        print(chr(16),"    ", now.hour,":",now.minute,":",now.second,"    ",chr(17), end="\r", sep="")
    now = datetime.datetime.now()
    time.sleep(1)