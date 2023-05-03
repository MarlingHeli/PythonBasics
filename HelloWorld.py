import time #for time delay
import sys #for standard out

def type(string):
#Prints letters one by one
    for c in string: #for each character in the argument
        sys.stdout.write(c) #display text
        #sys.stdout.flush() immediately prints to console without output buffering
        time.sleep(0.1)
        
type("\nHello, world!\n")
time.sleep(0.2)
type("\nI love programming :)")
time.sleep(0.5)
