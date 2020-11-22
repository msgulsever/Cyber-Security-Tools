#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORLDLIST OLUSTUR")
print("""
Wordlist olusturma aracina hosgeldin



""")

minimum = raw_input("minimum karakter sayisini girin: ")
maximum = raw_input("maximum karakter sayisini girin: ")
karakter = raw_input("Istediginiz Karakteri girin: ")
kayityeri = raw_input("Kaydedilecek yeri secin: ")

os.system("crunch " + minimum + " " + maximum + " " + karakter)
print("Basariyla kayit edildi")