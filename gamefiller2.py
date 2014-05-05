from gameitems2 import *
from gamepeople2 import *

def fill(room, thing, **kwargs):
	if thing == 'alien':
		alien = Person(**kwargs)
		room.things.append(alien)
	if thing == 'item':
		item = Item(**kwargs)
		room.things.append(item)