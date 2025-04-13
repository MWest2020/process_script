# process_script

Basically make a python that that runs:

vol -f sample.mem windows.pslist --pid 1944
vol -f sample.mem windows.memmap
strings [path to dump file]

vol -f sample.mem windows.handles --pid 1944

which gets the pid out a config.json

the sample.mem is found in the parent directory (../)

build the scipt according to :

Skip to content
Hacktivity LOGO
Hacktivity

Le Hacking est un état d'esprit

toggle open/close sidebar 

Menu 
0xHomeCheatsheetBlue Teamtoggle child menu
SOC
CERT
Blue Team
Red TeamCTF Write-upMembresToolstoggle child menu
Markdown Map
🤖 Volatility 3 – Windows | Cheatsheet
By : Li_in 23 janvier 2023

OS
Processes / Programs
List processes
Dump process memory
Dump the dlls & exe associated with a process
Extract a process’s memory pages
Extract the “Handles” of a process
Extract DLLs loaded by a process
Network
Files
List files
Extract files
Others
Mindmap
Sources
🇫🇷 Version Française ici
Below is a list of the most frequently used modules and commands in Volatility3 for Windows.

OS
OS information
volatility -f "/path/to/image" windows.info 
Show registers
volatility -f "/path/to/image"  windows.registry.hivescan
List roots :

volatility -f "/path/to/image" windows.registry.hivelist 
List roots and get initial subkeys :

volatility -f "/path/to/image" windows.registry.printkey.PrintKey 
Print Key :

volatility -f "/path/to/image" windows.registry.printkey.PrintKey --key "Software\Microsoft\Windows NT\CurrentVersion"
List services
Scans for windows services :

volatility -f "/path/to/image" windows.svcscan.SvcScan 
Find executed commands
volatility -f "/path/to/image" windows.cmdline
Commands entered in cmd.exe are processed by conhost.exe (csrss.exe before Windows 7). So even if an attacker has managed to kill cmd.exe before we get a memory dump, there’s still a chance of recovering the command line history from conhost.exe’s memory. If you find something odd, try dumping the memory of the process associated with conhost.exe and look for strings inside to extract the command lines


Processes / Programs
List processes
volatility -f "/path/to/image" windows.pslist
volatility -f "/path/to/image" windows.psscan
volatility -f "/path/to/image" windows.pstree
Dump process memory
volatility -f "/path/to/image" -o "/output/path"  windows.memmap.Memmap --pid <PID>  --dump
Dump the dlls & exe associated with a process
volatility -f "/path/to/image" -o "/path/to/dir" windows.dumpfiles ‑‑pid <PID>
Extract a process’s memory pages
Extraire toutes les pages résidant en mémoire dans un fichier individuel.

volatility -f "/path/to/image" -o "/path/to/dir" windows.memmap ‑‑dump ‑‑pid <PID>
Extract the “Handles” of a process
volatility -f "/path/to/image" windows.handles ‑‑pid <PID>
A handle is a structure that lets you define an object (file, socket, pipe, shared memory area, etc. ) and then manipulate it. Handles can be shared by several processes.

Extract DLLs loaded by a process
volatility -f "/path/to/image" windows.dlllist ‑‑pid <PID>
Network
Show network connections
volatility -f "/path/to/image" windows.netscan
volatility -f "/path/to/image" windows.netstat

Files
List files
volatility -f "/path/to/image"  windows.filescan
Extract files
# All files found
volatility -f "/path/to/image" -o "/path/to/dir" windows.dumpfiles
# From its virtual memory offset
volatility -f "/path/to/image" -o "/path/to/dir" windows.dumpfiles ‑‑virtaddr <offset>
# From its physical memory offset
volatility -f "/path/to/image" -o "/path/to/dir" windows.dumpfiles ‑‑physaddr <offset>
Others
Malware scan :
# MALFIND
volatility -f "/path/to/image" windows.malfind
# YARASCAN
volatility -f "/path/to/image" windows.vadyarascan ‑‑yara-rules <string>
volatility -f "/path/to/image" windows.vadyarascan ‑‑yara-file "/path/to/file.yar"
volatility -f "/path/to/image" yarascan.yarascan ‑‑yara-file "/path/to/file.yar"
String search
strings -n <min-string-size> <binary>
Mindmap
Volatility 3 commands mind map | made with markdown-map.com
Volatility 3 commands mind map | made with markdown-map.com
Sources
Problems with volatility 3 : https://blogs.jpcert.or.jp/en/2021/09/volatility3_offline.html
Identify profile : https://heisenberk.github.io/Profile-Memory-Dump/
https://book.hacktricks.xyz/forensics/basic-forensic-methodology/memory-dump-analysis/volatility-examples
https://blog.onfvp.com/post/volatility-cheatsheet/
https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet?q=volatility+
Convert Markdown to mindmap with Markdown-map.com
Posted in Cheatsheet, Favoris, Forensique and tagged Windows
Similaire

🤖 Volatility 3 – Windows | Cheatsheet (FR)
17 avril 2024
Dans "Blue Team"


🤖 Volatility 2 – Windows | Cheatsheet
12 décembre 2024
Dans "Autres"

metasploit
Metasploit – Cheatsheet
22 décembre 2022
Dans "Cheatsheet"




