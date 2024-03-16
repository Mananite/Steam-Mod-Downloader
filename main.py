import re, os, time
 
print("""
███████╗████████╗███████╗ █████╗ ███╗   ███╗	███╗   ███╗ ██████╗ ██████╗		 ██████╗  ██████╗ ██╗	██╗███╗   ██╗██╗	  ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║	████╗ ████║██╔═══██╗██╔══██╗	██╔══██╗██╔═══██╗██║	██║████╗  ██║██║	 ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗   ██║   █████╗  ███████║██╔████╔██║	██╔████╔██║██║   ██║██║  ██║	██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║	 ██║   ██║███████║██║  ██║█████╗  ██████╔╝
╚════██║   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║	██║╚██╔╝██║██║   ██║██║  ██║	██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║	 ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
███████║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║	██║ ╚═╝ ██║╚██████╔╝██████╔╝	██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝	 ╚═╝	╚═╝	 ╚═╝ ╚═════╝ ╚═════╝	 ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝	 
			  
█░█░█ █ █▀█
▀▄▀▄▀ █ █▀▀
""")

placeholder_app_id = 0
app_id = 0
mods = []

with open("mods.txt","r+") as f:
	lines = f.readlines()
		
	for i in range(len(lines)):

		if not lines[i].startswith("https://steamcommunity.com/sharedfiles"):
			pass

		if lines[i].startswith("https://steamcommunity.com/workshop/browse/"):
			app_id: re.search(r'\bappid=(\d+)+',str(lines[i]))
			print(app_id)

			if app_id != placeholder_app_id and placeholder_app_id != 0:
				print("This doesnt support multiple games, go into the code and change stuff if you want to support it and make a fork, exiting")
				time.sleep("15")
				os.system("exit")
			
			placeholder_app_id = app_id
			continue

		only_number = re.search(r"\bid=(\d+)",str(lines[i]))
		mods.append(str(only_number))
		

if app_id == 0 or None:
	app_id = str(input("Appid: "))


if os.path.exists("q.txt"): #mostly a just in case tbh
  os.remove("q.txt")
  

with open("q.txt","w+") as f:
	f.write("login anonymous")
	f.write("\n")
	for i in range(len(mods)+1):
		f.write(f"workshop_download_item " f"{app_id} {mods[i-1]}")
		f.write("\n")
	f.write("exit")
	f.close()


os.system("steamcmd.exe +runscript q.txt +stop")
os.remove("q.txt") #doesnt actually work since steamcmd wont close
