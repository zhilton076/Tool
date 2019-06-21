#!/usr/bin/python3

"""

Author: Zack Hilton
Date of Creation: 6/10/2019

This program is designed to parse a spreadsheet
containing network vlans, then use the results 
to nmap the network.

"""

import re
import nmap

# open vlan file, store in v
infile = open("/root/EnumerationTool/Data/parseToTxt.txt", "r")

# open file for nmap results
outFile = open("/root/EnumerationTool/Data/fullNmapResults.csv", "w+")

# nmap handling
nm = nmap.PortScanner()

# iterate through the file, scanning each IP range
for line in infile:
	if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line):
		print(re.sub(r'.*10', '10', line))
		nm.scan(re.sub(r'.*10', '10', line))
		outFile.write(nm.csv())




