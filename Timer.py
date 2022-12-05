import time
from datetime import datetime
import datetime
import os
import winsound

m2="00"
u=input("Digita orario timer (hh.mm):  ")
u=u.split(".")
if len(u)>1:
    m2=u[1]
h1=u[0]

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'cls'): 
        command = 'cls'
    os.system(command)

def countdown(h2,m2):
    controllo=0
    secondi=2
    while secondi>0:
        stringaorapc=datetime.datetime.now()
        orario=str(stringaorapc).split()
        orario=orario[1].split(":")
        h=int(orario[0])
        m=int(orario[1])+1
        s=orario[2].split(".")
        s=s[0]
        secondi=(h2-h)*3600+(m2-m)*60-int(s)+60
        timer=datetime.timedelta(seconds=secondi)
        time.sleep(0.97)
        if secondi!=controllo and len(str(m2))>1:
                clearConsole()
                print("Tempo rimanente per le ",str(h1)+":"+str(m2),"   -    ",timer)
                controllo=secondi
                g=0
        elif secondi!=controllo:
                clearConsole()
                print("Tempo rimanente per le ",str(h1)+":"+str(m2)+"0   -    ",timer)
                controllo=secondi
                g=0
    frequency = 500  # Set Frequency To 2500 Hertz
    duration = 200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    
           
countdown(int(h1),int(m2))

p=input("Timer terminato, riniziare timer? [s/n]  ")
if p=="s":
        m2="00"
        u=input("Digita orario timer (hh.mm):  ")
        u=u.split(".")
        if len(u)>1:
            m2=u[1]
        h1=u[0]
        countdown(int(h1),int(m2))
    
        
    

    
