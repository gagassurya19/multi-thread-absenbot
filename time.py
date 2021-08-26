from datetime import datetime
from time import sleep

def time():
    while True: 
        format = '%H:%M:%S'

        now = (datetime.now()).strftime(format)
        tomorrow = '05:50:00'

        timeRemain = datetime.strptime(tomorrow, format) - datetime.strptime(now, format)

        if(now != tomorrow):
            print( timeRemain, now, tomorrow, end="\r")
            sleep(1)
        else:
            break 

time()
print("finally")