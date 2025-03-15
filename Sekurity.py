#!/usr/bin/env python3.10
# Coded by audaz#0001

import os
import time
import socket
import ctypes
import requests
from pprint import pprint
from requests import get

host = socket.gethostname()
IPv4 = get('https://api.ipify.org/').text
IPv6 = get('https://api64.ipify.org/').text
IPsearch = "http://ip-api.com/json/" + IPv4 + "?fields=status,message,continent,continentCode,country,countryCode," \
                                              "region,regionName,city,district,zip,lat,lon,timezone,offset,currency," \
                                              "isp,org,as,asname,reverse,mobile,proxy,hosting,query"


def selection():
    print('''
     [ 1 ] - My IP Info
     [ 2 ] - Lookup IP/
     [ 3 ] - Ping IP
     [ 4 ] - Quit
    ''')


def logo():
    print('''\033[0m\033[31m
  ██████ ▓█████  ██ ▄█▀ █    ██  ██▀███   ██▓▄▄▄█████▓▓██   ██▓
▒██    ▒ ▓█   ▀  ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
░ ▓██▄   ▒███   ▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░  ▒██ ██░
  ▒   ██▒▒▓█  ▄ ▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░██░░ ▓██▓ ░   ░ ▐██▓░
▒██████▒▒░▒████▒▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒░██░  ▒██▒ ░   ░ ██▒▓░
▒ ▒▓▒ ▒ ░░░ ▒░ ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓    ▒ ░░      ██▒▒▒ 
░ ░▒  ░ ░ ░ ░  ░░ ░▒ ▒░░░▒░ ░ ░   ░▒ ░ ▒░ ▒ ░    ░     ▓██ ░▒░ 
░  ░  ░     ░   ░ ░░ ░  ░░░ ░ ░   ░░   ░  ▒ ░  ░       ▒ ▒ ░░  
      ░     ░  ░░  ░      ░        ░      ░            ░ ░     
                                                       ░ ░     \033[0m
                   By : \033[31maudaz#0001 - https://github.com/audaz-AZ\033[0m''')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def YourIP():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - Informacion de tu IP"), cls()
    except:
        cls()
        pass
    r = requests.get(IPsearch)
    print("""\033[0m\033[31m
 _____ _   _ ______ _____     
|_   _| \ | ||  ___|  _  |  _ 
  | | |  \| || |_  | | | | (_)
  | | | . ` ||  _| | | | |    
 _| |_| |\  || |   \ \_/ /  _ 
 \___/\_| \_/\_|    \___/  (_)\033[0m
    """)
    print("\033[31m"), print("  IPv4 : " + IPv4 + "\033[0m")
    print("\033[31m"), print("  IPv6 : " + IPv6 + "\033[0m")
    print(""), pprint(r.json())
    print(""), input("  Pulsa enter para continuar"), menu()


def searchdata():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - Ping IP/URL"), cls(), print("")
    except:
        cls(), print("")
        pass
    x = input("  \033[0m\033[31mEnter IP/URL\033[0m : ")
    if x == '':
        cls(), print(""), print("\033[0m\033[31m  Direccion Invalida\033[0m"), time.sleep(0.5), searchdata(), print("")
    print("""\033[0m\033[31m
 _____ _   _ ______ _____     
|_   _| \ | ||  ___|  _  |  _ 
  | | |  \| || |_  | | | | (_)
  | | | . ` ||  _| | | | |    
 _| |_| |\  || |   \ \_/ /  _ 
 \___/\_| \_/\_|    \___/  (_)\033[0m
    """)
    print("")
    y = "http://ip-api.com/json/" + x + "?fields=status,message,continent,continentCode,country,countryCode," \
                                        "region,regionName,city,district,zip,lat,lon,timezone,offset,currency," \
                                        "isp,org,as,asname,reverse,mobile,proxy,hosting,query"

    x = requests.get(y)
    pprint(x.json())

    print(""), print("")
    while True:
        print(""), print("""\033[31m  Run again?\033[0m \033[32mY\033[0m or \033[32mN\033[0m (Default=N)"""), print("")
        choice = input("\033[31mroot\033[0m@" + "\033[32m" + host + "\033[0m" + ":~$ ").lower()
        if choice == 'y' and 'Y':
            searchdata()
        elif choice == 'n' and 'N':
            menu()
        elif choice == '':
            menu()
        else:
            cls(), print(""), print("\033[0m\033[31m  Invalid Option\033[0m"), time.sleep(0.5), cls()


def Ping():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - Ping IP/URL"), cls(), print("")
    except:
        cls(), print("")
        pass

    x = input("  \033[31mEscribe la IP/URL\033[0m : ")
    if x == '':
        cls(), print(""), print("\033[31m  Direccion Invalida\033[0m"), time.sleep(0.5), Ping(), print(""), "\033[31m"
    os.system('start cmd.exe @cmd /k "mode con:cols=60 lines=55 & color 9 &" ping -t ' + x if os.name == 'nt' else
              'gnome-terminal -- bash -c "ping ' + x + '"')


def menu():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - Menu"), cls(), print("")
    except:
        pass
    while True:
        cls()
        logo()
        selection()
        choice = input("\033[31mroot\033[0m@" + "\033[32m" + host + "\033[0m" + ":~$ ").lower()
        if choice == '1':
            YourIP()
        elif choice == '2':
            searchdata()
        elif choice == '3':
            Ping()
        elif choice == '4':
            cls()
            print("\033[31m Cerrando la Tool - Desarrollado por audaz.\033[0m")
            time.sleep(0.5)
            exit()


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        cls(), print(""), print("\033[31m  ERROR\033[0m : KeyboardInterrupt (ctrl+c)")
        exit()
    except:
        cls(), print(""), print("\033[31m  ERROR\033[0m : % (ctrl+c)")
        exit()
