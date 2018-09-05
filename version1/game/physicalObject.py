import pyglet
from game import util

class PhysicalObject(pyglet.sprite.Sprite):

	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)

		self.velocity_x, self.velocity_y = 0.0, 0.0
		self.dead = False
		self.new_objects = []
		self.event_handlers = []

		self.name = ''

	def update(self, dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt

		self.checkBounds()

	def checkBounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = 800 + self.image.width/2
		max_y = 600 + self.image.height/2

		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x

		if self.y < min_y:
			self.y = max_y
		elif self.y > max_y:
			self.y = min_y

	def collides_with(self, other_object):
		collision_distance = self.image.width/2 + other_object.image.width/2
		actual_distance = util.distance((self.x, self.y), (other_object.x, other_object.y))
		return actual_distance <= collision_distance

	def handle_collision_with(self, other_object):
		if self.__class__ == other_object.__class__ :
			self.dead = False
		elif self.name == ('player' or 'bullet') and other_object.name == ('bullet' or 'player'):
			self.dead = False
		else:
			self.dead = True