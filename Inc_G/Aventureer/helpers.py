import time
import sys

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("\n")
def dprintf(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write("\n")
# this defines the color codes for the text
# by samat-jain on stackoverflow
