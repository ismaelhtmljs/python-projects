import time
import os

for i in range(5):
    print('.',end=" ",flush=True)
    time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
