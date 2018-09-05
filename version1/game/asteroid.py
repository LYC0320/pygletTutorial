import pyglet, random
from game import resources, physicalObject

class Asteroid(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Asteroid, self).__init__(img = resources.asteroid_image, *args, **kwargs)
		self.rotation_speed = random.random() * 100 - 50
		self.name = 'asteroid'
	
	def handle_collision_with(self, other_object):
		super(Asteroid, self).handle_collision_with(other_object)
		if self.dead and self.scale > 0.25:
			num_asteroid = random.randint(2, 3)
			for i in range(num_asteroid):
				new_asteroid = Asteroid(x = self.x, y = self.y, batch = self.batch)
				new_asteroid.rotation = random.randint(0, 360)
				new_asteroid.velocity_x = self.velocity_x + random.random() * 30
				new_asteroid.velocity_y = self.velocity_y + random.random() * 30
				new_asteroid.scale = self.scale * 0.5
				self.new_objects.append(new_asteroid)

	def update(self, dt):
		super(Asteroid, self).update(dt)
		self.rotation += self.rotation_speed * dt
		