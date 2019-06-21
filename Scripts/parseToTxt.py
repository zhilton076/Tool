#!/usr/bin/python3
"""

Author: Zack Hilton
Date of Creation: 6/11/2019

This program is designed to parse the output
of autoSwitchPull.sh and put the vlan information
neatly into a spreadsheet.


"""

import re


# open script output file
file = open("/root/EnumerationTool/Data/vlanInfo.txt", "r")
outFile = open("/root/EnumerationTool/Data/parseToTxt.txt", "w+")


# parse vlan information
for line in file:
	if re.match(r"vlan", line):
		outFile.write(line)
		for line in range(4):
			outFile.write(next(file))

# same ouput, worse code
"""		# print(line)
		outFile.write(line)
	if re.match("   name", line):
		# print(line)
		outFile.write(line)
	if re.match(r"   ip", line):
		# print(line)
		outFile.write(line)
"""


		



