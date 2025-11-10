# The Picofetch Authors, 2025
# (chromium ahh)
import os
import platform
import socket
from datetime import datetime
import subprocess

class Colours:
    RESET = '\033[0m'
    BOLD = '\033\1m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    BLUE = '\033[34m'

def get_upt(): # uptime
    try:
        with open('/proc/uptime', 'r') as f:
            upt_seconds = float(f.readline().split()[0])
            days = int(upt_seconds // 86400)
            hours = int((upt_seconds % 86400) // 3600)
            minutes = int((upt_seconds % 3600) // 60)
            return f"{days}d {hours}h {minutes}m"
    except:
        return "unknown" # this hopefully shouldn't happen on most systems

def get_cpu():
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'model name' in line:
                    return line.split(':')[1].strip()
    except:
        return platform.processor() or "unknown"

def get_cpu_count():
    try:
        with open('/proc/cpuinfo', 'r') as f:
            return len([line for line in f if line.startswith('processor')])
    except:
        return "unknown"

def get_mem():
    try:
        with open('/proc/meminfo', 'r') as f:
            lines = f.readlines()
            total = int(lines[0].split()[1]) / 1024
            available = int(lines[2].split()[1]) /1024
            used =total-available
            return f"{used:.0f}MiB/{total:.0f}MiB"
    except:
        return "unknown" # this also probably shouldn't happen

def get_disk_usg():
    try:
        stat =  os.statvfs('/')
        total = (stat.f_blocks * stat.f_frsize) / (1024**3)
        free = (stat.f_bfree * stat.f_frsize) / (1024**3)
        used = total- free
        return f"{used:.1f}G / {total:.1f}G ({int((used/total)*100)}%)"
    except:
        return "unknown"

def get_shell():
    shell = os.environ.get('SHELL', 'unknown')
    return os.path.basename(shell)

def get_pkgs():
    pass

def get_res():
    try:
        result = subprocess.run(['xrandr'], capture_output=True, text=True, timeout=2)
        for line in result.stdout.split('\n'):
            if '*' in line:
                res = line.split()[0]
                return res
    except:
        pass
    return "unknown" 

def get_wm():
    de = os.environ.get('XDG_CURRENT_DESKTOP', '')
    wm = os.environ.get('DESKTOP_SESSION', '')
    if de:
        return de
    elif wm:
        return wm
    return "unknown"

ascii_art = [
    "        @@@@@@@@@      @@@@@@@@@        ",
    "      @           @  @           @      ",
    "      @    @       @@       @    @      ",
    "      @@      @@   @@   @@      @@      ",
    "       @         @@@@@@         @       ",
    "        @@@     @@@@@@@@     @@@        ",
    "          @@@@@@@@ .. @@@@@@@@          ",
    "        @@    @@ .::::. @@    @@        ",
    "       @@ . @@@@@:.....@@@@@.. @@       ",
    "       @@ @@@ ....@@@@......@@ @@       ",
    "      @@-@@ .::::: @@ ::::::.@@ @@      ",
    "     @ . @-.::::::.@@ ::::::: @ . @     ",
    "    @@.:.@@.:::::. @@@.:::::. @.:.@@    ",
    "    @@ . @@= ....@@@@@@:... @@@ . @@    ",
    "     @@ @@@@@@@@=.......@@@@@@*@ @@     ",
    "      @@ .. @@@@.::::::: @@ ... @@      ",
    "      @@ :::. @@ :::::::.@.:::: @@      ",
    "       @@.::::.@@ .....:@.::::.*@       ",
    "        @@ ... @@@@@@@@@@ ... @@        ",
    "           @@@@@ ...... @@@@@           ",
    "              @@ ...... @@              ",
    "                @@@@@@@@                "
]

username = os.environ.get('USER', 'unknown')
hostname = socket.gethostname()
os_name = f"{platform.system()} {platform.release()}"
kernel = platform.release()
upt = get_upt()
pkgs = get_pkgs()
shell = get_shell()
res = get_res()
de_wm = get_wm()
terminal = os.environ.get('TERM', 'unknown')
cpu = get_cpu()
cpu_cores = get_cpu_count()
mem = get_mem()
disk = get_disk_usg()

info_lns = [
    f"{Colours.CYAN}{username}{Colours.RESET}@{Colours.CYAN}{hostname}{Colours.RESET}",
    f"{Colours.CYAN}{'-' * (len(username) + len(hostname) + 1)}{Colours.RESET}",
    f"{Colours.CYAN}OS{Colours.RESET}: {os_name}",
    f"{Colours.CYAN}Host{Colours.RESET}: Picoducky",
    f"{Colours.CYAN}Kernel{Colours.RESET}: {kernel}",
    f"{Colours.CYAN}Uptime{Colours.RESET}: {upt}",
    f"{Colours.CYAN}Packages{Colours.RESET}: {pkgs}",
    f"{Colours.CYAN}Shell{Colours.RESET}: {shell}",
    f"{Colours.CYAN}Resolution{Colours.RESET}: {res}",
    f"{Colours.CYAN}DE{Colours.RESET}: {de_wm}",
    f"{Colours.CYAN}Terminal{Colours.RESET}: {terminal}",
    f"{Colours.CYAN}CPU{Colours.RESET}: {cpu}",
    f"{Colours.CYAN}CPU cores{Colours.RESET}: {cpu_cores}",
    f"{Colours.CYAN}Memory{Colours.RESET}: {mem}",
    f"{Colours.CYAN}Disk (/){Colours.RESET}: {disk}",
    "",
    f"{Colours.RED}███{Colours.GREEN}███{Colours.YELLOW}███{Colours.BLUE}███{Colours.MAGENTA}███{Colours.CYAN}███{Colours.RESET}"
]

print()
max_lns = max(len(ascii_art), len(info_lns))
for i in range(max_lns):
    left = ascii_art[i] if i < len(ascii_art) else " " * 26
    right = info_lns[i] if i < len(info_lns) else ""
    print(f"{left} {right}")
print()