"""
File: breakout.py
Name: Zoe
----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

These code is to create a breakout game. And when the balls falls out of
the bottom edge of the window, your remaining lives will be deducted once.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts



def main():
    """
    These code is to create a breakout game.
    """
    graphics = BreakoutGraphics()
    graphics.set_lives(NUM_LIVES)
    while graphics.num_lives > 0:
        while True:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get_dx())
            if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
                graphics.ball.x = (graphics.window.width - graphics.ball.width)//2
                graphics.ball.y = (graphics.window.height - graphics.ball.width)//2
                graphics.num_lives -= 1
                graphics.lives_board.text = 'Lives remain: ' + str(graphics.num_lives)  
                graphics.set_dx(0)  
                graphics.set_dy(0)  
                graphics.click = False  
                break
            if graphics.bricks_num == 0:  
                break
            pause(FRAME_RATE)
            check_for_collision(graphics)
        if graphics.bricks_num == 0:  
            break


def check_for_collision(graphics):
    """
    This function is to check whether the ball contact the bricks and paddles, it will eliminate the bricks when
    contacting them; and bouncing when contacting the paddle.
    """
    for i in range(0, graphics.ball.width+1, graphics.ball.width):
        for j in range(0, graphics.ball.height+1, graphics.ball.height):
            obj = graphics.window.get_object_at(graphics.ball.x+i, graphics.ball.y+j)
            if obj is not None:
                if obj == graphics.paddle:
                    if graphics.get_dy() > 0:  
                        graphics.set_dy(-graphics.get_dy())
                        return
                else:
                    graphics.window.remove(obj)
                    graphics.bricks_num -= 1
                    graphics.set_dy(-graphics.get_dy())
                    return



if __name__ == '__main__':
    main()
