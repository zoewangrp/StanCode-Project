"""
File: breakout graphics.py
Name: Zoe
----------------------------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

These code is to create a breakout game. And when the balls falls out of
the bottom edge of the window, your remaining lives will be deducted once.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball



class BreakoutGraphics:
    # To create window, bricks, ball, Remain-lives board and paddle. Then to initialize the mouse listeners.
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create lives remaining board
        self.num_lives = 0
        self.lives_board = GLabel('Lives remain: ' + str(self.num_lives))
        self.lives_board.font = '-20'
        self.window.add(self.lives_board, x=10, y=self.lives_board.height+10)


        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width - paddle_width)//2,
                        y=(window_height - paddle_height - paddle_offset))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width - ball_radius * 2)//2, y=(window_height - ball_radius * 2)//2)

        self.bricks_num = brick_cols * brick_rows  

        # Draw bricks
        for i in range(0, brick_cols * (brick_width + brick_spacing), (brick_width + brick_spacing)):
            for j in range(brick_offset, (brick_offset+brick_rows*(brick_height+brick_spacing)), (brick_height+brick_spacing)):
                self.bricks = GRect(brick_width, brick_height, x=i, y=j)
                self.bricks.filled = True
                self.bricks.fill_color = 'red'
                self.bricks.color = 'red'
                self.window.add(self.bricks)

        for i in range(0, brick_cols * (brick_width + brick_spacing), (brick_width + brick_spacing)):
            for j in range(brick_offset+2*(brick_height + brick_spacing), (brick_offset+4*(brick_height + brick_spacing))
                           , (brick_height + brick_spacing)):
                self.bricks = GRect(brick_width, brick_height, x=i, y=j)
                self.bricks.filled = True
                self.bricks.fill_color = 'orange'
                self.bricks.color = 'orange'
                self.window.add(self.bricks)

        for i in range(0, brick_cols * (brick_width + brick_spacing), (brick_width + brick_spacing)):
            for j in range(brick_offset+4*(brick_height + brick_spacing), (brick_offset+6*(brick_height + brick_spacing))
                           , (brick_height + brick_spacing)):
                self.bricks = GRect(brick_width, brick_height, x=i, y=j)
                self.bricks.filled = True
                self.bricks.fill_color = 'yellow'
                self.bricks.color = 'yellow'
                self.window.add(self.bricks)

        for i in range(0, brick_cols * (brick_width + brick_spacing), (brick_width + brick_spacing)):
            for j in range(brick_offset+6*(brick_height + brick_spacing), (brick_offset+8*(brick_height + brick_spacing))
                           , (brick_height + brick_spacing)):
                self.bricks = GRect(brick_width, brick_height, x=i, y=j)
                self.bricks.filled = True
                self.bricks.fill_color = 'green'
                self.bricks.color = 'green'
                self.window.add(self.bricks)

        for i in range(0, brick_cols * (brick_width + brick_spacing), (brick_width + brick_spacing)):
            for j in range(brick_offset+8*(brick_height + brick_spacing), (brick_offset+10*(brick_height + brick_spacing))
                           , (brick_height + brick_spacing)):
                self.bricks = GRect(brick_width, brick_height, x=i, y=j)
                self.bricks.filled = True
                self.bricks.fill_color = 'blue'
                self.bricks.color = 'blue'
                self.window.add(self.bricks)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        self.click = False

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start)

    def get_dx(self):
        """
        For user to get the dx
        """
        return self.__dx

    def get_dy(self):
        """
        For user to get the dx
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        For user to change the dx
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        For user to change the dy
        """
        self.__dy = new_dy

    def move_paddle(self, mouse):
        """
        Mouse controls the paddle
        """
        
        self.paddle.x = mouse.x-self.paddle.width//2  
        if mouse.x < self.paddle.width//2: 
            self.paddle.x = 0
        if mouse.x > self.window.width-self.paddle.width//2:  
            self.paddle.x = self.window.width-self.paddle.width

    def start(self, mouse):
        if not self.click:
            self.click = True  
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def set_lives(self, new_lives):
        # For user to change the number of lives
        self.num_lives = new_lives
        self.lives_board.text = 'Lives remain: ' + str(self.num_lives)  # ?

