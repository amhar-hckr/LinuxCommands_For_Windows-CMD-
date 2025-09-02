# Linux Command Aliases for Windows

This project provides a Python script (`Alias.py`) that automatically creates Windows batch files to mimic popular Linux shell commands. It helps users familiar with Linux to use similar commands in Windows Command Prompt (CMD).

## Features
- Creates a `C:\bin` directory and populates it with batch files for common Linux commands (e.g., `ls`, `cat`, `grep`, `pwd`, `cp`, `mv`, etc.).
- Each batch file translates the Linux command to its closest Windows equivalent.
- Adds `C:\bin` to the user's PATH for easy access from any CMD window.
- Supports over 80 Linux-like commands, including file operations, system info, networking, and more.

## How It Works
1. **Batch File Creation:**
	- The script creates a batch file for each command in the `C:\bin` directory.
	- Each batch file contains the Windows equivalent of the Linux command.
2. **PATH Update:**
	- The script adds `C:\bin` to the user's PATH environment variable, so you can run these commands from any CMD window.

## Usage

### 1. Run the Setup Script
Open a terminal (CMD or PowerShell) and run:
```bash
python Alias.py
```


## 2. Add to Path
1 – Add C:\bin to PATH (permanent)

Run this command in PowerShell (as Admin):

```
setx PATH "$($env:PATH);C:\bin" /M
```

✅ This will add C:\bin permanently to the system PATH.
You need to restart your terminal (close and reopen cmd/PowerShell).

### 3. Open a New CMD Window
After setup, open a new Command Prompt window. You can now use Linux-like commands such as:
```bash
ls
cat myfile.txt
pwd
cp file1.txt file2.txt
rm file.txt
```

### 3. Supported Commands
Some examples:
- `ls` → `dir /B %*`
- `cat` → `type %*`
- `grep` → `findstr %*`
- `pwd` → `cd`
- `cp` → `copy %*`
- `mv` → `move %*`
- `rm` → `del %*`
- `nano`/`vi` → `notepad %*`
- `ps`/`top` → `tasklist`
- `kill` → `taskkill /PID %* /F`
- `ifconfig` → `ipconfig`
- `wget` → `powershell Invoke-WebRequest -Uri %* -OutFile %*`
- `unzip` → `powershell Expand-Archive -Path %* -DestinationPath .`
- `zip` → `powershell Compress-Archive -Path %* -DestinationPath archive.zip`
- `man` → `echo Use 'command /?' for help`

### 4. Limitations
- Some Linux commands (e.g., `chmod`, `chown`, `ln`, `dmesg`) are not supported in Windows and will display a message.
- For package management, use [Chocolatey](https://chocolatey.org/) (`choco install <package>`).
- For advanced Linux tools (e.g., `gcc`), install [MinGW](http://www.mingw.org/) or [WSL](https://docs.microsoft.com/en-us/windows/wsl/).

## Uninstallation
To remove the aliases, delete the `C:\bin` directory and remove it from your PATH.

## License
MIT License

## Author
Amh4ck3r

---
Feel free to contribute or suggest improvements!
