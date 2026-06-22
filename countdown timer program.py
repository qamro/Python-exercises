import time

my_time = int(input("Enter the time in seconds: "))
for i in range(my_time, 0, -1): #we can also use for i in reversed(range(0, my_time)):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i // 3600) #if we add the days it will be hours = (i // 3600) % 24 and if we add the years it will be hours = (i // 3600) % 8760
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is UP!!")    