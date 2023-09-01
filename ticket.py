#automatic traffic ticket imposer
import random
import time

while True:
    
    s = random.uniform(0,200)
    if s <= 70:
        print (":-)")
    elif s > 70:
        print("Caught in 4k going ", s , " in a 70")
        ticket = s*15
        print("Traffic ticket ", ticket)
        time.sleep(random.uniform(0, 5))
