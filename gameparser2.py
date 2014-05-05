
import random
from gamestarter2 import *
from gameitems2 import *




class Parser(object):
	def __init__(self):
		self.valid = {'hall' : ['open','unlock'], 'alien' : 'attack', 'item' : ['take', 'use'] }
		
	def help(self, room):
		print "type simple two word commands to have me do them."
	
	def parse(self, doer, action, receiver):
		real_action = self.translate(action)
		if real_action in self.valid[receiver.type]:
			return self.do_action(doer, real_action, receiver)
		else:
			print 'I cannot parse.'
		
	def examine(self, doer, action, receiver):
		l = ['look', 'read', 'examine', 'use']
		if action in l:
			for item in doer.items:
				if item.name == receiver:
					if item.name == 'computer':
						self.computer(doer, item)
					else:
						print_lines(item.after)
						
	def computer(self, you, computer):
		print_lines(computer.after)
		while True:
			print "Type 'e' to access the escape pod system self-diagnostic."
			print "Type 'c' to access the captains office security system."
			print "Type 'exit' to exit."
			x = raw_input("> ")
			if x == 'e':
				print "Enter password."
				y = raw_input("> ")
				if y == 'rosebud':
					print "Checking escape pods for problems."
					print "Diagnosing", waiter()
					print "Fixing problems", waiter()
					print "2 problems fixed." 
					print "Perform a manual reset to make Escape pods fully functional."
					print "Returning to main menu."
					you.escape = True
				else:
					print "access denied."
					print "Returning to main menu."
			elif x == 'c':
				
				print "Enter password."
				y = raw_input("> ")
				if y == 'marilyn':
					print "Captains office can now be unlocked."
					print "Returning to main menu."
					key = Item(type = 'key', location = 'captains office')
					you.items.append(key)
				else:
					print "access denied."
					print "Returning to main menu."
			elif x == 'exit':
				break
			else:
				print "Invalid command."
				continue
					
				
		
	def do_action(self, doer, action, receiver):
		if action == 'open':
			return self.open(doer, receiver)
		if action == 'attack':
			return self.attack(doer, receiver)
		if action == 'take':
			return self.take(doer, receiver)
		if action == 'unlock':
			return self.unlock(doer, receiver)
		if action == 'use':
			return self.examine(doer, action, receiver)
		
			
	def take(self, you, item):
		if item.active:
			item.active = False
			you.items.append(item)
			if item.name == 'pipe':
				you.pipe = True
			
	def open(self, you, door):
		if not door.locked:
			return door.location
		else:
			return self.unlock(you, door)
			
	def unlock(self, you, door):
		if len(you.items) >= 1:
			for item in you.items:
				if item.location == door.location:
					print "I unlocked the door!"
					door.locked = False
					return self.open(you, door)
		else:
			return "The door is locked"
			
	def attack(self, you, alien):
		power = random.randint(5,15)
		if alien.alive:
			print "I attacked the alien for %d damage!" % power
			alien.health -= power
			if alien.health <= 0:
				print "you killed the alien"
				alien.active = False
				alien.alive = False
			else:
				print "the alien has %d health left!" % alien.health
		else:
			print "the alien is dead, you can't attack it."
			
	def translate(self, action):
		l = ['look', 'read', 'examine', 'use', 'connect']
		if action in l:
			return 'use'
		unlock = ['unlock']
		if action in unlock:
			return 'unlock'
		open = ['go', 'open']
		if action in open:
			return 'open'
		fight = ['attack', 'fight', 'shoot', 'hit']
		if action in fight:
			return 'attack'
		take = ['take', 'pick up', 'grab', 'get']
		if action in take:
			return 'take'