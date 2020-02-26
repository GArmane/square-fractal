from TurtleWorld import *

TURTLE_X = -75
TURTLE_Y = 75
TURTLE_DELAY = 0
DRAW_LENGHT = 500

def draw_square_fractal(turtle, lenght, angle=90):
	for _ in range(4):
		draw_square_line(turtle, lenght, angle)
		rt(turtle, 90)

def draw_square_line(turtle, lenght, angle=90):
	if lenght < 4:
		fd(turtle, lenght)
		return
	else:
		div_lenght = lenght / 4
		draw_square_line(turtle, div_lenght)
		lt(turtle, angle)
		draw_square_line(turtle, div_lenght)
		rt(turtle, angle)
		draw_square_line(turtle, div_lenght)
		rt(turtle, angle)
		draw_square_line(turtle, div_lenght)
		lt(turtle, angle)
		draw_square_line(turtle, div_lenght)

if __name__ == '__main__':
	world = TurtleWorld()
	turtle = Turtle()
	turtle.x = TURTLE_X
	turtle.y = TURTLE_Y
	turtle.delay = TURTLE_DELAY
	turtle.redraw()

	draw_square_fractal(turtle, DRAW_LENGHT)

	wait_for_user()
