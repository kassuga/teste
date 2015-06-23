import time
import datetime as dt 

def count(seconds):
    for sec in range(seconds):
        print sec + 1
        time.sleep(1)


def count_slow(seconds_slow):
    for sec in range(seconds_slow):
        print sec + 1
        time.sleep(1.5)