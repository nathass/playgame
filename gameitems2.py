


class Item(object):
	def __init__(self, **kwargs):
		self.kind = 'item'
		self.name = None
		self.type = None
		self.location = None
		self.direction = None
		self.before = None
		self.after = None
		self.locked = False
		self.using = False
		self.options = kwargs
		self.active = True
		self.make()
		self.items = []
		
	def make(self):
		if self.options is not None:
			for k,v in self.options.items():
				if k == 'location':
					self.location = v
				if k == 'name':
					self.name = v
				if k == 'type':
					self.type = v
				if k == 'direction':
					self.direction = v
				if k == 'locked':
					self.locked = v
				if k == 'before':
					self.before = v
				if k == 'after':
					self.after = v
				if k == 'using':
					self.using = v
					
					
	def __str__ (self):
		if self.type == 'hall':
			return "hallway to the %s" % self.location
		if self.type == 'item':
			return "%s" % self.name