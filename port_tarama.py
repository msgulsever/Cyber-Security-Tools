#!/usr/bin/env python

import os


os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""Port Tarama Aracina hos geldiniz : )

1) Hizli tarama
2) Servis ve Versiyon bilgisi
3) Isletim Sistemi Bilgisi

""")

islemno = raw_input("islemn numarasini girin: ")

if(islemno=="1"):
	hedefip=raw_input("hedef Ip Girin: ")
	os.system("nmap " +hedefip)
elif(islemno=="2"):
	hedefip=raw_input("Hedef Ip Girin: ")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
	hedefip=raw_input("hedef Ip Girin: ")
	os.system("nmap -0 " +hedefip)
else:
	print(" hatali secim")
	
	
