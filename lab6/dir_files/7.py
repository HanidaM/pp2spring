import imp


import os

with open('test1.py','r') as first, open('test2.py','a') as second:
	
	for line in first:
            second.write(line)
