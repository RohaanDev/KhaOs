import os
import art
import urllib.request
import subprocess
import importlib.util
import shutil
import time
import psutil
import socket
import pywifi
import time
from pywifi import const
COMMANDS = {}
GAMES = {"Snake" : "snake.py"}
def wifi(args):
     if args[0] == "help":
         print("""
WiFi Commands
-------------
wifi help
wifi scan
wifi current
wifi connect "<SSID>" 
wifi disconnect
wifi ip
""")
     elif args[0] == "scan":
          wifi  = pywifi.PyWiFi()
          iface = wifi.interfaces()[0]
          iface.scan()
          time.sleep(4)
          for network in iface.scan_results():
               print(network.ssid)
     elif args[0] =="current":
          current_wifi = subprocess.check_output("netsh wlan show interfaces",
                                                 shell=True,
                                                 text=True)
          for line in current_wifi.splitlines():
               if "SSID" in line and "BSSID" not in line:
                    print(line.split(":",1)[1].strip())
                    break
     elif args[0] == "ip":
          s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
          s.connect(("8.8.8.8", 80))
          print("IP:", s.getsockname()[0])
          s.close()
     elif args[0] == "disconnect":
         
          wifi  = pywifi.PyWiFi()
          iface = wifi.interfaces()[0]
          iface.disconnect()
          time.sleep(3)
          print("WIFI DISCONNECTED") 
     elif args[0] == "connect":
         ssid = args[1]
         wifi = pywifi.PyWiFi()
         iface = wifi.interfaces()[0]
         subprocess.run(f"netsh wlan connect name={ssid}",shell=True)
 
 
       
           

          

          
def register(name, func):
    COMMANDS[name] = func
register("wifi",wifi)
def sysinfo(args):
     print("||KHA OS SYSTEM MANAGER||")
     print(f"CPU:{psutil.cpu_percent(interval=1)}%")
     print(f"RAM:{psutil.virtual_memory().percent}%")
     print(f"Disk:{psutil.disk_usage("/").percent}%")
     try:
        print(f"Battery{psutil.sensors_battery().percent}%")
     except:
        print("NO BATTERY FOUND")
     
register("sysinfo",sysinfo)
def run(args):
    target = args[0]
    if not os.path.exists(target):
        print("File not found")
        return 
    ext = os.path.splitext(target)[1]
    if ext == ".py":
        time.sleep(0.55)
        print (f"running" , target)
        try:
            subprocess.run(["python", target])
        except:
            subprocess.run(["python3", target])
    elif ext == ".js":
        subprocess.run(["node", target])
    elif ext == ".c":
        output = "a.out"
        subprocess.run(["gcc", target, "-o", output])
        subprocess.run([f"./{output}"])
    elif ext == ".cpp":
        output = "a.out"
        subprocess.run(["g++", target, "-o", output])
        subprocess.run([f"./{output}"])
    else:
        print("file type not supported")
register("run", run)
def edit(args):
    filename = args[0]

    print("Enter text. Type :sv to save and exit.")

    lines = []

    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.read().splitlines()
            for line in lines:
                print(line)

    while True:
        line = input()

        if line == ":sv":
            break

        lines.append(line)

    with open(filename, "w") as f:
        f.write("\n".join(lines))

    print("Saved.")
	
register("edit", edit)
def ver(args):
	print("KhaOs 0.1")
register("ver",ver)
def leo(args):
	with open(args[0], "r") as f:
		print(f.read())
register("leo",leo)
def prompt():
    return "\033[37mkhaOs\033[0m\033[36m>>\033[0m "
def execute(name, args):
    func = COMMANDS.get(name)
    if func:
        return func(args)
    print("unknown command")
art.tprint("KhaOs")
def install(args):
    url = args[0]
    name = url.split("/")[-1]

    urllib.request.urlretrieve(url, name)
    print("Installed:", name)
register("install", install)
def search(args):
    path = args[0]
    for root, dirs, files in os.walk(path):
        depth = root[len(path):].count(os.sep)
        indent = "  " * depth
        print(indent + root + "/")
        for d in sorted(dirs):
            print(indent + "  ├── " + d)
        for i, f in enumerate(sorted(files)):
            if i == len(files) - 1:
                print(indent + "  └── " + f)
            else:
                print(indent + "  ├── " + f)

def game(args):
	for i in GAMES:
		print(i)
def calc(args):
	print(eval(args[0]))
register("calc",calc)
register("game", game)
def forge(args):
     subprocess.run(["git","clone",args[0]])
register("forge",forge)
def load_command(filepath):
    name = os.path.splitext(os.path.basename(filepath))[0]
    spec = importlib.util.spec_from_file_location(name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
register("load", load_command)
def move(args):
    src = args[0]
    dst_folder = args[1]
    if not os.path.exists(src):
        print("File not found")
        return
    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder, exist_ok=True)
    dst = os.path.join(dst_folder, os.path.basename(src))
    if os.path.exists(dst):
        print("KhaOs: destination file already exists")
        return
    shutil.move(src, dst)
    print("Moved:", dst)
register("move", move)
def hello(args):
    print("Welcome To KhaOs")
register("search", search)
register("hello", hello)
def crd(args):
	print(os.getcwd())
register("crd" , crd)
def cd(args):
	os.chdir(args[0])
register("cd" , cd)
def rv(args):
	os.remove(args[0])
register("rv" , rv)
def clear(args):
    try:
        os.system("clear")
    except:
        print("\n" * 50)

    print("\033c", end="")
    art.tprint("KhaOs")
def fc(args):
     for item in os.listdir():
          print(item)
register("fc", fc)
register("clear", clear)
def help(args):
	for i in COMMANDS:
		print(i)      
register("help",help)		
def ressentir(args):
	print(" ".join(args))
register ("ress", ressentir)
while True:
    cmd = input(prompt()).strip()
    parts = cmd.split()
    try:
        if not parts:
            continue
        if cmd == "exit":
            break
        
        if parts[0] in COMMANDS:
            execute(parts[0], parts[1:] )
            continue
        else:
            subprocess.run(parts)
            continue
    except FileNotFoundError as e:
        print("KhaOs:", e)
    except IndexError as e:
        print("KhaOs:", e)
    except Exception as e:
        print("KhaOs: " , e)
print("COMMANDS:", COMMANDS.keys())

