import time
import winsound

def timer(min, sec):
    total_secs = min*60 + sec
    while total_secs >= 0:
        m, s = divmod(total_secs, 60)
        timer = f"{m:02d}:{s:02d}"
        print(timer, end = "\r")
        time.sleep(1)
        total_secs -= 1

    print("\nTime's up!")
    winsound.Beep(1000, 1000) 
    
print("\nCountdown Timer")
try:
    m = int(input("Enter minutes:"))
    s = int(input("Enter seconds:"))
    timer(m, s)
except ValueError:
    print("Please enter valid numbers.")

input("Press enter to exit.")
