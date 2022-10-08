import asyncio
import datetime
import time

async def foo():
  while True:
    await asyncio.sleep(1)
    output = datetime.datetime.now()
    Element("outputDiv2").write(output)

    out3 = Element("outputDiv3")
    if output[-1] in ["0", "4", "8"]:
      out3.write("It's espresso time!")
    else:
      out3.clear()

current_time=datetime.datetime.now()
# Printing attributes of now().
print("The attributes of now() are :")
 
print("Year :", current_time.year)
 
print("Month : ", current_time.month)
 
print("Day : ", current_time.day)
 
print("Hour : ", current_time.hour)
 
print("Minute : ", current_time.minute)
 
print("Second :", current_time.second)
 
print("Microsecond :", current_time.microsecond)

def clock():
    while True:
        print(datetime.datetime.now().strftime("%D/%m/%Y %H:%M:%S"), end="\r")
        output = datetime.datetime.now().strftime("%D/%m/%Y %H:%M:%S")
        time.sleep(1)

output = datetime.datetime.now().strftime("%D/%m/%Y %H:%M:%S")
print(int(output[-1]))

clock()