import sys
import argparse
import os
import socket
import sys
import json
import random
import threading
import math
import base64
import time
from sys import argv
from getpass import getpass
from xml.dom import minidom
from time import gmtime, strftime, sleep

def yesOrNo():
    return (raw_input("Devam et Y / N: ") in yes)

tulpanerlogo = """

 ######## ##     ## ##       ########     ###    ##    ## ######## ########
    ##    ##     ## ##       ##     ##   ## ##   ###   ## ##       ##     ##
    ##    ##     ## ##       ##     ##  ##   ##  ####  ## ##       ##     ##
    ##    ##     ## ##       ########  ##     ## ## ## ## ######   ########
    ##    ##     ## ##       ##        ######### ##  #### ##       ##   ##
    ##    ##     ## ##       ##        ##     ## ##   ### ##       ##    ##
    ##     #######  ######## ##        ##     ## ##    ## ######## ##     ##






"""

class tulpaner:
    def __init__(self):
        print (tulpanerlogo + '''
             }-----{+} Made with LOVE by kutaygs =) {+}-----{
            }--------{+} kutayyavuz03@hotmail.com {+}--------{
         }-----{+} Program python dilinde yapilmistir. {+}-----{
  ''' '''
             {1}--Giris
             {9}-Cikis\n

             ''')
        choice1 = raw_input("tulpaner~# ")
        if choice1 == "1":
            secim()
        elif choice == "9":
            sys.exit()
        else:
            print("Hatali Giris")
            self.__init__()
        self.completed()

    def completed(self):
        print("Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()

def ftok():
    f = float(input("  Ferenheit Giriniz : "))
    c = (5 * (f - 32)) / 9
    k = c +273
    print (round(k, 1))
    print ("Kelvin")
    print('''
    {9}--Cikis\n''')
    choice = raw_input('tulpaner~# ')
    if choice == '9':
        secim()

def ctof():
    c = float(input('  Celsius Giriniz : '))
    f = ((9 * c) / 5) + 32
    k = c + 273
    print (round(f, 1))
    print ("Fahrenheit")
    print('''
    {9}--Cikis\n''')
    choice = raw_input('tulpaner~# ')
    if choice == '9':
        secim()

def ktoc():
    k = float(input('  Kelvin Giriniz : '))
    c = k + 273
    f = ((9 * c) / 5) + 32
    print (round(c, 1))
    print ("Celsius")
    print('''
    {9}--Cikis\n''')
    choice = raw_input('tulpaner~# ')
    if choice == '9':
        secim()



class secim:
    def __init__(self):
        print (tulpanerlogo)
        print("   Cevirmek istediginiz birimi girin!")
        print("   {1}--Kelvin to Celsius")
        print("   {2}--Celsius to Fahrenheit")
        print("   {3}--Fahrenheit to Kelvin")
        print("   {9}-Ana Menuye Git\n")
        print("")
        print("")
        print("")
        choice4 = raw_input("tulpaner~# ")
        if choice4 == "1":
            ktoc()
        elif choice4 == "2":
            ctof()
        elif choice4 == "3":
            ftok()
        elif choice4 == "9":
            tulpaner()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        print("Tamamlandi, geri donmek icin tiklayiniz")
        self.__init__()

if __name__ == "__main__":
    try:
        tulpaner()
    except KeyboardInterrupt:
        print(
        """
Yukleniyor, lutfen bekleyiniz...
<Eger 3 dakika icinde acilmazsa silip bir daha yukleyin...>\r"""
            ),
        time.sleep(100)
