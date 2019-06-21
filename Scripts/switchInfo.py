#!/usr/bin/python3

"""

Author: Zack Hilton
Date of Creation: 6/19/19

This program is designed to parse switch information
including SW model, IP address, subnet mask, and timsestamp
and convert information to csv for importing into ES.


"""

import re
import datetime


# read in file for parsing
file = open("/root/EnumerationTool/Data/vlanInfo.txt", "r")

# create output file
outFile = open("/root/EnumerationTool/Data/SwitchInfo.txt", "w+")

# open file and parse information
for line in file:
	# look for sw model
	if re.match(r'Aruba', line):
		outFile.write(line)
	# look for sw IP address and subnet mask
	if re.match(r'IP', line):
		outFile.write(line)
	# attempt vlan grab
	if re.match(r"vlan", line):
		outFile.write(line)
		#for line in range(4):
		#	outFile.write(next(file))
# record time
currentTime = str(datetime.datetime.now())

# write time to file
outFile.write(currentTime)


