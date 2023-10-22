import requests
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m ██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GET ID FACEBOOK & NGÀY TẠO ACC
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mAN ORIN
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31manorintool
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/g/dpfbxq529
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://youtube.com/@AnOrinTool403
\033[1;31m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()
id = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập ID Facebook: ")
cookies = {
    '__cf_bm': 'hCJ70.qlLOmLP4yNJ3T.jU8U_gfpcDM3yKeSq.apXTo-1680193382-0-AXRqj+GxSV8cBESQDO9SQMjV7H0A2R+tRrgVFIKA5xekIcDlqHBeZ4so6MN6pXK4GMo+0TIMns5G6wo8qZaq9BJnZAjfOAUGUQUyQqraD29vAUXcHAcOFGMeb6X0xovVdQ==',
}

headers = {
    'authority': 'golike.com.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': '__cf_bm=hCJ70.qlLOmLP4yNJ3T.jU8U_gfpcDM3yKeSq.apXTo-1680193382-0-AXRqj+GxSV8cBESQDO9SQMjV7H0A2R+tRrgVFIKA5xekIcDlqHBeZ4so6MN6pXK4GMo+0TIMns5G6wo8qZaq9BJnZAjfOAUGUQUyQqraD29vAUXcHAcOFGMeb6X0xovVdQ==',
    'referer': 'https://golike.com.vn/lay-uid-va-kiem-tra-ngay-tao-tai-khoan-facebook/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'user': id,
}

response = requests.get('https://golike.com.vn/func-api.php', params=params, cookies=cookies, headers=headers).json()
getuid = response["data"]["uid"]
gettime = response["data"]["date"]
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32muid: "+getuid)
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mtime: "+gettime)