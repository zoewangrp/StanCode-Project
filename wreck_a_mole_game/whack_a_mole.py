"""
File: whack_a_mole.py
Name: Zoe
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

score = 0                                                       # 變數, 所以local要用時, 需要先呼叫global
score_label = GLabel('Score ='+str(score))
score_label.font = '-50'
window.add(score_label, x=0, y=score_label.height)


def main():
    onmouseclicked(wrack)
    while True:
        img = GImage('mole.png')
        img.x = random.randint(0, WINDOW_WIDTH-img.width)
        img.y = random.randint(0, WINDOW_HEIGHT-img.height)
        window.add(img)
        pause(DELAY)


def wrack(mouse):
    global score                                                # 呼叫全域變數 score
    maybe_mole = window.get_object_at(mouse.x, mouse.y)
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        score_label.text = 'Score =>' + str(score)              # label.text 更新原本的文字內容, 後面是要更新的內容


if __name__ == '__main__':
    main()
