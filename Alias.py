import os
import sys
import ctypes
import subprocess

# ===========================
# Config
# ===========================
BIN_DIR = os.path.expanduser(r"C:\bin")  # folder for batch files

# List of Linux-like commands to create
commands = {
    "ls": "dir /B %*",
    "ll": "dir /A:D %*",
    "la": "dir /A %*",
    "pwd": "cd",
    "cd": "cd %*",
    "mkdir": "mkdir %*",
    "rmdir": "rmdir /S /Q %*",
    "touch": "copy nul %*",
    "cp": "copy %*",
    "mv": "move %*",
    "rm": "del %*",
    "cat": "type %*",
    "head": "more +0 %*",
    "tail": "more %*",
    "clear": "cls",
    "echo": "echo %*",
    "env": "set",
    "stat": "dir %*",
    "find": "findstr %*",
    "nano": "notepad %*",
    "vi": "notepad %*",
    "grep": "findstr %*",
    "wc": "find /c /v \"\" %*",
    "ping": "ping %*",
    "ifconfig": "ipconfig",
    "traceroute": "tracert %*",
    "netstat": "netstat",
    "curl": "curl %*",
    "wget": "powershell Invoke-WebRequest -Uri %* -OutFile %*",
    "ps": "tasklist",
    "top": "tasklist",
    "kill": "taskkill /PID %* /F",
    "who": "echo %USERNAME%",
    "date": "date /T",
    "time": "time /T",
    "df": "wmic logicaldisk get size,freespace,caption",
    "free": "wmic OS get FreePhysicalMemory",
    "du": "dir /S /B %*",
    "lsattr": "attrib %*",
    "chmod": "echo Chmod not supported in CMD",
    "chown": "echo Chown not supported in CMD",
    "ln": "echo Symlink not supported in CMD",
    "apt": "echo Use Chocolatey: choco install %*",
    "yum": "echo Use Chocolatey: choco install %*",
    "brew": "echo Use Chocolatey: choco install %*",
    "tar": "tar -cf %*",
    "unzip": "powershell Expand-Archive -Path %* -DestinationPath .",
    "zip": "powershell Compress-Archive -Path %* -DestinationPath archive.zip",
    "man": "echo Use 'command /?' for help",
    "sleep": "timeout /T %* >nul",
    "history": "doskey /history",
    "alias": "doskey",
    "which": "where %*",
    "reboot": "shutdown /r /t 0",
    "shutdown": "shutdown /s /t 0",
    "clear": "cls",
    "exit": "exit",
    "git": "git %*",
    "gcc": "echo Install MinGW or WSL for gcc",
    "python": "python %*",
    "node": "node %*",
    "npm": "npm %*",
    "pbcopy": "clip < %*",
    "pbpaste": "powershell Get-Clipboard",
    "tree": "tree %*",
    "comp": "fc %*",
    "diff": "fc %*",
    "sort": "sort %*",
    "uniq": "echo Use 'sort | find /V' for uniqueness",
    "lsmod": "driverquery",
    "dmesg": "echo Not available in CMD"
}

# ===========================
# Function: Create batch files
# ===========================
def create_bin_dir():
    if not os.path.exists(BIN_DIR):
        os.makedirs(BIN_DIR)
        print(f"[+] Created folder: {BIN_DIR}")

def create_batch_files():
    for cmd_name, cmd_action in commands.items():
        file_path = os.path.join(BIN_DIR, f"{cmd_name}.bat")
        with open(file_path, "w") as f:
            f.write(f"@echo off\n{cmd_action}\n")
        # Optional: make executable? Not needed for .bat
    print(f"[+] Created {len(commands)} command batch files in {BIN_DIR}")

# ===========================
# Function: Add to PATH
# ===========================
def add_to_path():
    # Check if BIN_DIR is already in PATH
    current_path = os.environ.get("PATH", "")
    if BIN_DIR.lower() in current_path.lower():
        print("[*] BIN_DIR already in PATH")
        return

    # Add to User PATH via registry
    subprocess.run(f'setx PATH "%PATH%;{BIN_DIR}"', shell=True)
    print(f"[+] Added {BIN_DIR} to user PATH. Restart CMD to apply.")

# ===========================
# Main
# ===========================
def main():
    create_bin_dir()
    create_batch_files()
    add_to_path()
    print("[+] Setup complete! Open a new CMD window to use Linux commands.")

if __name__ == "__main__":
    main()
