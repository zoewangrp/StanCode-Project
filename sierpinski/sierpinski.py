"""
File: sierpinski.py
Name: Zoe
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6  # Controls the order of Sierpinski Triangle
LENGTH = 600  # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150  # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100  # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950  # The width of the GWindow
WINDOW_HEIGHT = 700  # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	To recursively prints the Sierpinski triangle on GWindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the level of the triangle.
	:param length: int, the side length of the triangle.
	:param upper_left_x: int, the triangle's x coordinate of upper left vertex.
	:param upper_left_y: int, the triangle's y coordinate of upper left vertex.
	:return: Sierpinski triangle
	"""
	if order == 0:
		pass
	else:
		left_side = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		window.add(left_side)
		top_side = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		window.add(top_side)
		right_side = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.866)
		window.add(right_side)
		pause(100)

		# Left triangle
		sierpinski_triangle(order-1, length*0.5, upper_left_x, upper_left_y)
		# Right triangle
		sierpinski_triangle(order-1, length*0.5, upper_left_x+length*0.5, upper_left_y)
		# Bottom triangle
		sierpinski_triangle(order - 1, length * 0.5, upper_left_x + length * 0.25, upper_left_y+length* 0.5 * 0.866)


if __name__ == '__main__':
	main()
