
from gamepeople2 import Person
from gameitems2 import *
from gamefiller2 import *
from gameparser2 import *
from gamestarter2 import *

class Scene(object):
	def __init__(self, player = None):
		self.new = True
		self.kind = 'scene'
		self.name = None
		self.things = []
		self.main = player
		self.begin()
		
	def start(self):
		pass
	
	def begin(self):
		pass
	
	def enter(self):
		pass
		
	def tester(self):
		if self.new:
			self.start()
			self.new = False
			for thing in self.things:
				if thing.active:
					if thing.before:
						print_lines(thing.before)
					elif thing.direction == self.main.direction:
						x = "Behind me to the the [%s], there is a %s where we came from.\n" % (thing.direction, thing)
						printer(x)
					else:
						x = "On the [%s] side of the room there is a %s.\n" % (thing.direction, thing)
						printer(x)
		else:
			print_lines(self.room_name)
		printer("what would you like me to do?\n")
		test = None
		while not test:
			input = raw_input("> ")
			test = self.parser(input)
		return test
		
	def parser(self, input):
		if 'computer' in input:
			q = Parser()
			for thing in self.things:
				if thing.name == 'computer':
					print 2
					q.computer(self.main, thing)
					return
		if input == 'help':
			t = Parser()
			return t.help(self)
		x = input.split()
		valid = False
		for thing in self.things:
			if thing.active:
				if thing.name == x[-1] or thing.direction == x[-1] or thing.type == x[-1]:
					valid = True
					action = ' '.join(x[:-1])
					z = self.main.do(action, thing)
		if not valid:
			try:
				t = Parser()
				t.examine(self.main, x[0], x[1])
			except:
				print "I don't understand."
		else:
			return z
		
class RobotStorage(Scene):
	def enter(self):
		return self.tester()
		
	def start(self):
		print_lines('START')
		x = raw_input("> ")
		if x == 'rochel':
			print_lines('NAME')
		else:
			printer(x)
			print ''
			print_lines('NAME2')
		print_lines('START2')
		print_lines('ROBOTSTORAGE')
			
		
		
	def begin(self):
		self.room_name = 'ROBOTSTORAGE'
		self.description = 'ROBOTSTORAGE2'
		fill(self, 'item', type = 'hall', location = 'engine room', name = 'engine room', direction = 'west')
		fill(self, 'item', type = 'hall', location = 'dining room', name = 'dining room', direction = 'east')
		
		
class DiningRoom(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'DININGROOM'
		self.description = 'DININGROOM2'
		fill(self, 'item', type = 'hall', location = 'captains office', name = 'captains office', direction = 'north', locked = True)
		fill(self, 'item', type = 'hall', location = 'barracks', name = 'barracks', direction = 'east')
		fill(self, 'item', type = 'hall', location = 'robot storage', name = 'robot storage', direction = 'west')
		

class Barracks(Scene):
	def start(self):
		print_lines(self.description)

	def enter(self):
		return self.tester()


	def begin(self):
		self.room_name  = 'BARRACKS'
		self.description = 'BARRACKS2'
		fill(self, 'item', type = 'hall', location = 'dining room', name = 'dining room', direction = 'west')
		fill(self, 'item', type = 'item', name = 'paper', before = 'PAPER1', after = 'PAPER2')

class EngineRoom(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'ENGINEROOM'
		self.description = 'ENGINEROOM2'
		fill(self, 'item', type = 'hall', location = 'maintenance room', name = 'maintenance room', direction = 'north')
		fill(self, 'item', type = 'hall', location = 'computer room', name = 'computer room', direction = 'west')
		fill(self, 'item', type = 'hall', location = 'robot storage', name = 'robot storage', direction = 'east')

class ComputerRoom(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'COMPUTERROOM'
		self.description = 'COMPUTERROOM2'
		fill(self, 'item', type = 'hall', location = 'engine room', name = 'engine room', direction = 'east')
		fill(self, 'item', type = 'item', name = 'computer', before = 'COMPUTER1', after = 'COMPUTER2', using='COMPUTER3')
		self.key = Item(type = 'key', location = 'captains office')

class MaintenanceRoom(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'MAINTENANCE'
		self.description = 'MAINTENANCE2'
		fill(self, 'item', type = 'hall', location = 'escape pod', name = 'escape pod', direction = 'east')
		fill(self, 'item', type = 'hall', location = 'engine room', name = 'engine room', direction = 'south')
		fill(self, 'item', type = 'hall', location = 'warehouse', name = 'warehouse', direction = 'north', locked = True)
		fill(self, 'item', type = 'hall', location = 'bathroom', name = 'bathroom', direction = 'west')

class Warehouse(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'WAREHOUSE'
		self.description = 'WAREHOUSE2'
		fill(self, 'item', type = 'hall', location = 'maintenance room', name = 'maintenance room', direction = 'south')
		fill(self, 'item', type = 'item', name = 'pipe',direction = 'east', before = 'PIPE1', after = 'PIPE2')
	
class EscapePod(Scene):
	def start(self):
		self.escape_test()
		
	def escape_test(self):
		if self.main.escape:
			for item in self.main.items:
				if item.name == 'pipe':
					print_lines('CLEANESCAPE')
					exit(1)
			print_lines('MAYBEESCAPE')
			exit(1)
		else:
			print_lines('NOESCAPE')
			exit(1)
	
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'ESCAPEPOD'
		self.description = 'ESCAPEPOD2'
		fill(self, 'item', type = 'hall', location = 'maintenance room', name = 'maintenance room', direction = 'west')
		fill(self, 'item', type = 'item', name = 'launch',direction = 'east')
		

class Bathroom(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'BATHROOM'
		self.description = 'BATHROOM2'
		fill(self, 'item', type = 'hall', location = 'maintenance room', name = 'maintenance room', direction = 'east')
		fill(self, 'item', type = 'item', name = 'photo', direction = 'west', before = 'PHOTO1', after = 'PHOTO2')
		
class CaptainsOffice(Scene):
	def start(self):
		print_lines(self.description)
		
	def enter(self):
		return self.tester()
	
	def begin(self):
		self.room_name  = 'CAPTAINSOFFICE'
		self.description = 'CAPTAINSOFFICE2'
		fill(self, 'item', type = 'hall', location = 'dining room', name = 'dining room', direction = 'south')
		fill(self, 'item', type = 'item', name = 'key', direction = 'east', location = 'warehouse', before = 'KEY1', after = 'KEY2')








































