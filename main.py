import requests
from colorama import Fore
fh=open("URL.txt","r")
websites=[]
for each in fh.readlines():
 websites.append(each.strip("\n"))
print websites
for i in websites:
 try:
 r=requests.get("http://"+i,timeout=5,verify=False)
 print (Fore.GREEN+"Alive Endpoint:"+" "+i)
 except:
 print (Fore.RED+"Something went wrong:"+" "+i)
fh.close()
print "<----Scan completed---->"
