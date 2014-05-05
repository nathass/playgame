
import os
a = "x.append("""
b = """)"""
x = open('/Users/nathan/developer/game/gametext2.txt')
y = open('/Users/nathan/developer/game/gametext2.py', 'w')
for line in x:
	y.write(a+line.strip()+b+"\n")
y.close()