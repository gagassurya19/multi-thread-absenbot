from datetime import datetime
import pytz
import json

WIB = pytz.timezone('Asia/Jakarta')
time_now = datetime.now(WIB)

time_input = input('input time: ')

time_hours = time_input[0:].split(':')[0]
time_minutes = time_input[0:].split(':')[1]
time_seconds = time_input[0:].split(':')[2]

# time_custom = '{"hours": {}, "minutes": {}, "seconds": {}}'.format(time_hours, time_minutes, time_seconds)
# time_loads = json.loads(time_custom)

# time_now.strftime('%H') == '05'

result = time_hours + ":" + time_minutes + ":" + time_seconds

# print(time_loads[hours])

# some JSON:
x = b'{{"Machine Name":"{0}"}}'.__format__(time_hours)

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])