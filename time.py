from datetime import datetime

# current date and time
now = datetime.now()
today=datetime.today()
breakpoint()

t = now.strftime("%H:%M:%S")
print("Time:", t)