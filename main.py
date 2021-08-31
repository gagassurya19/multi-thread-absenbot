from pyasn1.type.univ import Null
import scriptabsen
import values
from account.getaccount import getaccount
from discord import sendMessage
import pytz
from time import time, sleep
from datetime import datetime
import concurrent.futures


# TIME-SECTION
WIB = pytz.timezone('Asia/Jakarta')
def setTimer(setTime):
    while True: 
        format = '%H:%M:%S'
        now = (datetime.now(WIB)).strftime(format)
        tomorrow = setTime
        timeRemain = datetime.strptime(tomorrow, format) - datetime.strptime(now, format)
        print(">Time now: ", now, " | Time remaining: ", timeRemain, " | Start at ", tomorrow, end="\r")
        sleep(1)
        if(now == tomorrow):
            break 


# CHOOSE-SHEET-SECTION
isAccount = Null
while (isAccount == Null):
    sheet = str(input('Masukkan sheet: '))
    accountsheet = getaccount(sheet)
    if (accountsheet != Null):
        isAccount = accountsheet
        print(f"[Success] '{sheet}' dalam antrian")
        print("========================================================")
        print(accountsheet)    
        print("Jumlah User: " + str(len(accountsheet)))
        print("========================================================")
    else:
        print("[Error] Sheet tidak ditemukan")


# RUN-SECTION
while True:
    # SET-READY
    setTimer("05:50:00")
    print("\nREADY!", end="\r")
    
    # RUN-AT-05:50AM
    sleep(5 - time() % 5)
    time_now = datetime.now(WIB)
    if (time_now.strftime('%H') == '05' and 
            time_now.strftime('%M') >= '50' and
            time_now.strftime('%a') != 'Sat' and
            time_now.strftime('%a') != 'Sun'):
        start = datetime.now()

        # RUN-SECTION
        time_now_message = datetime.now(WIB)
        sendMessage.info(time_now_message.strftime("%Y/%m/%d"), len(accountsheet), sheet)
        def run(account):
            # DISCORD-SECTION
            user = account[0] # get email
            username = user[0].upper() + user[1:].split('_', 2)[1] # Split
            
            # RUN-SCRIPTABSEN.PY
            temp = scriptabsen.runscript(account, values.sitelogger(), values.browser())
            times = datetime.now(WIB)
            if(temp == True):
                sendMessage.success(username, times.strftime('%c')) # DISCORD
                print(f"[{username}] Absen berhasil pada " + times.strftime('%c')) # CONSOLE
            elif(temp == False):
                sendMessage.warning(username, "Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi", times.strftime('%c')) # DISCORD
                print(f"[{username}] Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi " + times.strftime('%c')) # CONSOLE
                ass = scriptabsen.runscript(account, values.sitelogger(), values.browser())
                timee = datetime.now(WIB)
                if ass == True:
                    sendMessage.success(username, timee.strftime('%c')) # DISCORD
                    print(f"[{username}] Absen berhasil pada " + timee.strftime('%c')) # CONSOLE
                else:
                    sendMessage.failed(username, timee.strftime('%c')) # DISCORD
                    print(f"[{username}] Gagal akses website") # CONSOLE
            else:
                sendMessage.failed(username, times.strftime('%c')) # DISCORD
                print(f"[{username}] Server-mu Down " + times.strftime('%c'))

        # MULTI-THREAD-SECTION
        if __name__ == '__main__':
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(accountsheet)) as executor:
                results = executor.map(run, accountsheet)

        #END
        end = datetime.now() - start
        print(f'finished in {end}')
        sendMessage.done(f"Goodluck ^_^ | Finish in {end}s") # DISCORD