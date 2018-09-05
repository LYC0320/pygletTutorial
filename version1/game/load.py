import pyglet, random, math
from game import resources, physicalObject, util, asteroid


def asteroids(num_asteroids, player_position, batch=None):
	asteroids = []
	for i in range(num_asteroids):
		asteroids_x, asteroids_y = player_position
		while util.distance((asteroids_x, asteroids_y), player_position) < 100:
			asteroids_x = random.randint(0, 800)
			asteroids_y = random.randint(0, 600)
		#new_asteroid = pyglet.sprite.Sprite(img = resources.asteroid_image, 
		#									x=asteroids_x, y=asteroids_y, batch=batch)
		#new_asteroid = physicalObject.PhysicalObject(img = resources.asteroid_image,
		#	 										x =asteroids_x, y = asteroids_y, batch = batch) #已繼承pyglet.sprite.Sprite
		new_asteroid = asteroid.Asteroid(x = asteroids_x, y = asteroids_y, batch = batch) #已繼承pyglet.sprite.Sprite

		new_asteroid.rotation = random.randint(0, 360)
		new_asteroid.velocity_x = random.random()*40
		new_asteroid.velocity_y = random.random()*40
		asteroids.append(new_asteroid)
	return asteroids

def player_lives(nums_icons, batch=None):
	player_lives = []
	for i in range(nums_icons):
		new_sprite = pyglet.sprite.Sprite(img = resources.player_image,
										  x=785-i*30, y=585, batch=batch)
		new_sprite.scale = 0.5
		player_lives.append(new_sprite)
	return player_lives