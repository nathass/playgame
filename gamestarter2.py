
import sys
from time import sleep

def starter():
	x = "this is a test"
	printer(x)
	waiter()
	x = "second test"
	printer(x)
	waiter()
	
def waiter():
	for i in range(5):
		sys.stdout.write('.')
		sys.stdout.flush()
		sleep(.3)
		sys.stdout.write('.')
		sys.stdout.flush()
		sleep(.3)
		sys.stdout.write('.')
		sys.stdout.flush()
		sleep(.3)
		print '\b\b\b',
		print '\b   ',
		print '\b\b\b\b',
	print '\b...'
		
			
def printer(string):
	for l in string:
		sys.stdout.write(l)
		sys.stdout.flush()
		sleep(.01)

def get_start(file, location):
	for line in file:
		if line.strip() == location:
			break

def get_text(location):
	x = open('/Users/nathan/Developer/gametext.txt')
	o=[]
	get_start(x, location)
	for line in x:
		if 'END' in line:
			return o
		else:
			o.append(line)

def print_lines(location):
	x = get_text(location)
	for line in x:
		printer(line)
		








































