import time
import datetime as dt 

def count(seconds):
    for sec in range(seconds):
        print sec + 1
        time.sleep(1)
