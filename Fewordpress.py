#!/usr/bin/env python 
  
 import os 
  
 os.system("apt-get install figlet") 
 os.system("clear") 
 os.system("figlet bhecy") 
 os.system("figlet wordpress tarama") 
  
 print(""" 
  
 wordpress tarama aracına hoş geldin... 
  
 1) hızlı tarama 
 2) eklenti tarama 
 3) tema tarama 
 4) yönetici kullanıcı adı tarama 
  
 """) 
  
 islemno=input("işlem numarası giriniz : ") 
  
 if islemno=="1" 
         site=input("site adresi : ") 
         os.system("wpscan --url "+site) 
 elif islemno=="2" 
         site=input("site adresi : ") 
         os.system("wpscan --url "+site+" --enumerate p") 
 elif islemno=="3" 
         site=input("site adresi : ") 
         os.system("wpscan --url "+site+" --enumerate t") 
 elif islemno=="2" 
         site=input("site adresi : ") 
         os.system("wpscan --url "+site+" --enumerate u") 
 else: 
         print("yanlış seçim, program kapandı...") 
  
 
