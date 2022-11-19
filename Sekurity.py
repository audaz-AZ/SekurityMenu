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
     [ 2 ] - Lookup IP/URL
     [ 3 ] - Ping IP/URL
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
                   By : \033[31maudaz#0001 - @akka.huugo0\033[0m''')


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def YourIP():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - Your IP Info"), cls()
    except:
        cls()
        pass
    r = requests.get(IPsearch)
    print("""\033[0m\033[31m
       ___  ___ _________   _ 
      / _ \/ _ /_  __/ _ | (_)
     / // / __ |/ / / __ |_   
    /____/_/ |_/_/ /_/ |_(_)\033[0m
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
        cls(), print(""), print("\033[0m\033[31m  Invalid Address\033[0m"), time.sleep(0.5), searchdata(), print("")
    print("""\033[0m\033[31m
       ___  ___ _________   _ 
      / _ \/ _ /_  __/ _ | (_)
     / // / __ |/ / / __ |   
    /____/_/ |_/_/ /_/ |_| (_)\033[0m
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

    x = input("  \033[31mEnter IP/URL\033[0m : ")
    if x == '':
        cls(), print(""), print("\033[31m  Invalid Address\033[0m"), time.sleep(0.5), Ping(), print(""), "\033[31m"
    os.system('start cmd.exe @cmd /k "mode con:cols=60 lines=55 & color 9 &" ping -t ' + x if os.name == 'nt' else
              'gnome-terminal -- bash -c "ping ' + x + '"')


def YT():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Sekurity - YouTube-DL + FFmpeg"), cls(), print("")
    except:
        pass
    while True:
        cls(), print("")
        y = input("  \033[31mEnter file address\033[0m : ")
        if y == '':
            cls(), print(""), print("\033[31m  Invalid Address\033[0m"), time.sleep(0.5), YT(), print(""), "\033[31m"
        x = input("  \033[31mEnter video URL\033[0m : ")
        if x == '':
            cls(), print(""), print("\033[31m  Invalid Address\033[0m"), time.sleep(0.5), YT(), print(""), "\033[31m"
        cls()
        print("""
    \033[31mVIDEO FORMATS\033[0m              \033[31mAUDIO FORMATS\033[0m
        
    1  >  \033[32mBest\033[0m                        7   >  \033[32mBest\033[0m
    2  >  .mp4                               8   >  .mp3
    3  >  .webm                              9   >  .m4a
    4  >  .flv                               10  >  .flac
    5  >  .mkv                               11  >  .aac
    6  >  .avi                               12  >  .opus
                                             13  >  .ogg
                                             14  >  .wav
              ---< \033[32mSettings\033[0m >---
          
  15  >  \033[31mBypass geo restrictions\033[0m : NO  |  \033[32mDownload location\033[0m       : """ + y + """
                                          | 
  16  >  \033[32mUpdate Youtube-dl\033[0m       :     |  \033[31mVideo URL\033[0m               : """ + x + """
""")
        choice = input("  Enter # > ")
        if x or y == '':
            cls(), print(""), print("\033[31m  Invalid Address\033[0m"), time.sleep(0.5), YT(), print(""), "\033[31m"

        # VIDEO

        elif choice == '1':
            cls()
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --format bestvideo[ext=best]+bestaudio[ext=best]/best -o ' + y + '\%(title)s.%(ext)s ' + x)  # Best
            input()
        elif choice == '2':
            cls()
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --merge-output-format mp4 --recode-video mp4 -o ' + y + '\%(title)s.%(ext)s' + x)  # .mp4
            input()
        elif choice == '3':
            cls()
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --merge-output-format webm --recode-video webm -o ' + y + '\%(title)s.%(ext)s' + x)  # .webm
            input()
        elif choice == '4':
            cls()
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --merge-output-format flv --recode-video flv -o ' + y + '\%(title)s.%(ext)s' + x)  # .flv
            input()
        elif choice == '5':
            cls()
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --merge-output-format mkv --recode-video mkv -o ' + y + '\%(title)s.%(ext)s' + x)  # .mkv
            input()
        elif choice == '6':
            cls()
            os.system('Sekurity\Req\Sekurity\Req\youtube-dl.exe --add-metadata --merge-output-format avi --recode-video avi -o ' + y + '\%(title)s.%(ext)s' + x)  # .avi
            input()

        # AUDIO

        elif choice == '7':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --format bestaudio[ext=best]/best --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # Best
        elif choice == '8':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format mp3 --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .mp3
        elif choice == '9':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format m4a --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .m4a
        elif choice == '10':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format flac --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .flac
        elif choice == '11':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format aac --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .aac
        elif choice == '12':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format opus --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .opus
        elif choice == '13':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format ogg --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .ogg
        elif choice == '14':
            os.system('Sekurity\Req\youtube-dl.exe --add-metadata --extract-audio --audio-format wav --audio-quality 0 -o ' + y + '\%(title)s.%(ext)s ' + x)  # .wav
        elif choice == '15':
            os.system(' --geo-bypass')
        elif choice == '16':
            print("  \033[32mChecking for updates...\033[0m"), print(""), os.system("youtube-dl -U"), time.sleep(2), \
            cls(), print("")
        elif choice == '17':
            print("lol")
        menu()


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
            YT()
        elif choice == '5':
            cls(), exit()


if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        cls(), print(""), print("\033[31m  ERROR\033[0m : KeyboardInterrupt (ctrl+c)")
        exit()
    except:
        cls(), print(""), print("\033[31m  ERROR\033[0m : % (ctrl+c)")
        exit()