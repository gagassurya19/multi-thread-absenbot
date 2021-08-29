from account.getaccount import getaccount
from discord import sendMessage
from datetime import datetime
import pytz

WIB = pytz.timezone('Asia/Jakarta')
time_now = datetime.now(WIB)

sheet = str(input('Masukkan sheet: '))
accountsheet = getaccount(sheet)
sendMessage.info(time_now.strftime("%Y/%m/%d"), len(accountsheet), sheet)
i = 0
for x in accountsheet:
     # DISCORD
    user = accountsheet[i][0] # get email
    username = user[0].upper() + user[1:].split('_', 2)[1] # Split
    sendMessage.success(username, time_now.strftime('%c')) # DISCORD
    i += 1
sendMessage.done("Goodluck ^_^") # DISCORD