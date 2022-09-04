"""
File: bouncing_ball
Name: Zoe
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself. It stops after 3 times of clicks.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
click = False
count_outside = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    window.add(ball)
    onmouseclicked(start)


def start(mouse):
    global click, count_outside
    if not click and count_outside != 3:
        click = True
        dy = 0
        while True:
            ball.move(VX, dy)
            dy += GRAVITY

            if ball.y >= window.height - SIZE:
                dy *= -1 * REDUCE

            pause(DELAY)

            if ball.x > window.width:
                ball.x = START_X
                ball.y = START_Y
                count_outside += 1
                click = False
                break


if __name__ == "__main__":
    main()
