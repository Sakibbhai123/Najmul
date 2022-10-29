W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
from concurrent.futures import ThreadPoolExecutor

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""    
\033[1;91m     
\033[1;93m   
 \033[1;92m 
 \033[1;91m  
\033[1;92m   
\033[1;93m 
                                     
    鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹�
    鈹� [鉁揮 AUTHOR   : SAKIB            鈹�
    鈹� [鉁揮 GITHUB   : SAKIBBHAI123         鈹�
    鈹� [鉁揮 WHATSAPP : 01316165549        鈹�
    鈹� [鉁揮 POWER BY : \x1b[1;32mSAKIB\x1b[1;97m            鈹�
    鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹榎033[1;92m""")
		print("%s [%s庐%s] %sTOOL NAME : %sOLD CLONER"%(G,R,G,Y,G))
		print("%s [%s庐%s] %sVERSION   : %s2.0 "%(G,R,G,Y,G))
		print("%s [%s庐%s] %sSTATUS    : %sF R E E"%(G,R,G,Y,G)) 
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
		print("\033[92;1m        AUTHOR : SAKIB-XD      ")
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
	
