#!/usr/bin/python3
"""

Author: Zack Hilton
Date of Creation: 6/20/2019

This program is designed to parse the output
of autoSwitchPull.sh and put the vlan information
neatly into a spreadsheet.


"""

import re
import datetime

# grab current time for timestamp
current_time = datetime.datetime.now()

# open script output file
file = open("/root/EnumerationTool/Data/SwitchInfo.txt", "r")
outFile = open("/root/EnumerationTool/Data/parse_switch_info.csv", "w+")

# print csv structure header
#print("Switch model, Switch IP, VLAN ID")
outFile.write("Switch model,Switch IP,VLAN ID,Timestamp" + "\n")
# initalize arrays
switch = []
vlan = []
ip = []

# parse vlan information
for line in file:
	if re.findall(r"vlan ", line):
		vlan.append(line)
	if re.findall(r"Aruba ", line):
		switch.append(line)
	if re.findall(r"IP: ", line):
		ip.append(line)
file.close()

# strip newline chars at each line
for x in range(len(switch)):
	switch[x] = switch[x].strip()
for x in range(len(ip)):
	ip[x] = ip[x].strip()
	ip[x] = re.sub("IP: ","", ip[x])
for x in range(len(vlan)):
	vlan[x] = vlan[x].strip()

# loop to format into csv
try:
	for x in range(len(vlan)):
		outFile.write(switch[0] + ",")
		#print(switch[0], end = ",")
		outFile.write(ip[0] + ",")
		#print(ip[0], end = ",")
		outFile.write(vlan[x] + ",")
		outFile.write(str(current_time) + "\n")
		#print(vlan[x])
		#outFile.write(str(current_time))
		#print(" ")
except IndexError:
		print("Index Errors")


