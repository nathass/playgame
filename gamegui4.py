
from gameparser2 import *
from gamescenes2 import *
from gameitems2 import *
from gamepeople2 import *
from gametext2 import *
import os, sys
from Gui import *
from Tkinter import *


class Game(Gui):
	
		
	
	def setup(self):
		self.launch = False
		self.room_frame = None
		self.enter_text = None
		self.on_computer = False
		self.use_computer = False
		self.player = Person(name = 'player', health = 100, type = 'player')
		self.make_rooms()
		self.x = self.maps.get(self.name)
		self.draw_map()
		x = self.get_text('START3')
		x = ''.join(x)
		self.display.configure(text=x)
		self.mainloop()
		
	def make_rooms(self):
		self.maps = {'robot storage':RobotStorage(self.player), 'barracks':Barracks(self.player), 'dining room':DiningRoom(self.player)}
		self.maps['engine room'] = EngineRoom(self.player)
		self.maps['computer room'] = ComputerRoom(self.player)
		self.maps['maintenance room'] = MaintenanceRoom(self.player)
		self.maps['escape pod'] = EscapePod(self.player)
		self.maps['warehouse'] = Warehouse(self.player)
		self.maps['bathroom'] = Bathroom(self.player)
		self.maps['captains office'] = CaptainsOffice(self.player)
		self.name = 'robot storage'
	
	
		
				
	def go_room(self, direction):
		for thing in self.x.things:
			if thing.direction == direction and thing.type == 'hall':
				if thing.locked:
					for item in self.player.access:
						if item == thing.location:
							self.x = self.maps.get(thing.location)
							self.move_icon(direction)
							self.change_rooms()
						else:
							self.display.configure(text="It's locked.")
				else:
					self.x = self.maps.get(thing.location)
					self.move_icon(direction)
					self.change_rooms()
			else:
				pass
		
	def move_icon(self, direction):
		if direction == 'north':
			self.player_icon.move(0,110)
		if direction == 'south':
			self.player_icon.move(0,-110)
		if direction == 'east':
			self.player_icon.move(110,0)
		if direction == 'west':
			self.player_icon.move(-110,0)
		
		
		
	def draw_map(self):
		self.fr()
		self.row([0,1,0])
		self.col()
		self.west_b = self.bu(text='<', command = Callable(self.go_room, 'west'))
		self.endcol()
		self.col()
		self.north_b = self.bu(text='/\\', command = Callable(self.go_room, 'north'))
		ca = self.ca(width=560, height=340)
		item2 = ca.rectangle([[-270, 50], [-170, -50]], fill='grey', outline = 'grey')
		item1 = ca.rectangle([[-270, -60], [-170, -160]], fill='grey', outline = 'grey')
		item3 = ca.rectangle([[-160, 160], [-60, 60]], fill='grey', outline = 'grey')
		item4 = ca.rectangle([[-160, 50], [-60, -50]], fill='grey', outline = 'grey')
		item5 = ca.rectangle([[-160, -60], [-60, -160]], fill='grey', outline = 'grey')
		item6 = ca.rectangle([[-50, 50], [50, -50]], fill='grey', outline = 'grey')
		item7 = ca.rectangle([[-50, -60], [50, -160]], fill='grey', outline = 'grey')
		item8 = ca.rectangle([[60, 50], [160, -50]], fill='grey', outline = 'grey')
		item9 = ca.rectangle([[60, -60], [160, -160]], fill='grey', outline = 'grey')
		item10 = ca.rectangle([[170, -60], [270, -160]], fill='grey', outline = 'grey')
		ca.text([-220,-40], text='bathroom')
		ca.text([-220,-150], text='computer room')
		ca.text([-110,70], text='warehouse')
		ca.text([-110,-40], text='maintenance')
		ca.text([-110,-150], text='engine')
		ca.text([-10,-40], text='escape')
		ca.text([-10,-150], text='robot')
		ca.text([110,-40], text='captains')
		ca.text([110,-150], text='dining')
		ca.text([220,-150], text='baracks')
		item21 = ca.rectangle([[-170, 10], [-150, -10]], fill='grey', outline = 'grey')
		item22 = ca.rectangle([[-170, -110], [-150, -130]], fill='grey', outline = 'grey')
		item23 = ca.rectangle([[-65, -110], [-45, -130]], fill='grey', outline = 'grey')
		item24 = ca.rectangle([[45, -110], [65, -130]], fill='grey', outline = 'grey')
		item25 = ca.rectangle([[155, -110], [175, -130]], fill='grey', outline = 'grey')
		item26 = ca.rectangle([[-65, 10], [-45, -10]], fill='grey', outline = 'grey')
		item27 = ca.rectangle([[-120, 60], [-100, 40]], fill='grey', outline = 'grey')
		item28 = ca.rectangle([[-120, -50], [-100, -70]], fill='grey', outline = 'grey')
		item29 = ca.rectangle([[100, -50], [120, -70]], fill='grey', outline = 'grey')
		self.c_clock = ca.text([110,-55], text='=')
		self.w_lock = ca.text([-110,55], text='=')
		self.player_icon = ca.circle([0, -110], 10, fill = 'red')
		self.south_b = self.bu(text='\\/', command = Callable(self.go_room, 'south'))
		self.endcol()
		self.col()
		self.east_b = self.bu(text='>', command = Callable(self.go_room, 'east'))
		self.endcol()
		self.endrow()
		self.row([1,0])
		self.display = self.la(text="Hello there.\nHow are you?")
		self.ca(width=10, height=150)
		self.endrow()
		self.row()
		self.col()
		self.entry = self.en()
		self.entry.insert(END, 'Type your commands here.')
		self.endcol()
		self.endrow()
		self.row([0,1])
		self.col()
		self.ca(width=10, height=100)
		self.endcol()
		self.col([0,1])
		self.enter_key = self.bu(text='Enter', command=self.enter)
		self.ca(width=10, height=10)
		self.endcol()
		self.player_controls()
		self.make_controls()
		
	def enter(self):
		self.enter_text = self.entry.get()
		self.enter_check()
		
	def enter_check(self):
		if self.use_computer:
			self.display.configure(text=self.computer_display)
			self.is_it_on()
			
			
	def is_it_on(self):
		if self.enter_text == 'computer e':
			self.enter_key.configure(command = self.get_password_e)
			self.display.configure(text="enter password.")
		elif self.enter_text == 'computer c':
			self.enter_key.configure(command = self.get_password_c)
			self.display.configure(text = "enter password.")
		else:
			self.display.configure(text="does not compute.\n"+self.computer_display)
		
	def get_password_e(self):
		self.enter_text = self.entry.get()
		if self.enter_text == 'rosebud':
			self.player.escape = True
			self.display.configure(text="Escape Pods repaired.\nPerform manual reset to complete.")
		else:
			self.display.configure(text="incorrect password")
		self.enter_key.configure(command=self.enter)
		
	def get_password_c(self):
		self.enter_text = self.entry.get()
		if self.enter_text == 'marilyn':
			self.player.access.append('captains office')
			self.display.configure(text="Captain's office is now unlocked.")
			self.c_clock.delete()
		else:
			self.display.configure(text="incorrect password")
		self.enter_key.configure(command=self.enter)
			
		
	def change_rooms(self):
		if self.use_computer:
			self.use_computer = False
		if self.room_frame:
			self.room_frame.destroy()
		self.player_frame.destroy()
		self.player_controls()
		self.room_description = []
		self.get_lines(self.x.description)
		for thing in self.x.things:
			if thing.active:
				self.get_stuff(thing)
		x = ''.join(self.room_description)
		self.display.configure(text=x)
		self.make_controls()
		
	def describe_room(self):
		self.room_description = []
		self.get_lines(self.x.description)
		for thing in self.x.things:
			if thing.active:
				self.get_stuff(thing)
		x = ''.join(self.room_description)
		self.display.configure(text=x)
		
	def describe_action(self, item):
		self.display.configure(text='I took the %s' % item)
		if item.name == 'key':
			self.player.access.append('warehouse')
			self.w_lock.delete()
					
					
	def get_stuff(self, thing):
		if thing.before:
			self.get_lines(thing.before)
		
	
	def get_lines(self, before):
		x = self.get_text(before)
		for line in x:
			self.room_description.append(line)
	
	def get_start(self, file, location):
		for line in file:
			if line.strip() == location:
				break
	
	
	def get_text(self, location):
		z = get_game_text()
		o=[]
		q=False
		for i in z:
			if i == 'END' and q:
				return o
			if q:
				o.append(i+"\n")
			if i == location:
				q = True
		
				
	def make_controls(self):
		self.room_frame = self.fr(bd=2, relief=SUNKEN, padx=1, pady=1, expand=0)
		self.it = self.la(text='Items in room')
		for thing in self.x.things:
			if thing.type == 'item' and thing.active:
				if thing.name == 'computer':
					self.bu(text=thing, command=Callable(self.compute, thing))
				elif thing.name == 'launch':
					self.bu(text=thing, command=self.launcher)
				else:
					self.bu(text=thing, command=Callable(self.take, 'take', thing))
		self.endfr()
		
	def player_controls(self):
		self.player_frame = self.fr(bd=2, relief=SUNKEN, padx=1, pady=1, expand=0)
		self.p_it = self.la(text='Inventory')
		for item in self.player.items:
				self.bu(text=item, command=Callable(self.use, item))
		self.endfr()
	
	def use(self, item):
		x = self.get_text(item.after)
		x = ''.join(x)
		self.display.configure(text=x)
		
	
	def take(self, action, item):
		self.player.do(action, item)
		self.room_frame.destroy()
		self.describe_action(item)
		self.player_frame.destroy()
		self.player_controls()
		self.make_controls()
					
	def compute(self, thing):
		x = self.get_text(thing.after)
		x = ''.join(x)
		self.display.configure(text=x)
		self.use_computer = True
		x = self.get_text(thing.using)
		x = ''.join(x)
		self.computer_display = x
		
	def launcher(self):
		if self.launch:
			if self.player.escape:
				if self.player.pipe:
					x = self.get_text('CLEANESCAPE')
					x = ''.join(x)
					self.display.configure(text=x)
				else:
					x = self.get_text('MAYBEESCAPE')
					x = ''.join(x)
					self.display.configure(text=x)
			else:
				x = self.get_text('NOESCAPE')
				x = ''.join(x)
				self.display.configure(text=x)
		else:
			self.launch = True
			x = self.get_text('LAUNCH1')
			x = ''.join(x)
			self.display.configure(text=x)
			
					
	
	
	
					
class RoomControl(object):
	
	def __init__(self, game):
		self.game = game
		self.setup()
		
	def setup(self):
		w = self.game
		x = 0
		for thing in self.game.x.things:
			if thing.type == 'item' and thing.active:
				x+=1
		if x > 0:
			self.frame = w.fr(bd=2, relief=SUNKEN, padx=1, pady=1, expand=0)
			self.it = w.la(text='Items in room')
			for thing in self.game.x.things:
				if thing.type == 'item' and thing.active:
					w.bu(text=thing, command=Callable(self.use, 'take', thing))
			w.endfr()
	
	def use(self, action, item):
		self.game.player.do(action, item)
		self.frame.destroy()
		self.it.destroy()
		self.game.describe_action(item)
		self.setup()


































