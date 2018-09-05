import math

def distance(point_1=(0, 0), point_2=(0, 0)):
	return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)

def velocityScalar(velocity_x, velocity_y):
	return math.sqrt(velocity_x**2 + velocity_y**2)