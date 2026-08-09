import threading
import time

# import time will help to understand the multithreading
# Multithreading: run multiple threads concurrently in one process (shared memory).
# Good for I/O-bound tasks (network/disk waits)
# the structure to create a thread is: thread = threading.Thread(target=function, args=(...), kwargs={...})
# to begin running of the thread: thread.start()


def make_sum_operation(x, y):
    time.sleep(2) # it will take 8 seconds for making sum operation 
    print(f"the sum is: {x + y}")

def playing_chess():
    time.sleep(8) # it will take 8 seconds for playing chess
    print("you have finished playing chess")
    
def shopping():
    time.sleep(5)  # it will take 8 seconds for shopping
    print("you have finished the daily shopping")    
    
def hang_out():
    time.sleep(15)  # it will take 8 seconds for hanging out
    print("the hanging out is done")    
    

# creating multithread of my daily works and start running it     

work1 = threading.Thread(target=make_sum_operation, args=(190, 170))
work1.start()    

work2 = threading.Thread(target=playing_chess)
work2.start()  

work3 = threading.Thread(target=shopping)
work3.start()  

work4 = threading.Thread(target=hang_out)
work4.start()  