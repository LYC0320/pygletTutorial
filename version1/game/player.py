import pyglet, math
from game import physicalObject, resources, bullet, util
from pyglet.window import key

class Player(physicalObject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(img = resources.player_image, *args, **kwargs)
		self.thrust = 300.0
		self.rotate_speed = 200.0
		self.key_handler = key.KeyStateHandler()
		self.engine_sprite = pyglet.sprite.Sprite(img = resources.engine_image, *args, **kwargs)
		self.engine_sprite.visible = False

		#dict = {'left' : False, 'right' : False, 'up' : False}

		#self.keys = dict

		self.bullet_speed = 700.0
		self.event_handlers = [self, self.key_handler]

		#to prevent collision between player and bullet
		self.max_velocity = 300.0
		self.name = 'player'

	'''
		#pyglet的func
	def on_key_press(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.keys['left'] = True
		elif symbol == key.RIGHT:
			self.keys['right'] = True
		elif symbol == key.UP:
			self.keys['up'] = True
	
		#pyglet的func
	def on_key_release(self, symbol, modifiers):
		if symbol == key.LEFT:
			self.keys['left'] = False
		elif symbol == key.RIGHT:
			self.keys['right'] = False
		elif symbol == key.UP:
			self.keys['up'] = False
	'''

	def on_key_press(self, symbol, modifiers):
		if symbol == 983547510784 and not self.dead:
			self.fire()

	def update(self, dt):
		super(Player, self).update(dt)
		if self.key_handler[key.LEFT]:
			self.rotation -= self.rotate_speed*dt
		elif self.key_handler[key.RIGHT]:
			self.rotation += self.rotate_speed*dt

		if self.key_handler[key.UP]:
			angle_radian = -math.radians(self.rotation) #角度逆時針- 弧度逆時針+
			force_x = math.cos(angle_radian)*self.thrust*dt
			force_y = math.sin(angle_radian)*self.thrust*dt

			if util.velocityScalar(self.velocity_x + force_x, self.velocity_y + force_y) < self.max_velocity:
				self.velocity_x += force_x
				self.velocity_y += force_y

			self.engine_sprite.visible = True
			self.engine_sprite.x = self.x
			self.engine_sprite.y = self.y
			self.engine_sprite.rotation = self.rotation
		else:
			self.engine_sprite.visible = False

		if self.key_handler[key.DOWN]:
			self.velocity_x *= 0.98
			self.velocity_y *= 0.98


	def delete(self):
		self.engine_sprite.delete()
		super(Player, self).delete()

	def fire(self):
		angle_radian = -math.radians(self.rotation)
		ship_radius = self.image.width/2 + 20
		bullet_x = self.x + ship_radius * math.cos(angle_radian)
		bullet_y = self.y + ship_radius * math.sin(angle_radian)
		new_bullet = bullet.Bullet(x = bullet_x, y = bullet_y, batch = self.batch)
		bullet_vx = self.velocity_x + self.bullet_speed * math.cos(angle_radian)
		bullet_vy = self.velocity_y + self.bullet_speed * math.sin(angle_radian)
		new_bullet.velocity_x = bullet_vx
		new_bullet.velocity_y = bullet_vy
		self.new_objects.append(new_bullet)