import re, os, requests, time
from bs4 import BeautifulSoup
 
mods = []
app_id = []
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

with open("mods.txt","r+") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        only_number = re.search(r'\d+',str(lines[i])).group()
        mods.append(only_number)


for i in range(len(lines)):
  soup = BeautifulSoup(requests.get(lines[i], headers).content,"html.parser")
  for link in soup.find_all('a'):
    y=link.get('href')
    if "https://steamcommunity.com/app/" in y:
      only_number = re.search(r'\d+',str(y)).group()
      app_id.append(only_number)
      print(app_id)
      break


if os.path.exists("q.txt"): #mostly a just in case tbh
  os.remove("q.txt")

  
if len(mods) != len(app_id):
  print("Something went terribly wrong and the number of mods differs with the number of games")
  time.sleep(4)
  exit()


with open("q.txt","w+") as f:
    f.write("login anonymous")
    f.write("\n")
    for i in range(len(mods)):
        f.write(f"workshop_download_item " f"{app_id[i-1]} {mods[i-1]}")
        f.write("\n")
    f.close()  


os.system("steamcmd.exe +runscript q.txt")
os.remove("q.txt")
os.system("exit")