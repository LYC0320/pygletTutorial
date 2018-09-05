import pyglet
from game import physicalObject, resources

class Bullet(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Bullet, self).__init__(img = resources.bullet_image, *args, **kwargs)
		pyglet.clock.schedule_interval(self.die, 0.5)

		self.name = 'bullet'

	def die(self, dt):
		self.dead = True