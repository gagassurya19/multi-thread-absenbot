from pyasn1.type.univ import Null
import scriptabsen
import values
from account.getaccount import getaccount
import pytz
from time import time, sleep
from datetime import datetime
import concurrent.futures

# CHOOSE SHEET
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

# TIME SECTION
WIB = pytz.timezone('Asia/Jakarta')
time_now = datetime.now(WIB)
def setTimer(setTime):
    while True: 
        format = '%H:%M:%S'
        now = (datetime.now(WIB)).strftime(format)
        tomorrow = setTime
        timeRemain = datetime.strptime(tomorrow, format) - datetime.strptime(now, format)
        print(">Time now: ", now, " | Time remaining: ",timeRemain, " | Start at ", tomorrow, end="\r")
        sleep(1)
        if(now == tomorrow):
            break 

# SET READY
setTimer("05:50:00")
print("\nREADY!")

# RUN
while True:
    sleep(5 - time() % 5)
    if (time_now.strftime('%H') == '05' and 
            time_now.strftime('%M') == '50' and
            time_now.strftime('%a') != 'Sat' and
            time_now.strftime('%a') != 'Sun'):
        def run(account):
            print("[NEW THREAD]")
            temp = scriptabsen.runscript(account, values.sitelogger(), values.browser())
            times = datetime.now(WIB)
            if(temp == True):
                print("Absen berhasil pada " + times.strftime('%c'))
            elif(temp == False):
                print("Absen gagal, SERVER SEKOLAH KENTANK, mencoba lagi " +
                        times.strftime('%c'))
                ass = scriptabsen.override(account, values.sitelogger(), values.browser())
                if ass == True:
                    timee = datetime.now(WIB)
                    print("Absen berhasil pada " + timee.strftime('%c'))
                else:
                    print("Gagal akses website")
            else:
                print("Server-mu Down " + times.strftime('%c'))
        if __name__ == '__main__':
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # data account
                accounts = accountsheet
                results = executor.map(run, accounts)
        print(f'finished')