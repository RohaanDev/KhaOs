# KhaOs

A tiny custom shell built from scratch in Python, made for learning how terminals actually work.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat)
![Version](https://img.shields.io/badge/Version-0.1-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## About

KhaOs is a minimal command shell written in Python. It has its own set of built in commands, but if it doesn't recognize something you type, it just passes it along to your system shell. So it works a bit like a real terminal while staying simple enough to read the whole source file in one sitting.

The point of this project isn't to replace bash or cmd. It's to understand how shells, command dispatch, and basic OS level operations work by building one from the ground up.

## Features

- Run Python, JavaScript, C, and C++ programs
- Built in text editor
- Navigate, move, and delete files
- Download files from a URL
- Print a directory tree
- Wi-Fi utilities (scan, connect, disconnect, check IP)
- Live system info (CPU, RAM, disk, battery)
- Load external Python files as new commands at runtime
- Built in calculator
- Games list (Snake included)
- Falls back to the real system shell for anything it doesn't recognize

## Requirements

| Requirement | Needed for |
|---|---|
| Python 3.10+ | Core shell |
| art | ASCII banner |
| psutil | sysinfo command |
| pywifi | wifi command |
| Node.js (optional) | Running .js files |
| GCC (optional) | Running .c files |
| G++ (optional) | Running .cpp files |
| Git (optional) | forge command |

Note: parts of the wifi command rely on netsh which is Windows only. So right now KhaOs is really built and tested for Windows.

## Installation

Clone the repository:

```bash
git clone https://github.com/RohaanDev/KhaOs.git
cd KhaOs
```

Install dependencies:

```bash
pip install art psutil pywifi
```

Run it:

```bash
python khaos.py
```

## Usage

Once it's running you'll see the banner and the prompt:

```
khaOs>>
```

Type a command and hit enter. Anything that isn't one of KhaOs's built in commands gets passed straight to your system shell.

## Command reference

| Command | Usage | Description |
|---|---|---|
| help | help | List all available commands |
| ver | ver | Show the current KhaOs version |
| hello | hello | Print a welcome message |
| run | run <file> | Run a .py .js .c or .cpp file |
| edit | edit <file> | Open the built in text editor (type :sv to save and exit) |
| leo | leo <file> | Print the contents of a file |
| install | install <url> | Download a file from a URL |
| search | search <folder> | Print a folder as a directory tree |
| move | move <file> <folder> | Move a file into a target folder |
| cd | cd <folder> | Change the current directory |
| crd | crd | Print the current working directory |
| rv | rv <file> | Delete a file |
| calc | calc <expression> | Evaluate a math expression |
| load | load <file.py> | Load a Python file's commands into KhaOs at runtime |
| game | game | List available games |
| fc | fc | List files in the current directory |
| ress | ress <text> | Print back the given text |
| clear | clear | Clear the screen and reprint the banner |
| sysinfo | sysinfo | Show live CPU RAM disk and battery usage |
| forge | forge <repo-url> | Clone a git repository |
| wifi | wifi <sub-command> | Wi-Fi utilities, see below |
| exit | exit | Exit KhaOs |

### wifi sub-commands

| Sub-command | Description |
|---|---|
| wifi help | Show wifi command help |
| wifi scan | Scan for nearby networks |
| wifi current | Show the currently connected SSID |
| wifi connect "<SSID>" | Connect to a network by name |
| wifi disconnect | Disconnect from the current network |
| wifi ip | Show your current local IP address |

## Examples

```bash
khaOs>> help
khaOs>> crd
khaOs>> cd Projects
khaOs>> edit hello.py
khaOs>> run hello.py
khaOs>> calc 5 * 12
khaOs>> sysinfo
khaOs>> wifi scan
khaOs>> exit
```

Supported file types for run: .py .js .c .cpp

## Known limitations
- wifi current and wifi connect shell out to netsh so those two are Windows only for now.
- install downloads to the current directory using the file's original name. It doesn't check file type or size.
- This is an early build (v0.1) so expect some rough edges.


## Contributing

This started as a personal learning project but suggestions issues and pull requests are welcome. Feel free to fork it and mess around.

## License

Licensed under the MIT License.
