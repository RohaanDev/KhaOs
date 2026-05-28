import os
import art
import urllib.request
import subprocess
import importlib.util

COMMANDS = {}
def register(name , func):
		COMMANDS[name] = func 
def run(target):
	if not os.path.exists(target):
		print ("File not found")
		return 
	ext = os.path.splitext(target)[1]
	if ext == ".py":
		subprocess.run(["python" , target])
	elif ext == ".js":
		subprocess.run(["node" , target])
	elif ext == ".c":
		output = "a.out"
		subprocess.run(["gcc"
		, target ,
		"-o"
		, output])
		subprocess.run([f"./{output}"])
	elif ext == ".cpp":
		output= "a.out"
		subprocess.run(["g++" ,
		target
		, "-o" 
		, output])
		subprocess.run([f"./{output}"])
	else:
		print ("file type not supported")
register ("run" , run)
def prompt():
    return "\033[37mkhaOs\033[0m\033[36m>>\033[0m "
	
def execute(name , args):
		func = COMMANDS.get(name)
		if func:
			return func(args)
		print ("unknown command")
		print ("unknown commands")
art.tprint("KhaOs")
def install(url):
	name = url.split("/")[-1].replace(".git" , "")
	subprocess.run(["git" , "clone" , url , name])
register ("install" , install)
	
def search(path):
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

def load_command(filepath):
    name = os.path.splitext(os.path.basename(filepath))[0]

    spec = importlib.util.spec_from_file_location(name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
register("load" , load_command)
def handle_command(parts):
    subprocess.run(parts)
    return True
def hello(args):
	print ("Welcome To KhaOs")
register ("search" , search)
register ("hello" , hello)
while True:
	cmd = input(prompt()).strip().lower()
	parts = cmd.split()
	
	if not parts:
		continue 
	if cmd == "exit":
		break
	if parts[0] in COMMANDS:
		execute(parts[0] , parts [1])
		continue 
	else:
		subprocess.run(parts)
	
		
	
