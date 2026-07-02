A small terminal written in Python.

KhaOs is a simple shell made for learning how terminals work. It has its own built in commands but can also run normal system commands when a command is not found.
The goal of this project is to understand how operating systems and shells work by building one from scratch.

Current version 0.1

Features:
Run Python JavaScript C and C++ programs
Built in text editor
Change directories
View the current directory
Move files
Delete files
Download files from the internet
Browse folders
Load Python modules
Calculator
Clear the screen
Built in help command
Requirements
Python 3.10 or newer
art Python package

Optional

Node.js for JavaScript
GCC for C
G++ for C++
Installation

Clone the repository

git clone https://github.com/RohaanDev/KhaOs.git
cd KhaOs

Install the required package

pip install art

Run KhaOs

python khaos.py
Commands
help              Show all commands
ver               Show version
hello             Welcome message
run file.py       Run a program
edit file.txt     Edit a file
leo file.txt      Read a file
install URL       Download a file
search folder     Show folders and files
move file folder  Move a file
cd folder         Change directory
crd               Show current directory
rv file           Delete a file
calc expression   Calculate an expression
load plugin.py    Load a Python module
game              Show games
ress text         Print text
clear             Clear the screen
exit              Exit KhaOs
Supported files
.py
.js
.c
.cpp
Examples:
khaOs>> help

khaOs>> crd

khaOs>> cd Projects

khaOs>> edit hello.py

khaOs>> run hello.py

khaOs>> calc 5 * 12

khaOs>> exit
About:
    It is a personal project made to learn how shells work and to experiment with building command line tools in Python.
    More features will be added over time.
