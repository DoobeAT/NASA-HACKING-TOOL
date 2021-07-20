import os
import time

try:
 from colorama import Fore, init
except:
 os.system("py -m pip install colorama" if os.name == "nt" else "pip3 install colorama")

from colorama import Fore, init

print(f''' {Fore.RED}

 __    _  __   __  _______ 
|  |  | ||  | |  ||       |
|   |_| ||  |_|  ||_     _|
|       ||       |  |   |  
|  _    ||       |  |   |  
| | |   ||   _   |  |   |  
|_|  |__||__| |__|  |___|  

''')
time.sleep(3)

while True:
 print(f"{Fore.GREEN}HACKEANDO LA NASA")
 time.sleep(0.1)
