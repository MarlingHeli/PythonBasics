import time
import sys

def type(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        
type("\nHello, world!\n")
time.sleep(0.2)
type("\nI love programming :)")
time.sleep(0.2)
