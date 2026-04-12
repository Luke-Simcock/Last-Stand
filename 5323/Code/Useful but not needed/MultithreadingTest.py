import threading
import time

def brek():
    time.sleep(3)
    print("You eat brek")

def coff():
    time.sleep(4)
    print("You drink coff")

def stud():
    time.sleep(5)
    print("You stud")

x = threading.Thread(target=brek)

y = threading.Thread(target=coff)

z = threading.Thread(target=stud)

x.start()
y.start()
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate)

