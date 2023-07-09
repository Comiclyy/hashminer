import hashlib
import random
import string
import requests
import colorama
from colorama import *
import time
from modules import timex

def start():
    print(Fore.LIGHTBLACK_EX + f"[{int(time.time())}] {Fore.LIGHTGREEN_EX}{Style.BRIGHT}System init call recived...")
    timex.wait(3)
    
start()