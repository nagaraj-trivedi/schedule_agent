from datetime import datetime

print("The script is invoked at \n")

current_time = datetime.now()
print(current_time)

current_time = datetime.now().time()
print(current_time)
