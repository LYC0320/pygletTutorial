import pyglet
from game import resources, load, player, bullet, asteroid

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Version 1: Static Graphics", 
								x=400, y=575, anchor_x='center')

#player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
#player_ship = load.physicalObject.PhysicalObject(img=resources.player_image, x=400, y=300)
player_ship = player.Player(x=400, y=300, batch = main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)
player_lives = load.player_lives(5, main_batch)

				#轉成list
game_objects = [player_ship] + asteroids

score = 0

def init():
	global score
	score = 0

def update(dt):
	global score

	for i in range(len(game_objects)):
		for j in range(i+1, len(game_objects)):
			obj_1 = game_objects[i]
			obj_2 = game_objects[j]

			if obj_1.collides_with(obj_2) and not obj_1.dead and not obj_2.dead:
				obj_1.handle_collision_with(obj_2)
				obj_2.handle_collision_with(obj_1)

	to_add = []

	#order is important
	for object in game_objects:
		object.update(dt)
		to_add.extend(object.new_objects)
		object.new_objects = []

	for to_remove in (obj for obj in game_objects if obj.dead):
		if to_remove.name == 'asteroid':
			score += 10
			score_label.text = "Score:" + str(score)

		if to_remove.dead:
			to_remove.delete()
			game_objects.remove(to_remove)

	game_objects.extend(to_add)

for obj in game_objects:
	for handler in obj.event_handlers:
		game_window.push_handlers(handler)
#game_window.push_handlers(player_ship)

#1/120.0 會輸入給update
pyglet.clock.schedule_interval(update, 1/120.0)

#處理key事件
#game_window.push_handlers(player_ship)
game_window.push_handlers(player_ship.key_handler)

@game_window.event
def on_draw():
	game_window.clear()
	level_label.draw()
	#score_label.draw()
	#player_ship.draw()
	#for asteroid in asteroids:
	#	asteroid.draw()
	main_batch.draw()

if __name__ == '__main__':                                                                                                     
    pyglet.app.run()
    init()   