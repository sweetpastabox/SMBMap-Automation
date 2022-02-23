#/usr/bin/python3.9

import ipaddress
from subprocess import Popen, PIPE, STDOUT

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner = """
                                                                
 _____ _____ _____    _____     _                 _   _         
|   __|     | __  |  |  _  |_ _| |_ ___ _____ ___| |_|_|___ ___ 
|__   | | | | __ -|  |     | | |  _| . |     | .'|  _| | . |   |
|_____|_|_|_|_____|  |__|__|___|_| |___|_|_|_|__,|_| |_|___|_|_|
                                                                

				Automation by 0xZ3r0X
"""

def script():

	print(bcolors.HEADER + banner + bcolors.ENDC)
	print("")

	ip_range=input(bcolors.HEADER + "Select an IP range (x.x.x.x/X or single IP)	:	" + bcolors.ENDC)
	#nmap_report = NmapParser.parse_fromfile(path)

	IPS = [str(ip) for ip in ipaddress.IPv4Network(ip_range)]
	vulnerable = []

	print("")
	print(bcolors.OKCYAN + "--------- [[Proceed to testing on targets ? (Yes/No) ]] --------" +  bcolors.ENDC)
	print("")
	answ=input("  >>  ")

	if answ == "Yes":
		for a in IPS:
			p = Popen(["smbmap", "-H", a], stdin=PIPE, stdout=PIPE, stderr=STDOUT, text=True)
			for line in p.stdout:
				if "[!] Authentication error on" in line:
					print(bcolors.FAIL + line + bcolors.ENDC)
				elif "[+] Guest session " in line:
					print(bcolors.OKGREEN + line + bcolors.ENDC)
					vulnerable.append(line)
				elif "[+] IP:" in line:
					print(bcolors.OKGREEN + line + bcolors.ENDC)
					vulnerable.append(line)
		print("")
		print("Found %s vulnerable hosts : " %len(vulnerable))
		print("")
		print(bcolors.OKCYAN +"--------- [[VULNERABLE HOSTS]] --------"+  bcolors.ENDC)
		for a in vulnerable:
			print(a)
	if answ == "No":
		print("Ok, bye!")

if __name__ == '__main__':
	script()
