
from gameparser2 import Parser
from gameitems2 import *

class Person(object):
	def __init__(self, **kwargs):
		self.kind = 'person'
		self.name = None
		self.health = None
		self.type = None
		self.access = []
		self.pipe = False
		self.location = None
		self.direction = None
		self.escape = False
		self.alive = True
		self.active = True
		self.options = kwargs
		self.make()
		self.items = []
		
	def make(self):
		if self.options is not None:
			for k,v in self.options.items():
				if k == 'health':
					self.health = v
				if k == 'name':
					self.name = v
				if k == 'type':
					self.type = v
				if k == 'direction':
					self.direction = v
					
	def do(self, action, other):
		p = Parser()
		return p.parse(self, action, other)
					
	def __str__ (self):
		return self.name
		
