from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

print("The script is invoked today Sunday at  \n")

current_time = datetime.now()
print(current_time)

current_time = datetime.now().time()
print(current_time)



# 1. Get the current time in UTC
utc_time = datetime.now(ZoneInfo("UTC"))

# 2. Convert it to IST
ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

print(f"UTC Time: {utc_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"IST Time: {ist_time.strftime('%Y-%m-%d %H:%M:%S')}")
