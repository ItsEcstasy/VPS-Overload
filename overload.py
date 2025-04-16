from os import system
import time, threading

def thread_function(name):
    while True:
        x = threading.Thread(target=thread_function, args=(50,))
        x.start()

time.sleep(1)
print("\x1b[92mSuccessfully \x1b[31mbricked server\x1b[0m")
exit()
