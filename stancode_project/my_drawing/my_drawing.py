"""
File: Kanahei
Name: 王柔蘋
----------------------
My favorite rabbit and little bird in the world~~~ Kanahei: Piske & Usagi
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(600, 600, color='gold', title='KANAHEI')


def main():
    """
    This code is to create different parts of the KANAHEI figures.
    """
    # Background
    background = GRect(900, 600)
    background.filled =True
    background.fill_color = 'lightblue'
    background.color = 'lightblue'
    window.add(background)

    background1 = GOval(600, 600, x=0, y=300)
    background1.filled = True
    background1.fill_color = 'lightseagreen'
    background1.color = 'lightseagreen'
    window.add(background1)

    # Clouds
    cloud = GOval(500, 330, x=-300, y=-200)
    cloud.filled = True
    cloud.fill_color = 'white'
    cloud.color = 'white'
    window.add(cloud)

    cloud1 = GOval(300, 300, x=50, y=-200)
    cloud1.filled = True
    cloud1.fill_color = 'white'
    cloud1.color = 'white'
    window.add(cloud1)

    cloud2 = GOval(300, 300, x=200, y=-200)
    cloud2.filled = True
    cloud2.fill_color = 'white'
    cloud2.color = 'white'
    window.add(cloud2)

    # Sun

    sun = GOval(300, 300, x=400, y=-150)
    sun.filled = True
    sun.fill_color = 'gold'
    sun.color = 'gold'
    window.add(sun)


    # mountains
    mt1 = GOval(100, 80, x=30, y=550)
    mt1.filled = True
    mt1.fill_color = 'green'
    mt1.color = 'green'
    window.add(mt1)

    mt2 = GOval(80, 100, x=120, y=530)
    mt2.filled = True
    mt2.fill_color = 'green'
    mt2.color = 'green'
    window.add(mt2)

    mt3 = GOval(100, 80, x=180, y=550)
    mt3.filled = True
    mt3.fill_color = 'green'
    mt3.color = 'green'
    window.add(mt3)

    mt4 = GOval(80, 100, x=260, y=530)
    mt4.filled = True
    mt4.fill_color = 'green'
    mt4.color = 'green'
    window.add(mt4)

    mt5 = GOval(100, 80, x=320, y=550)
    mt5.filled = True
    mt5.fill_color = 'green'
    mt5.color = 'green'
    window.add(mt5)

    mt6 = GOval(80, 100, x=400, y=530)
    mt6.filled = True
    mt6.fill_color = 'green'
    mt6.color = 'green'
    window.add(mt6)

    mt7 = GOval(100, 80, x=460, y=550)
    mt7.filled = True
    mt7.fill_color = 'green'
    mt7.color = 'green'
    window.add(mt7)


    # Rabbit

    r_l_ear = GOval(30, 80, x=160, y=160)
    r_l_ear.filled = True
    r_l_ear.fill_color = 'pink'
    r_l_ear.color = 'pink'
    window.add(r_l_ear)

    r_r_ear = GOval(30, 80, x=220, y=160)
    r_r_ear.filled = 'pink'
    r_r_ear.fill_color = 'pink'
    r_r_ear.color = 'pink'
    window.add(r_r_ear)

    r_body = GRect(120, 120, x=140, y=300)
    r_body.filled = True
    r_body.fill_color = 'pink'
    r_body.color = 'pink'
    window.add(r_body)

    r_body1 = GArc(120, 150, 0, -180, x=140, y=374)
    r_body1.filled = True
    r_body1.fill_color = 'pink'
    r_body1.color = 'pink'
    window.add(r_body1)

    r_belly = GOval(45, 45, x=178, y=360)
    r_belly.filled = True
    r_belly.fill_color = 'white'
    r_belly.color = 'white'
    window.add(r_belly)

    r_belly1 = GRect(45, 30, x=178, y=380)
    r_belly1.filled = True
    r_belly1.fill_color = 'white'
    r_belly1.color = 'white'
    window.add(r_belly1)

    r_belly2 = GArc(45, 45, 0, -180, x=178, y=400)
    r_belly2.filled = True
    r_belly2.fill_color = 'white'
    r_belly2.color = 'white'
    window.add(r_belly2)

    r_l_foot = GOval(15, 40, x=170, y=430)
    r_l_foot.filled = True
    r_l_foot.fill_color = 'pink'
    r_l_foot.color = 'pink'
    window.add(r_l_foot)

    r_r_foot = GOval(15, 40, x=220, y=430)
    r_r_foot.filled = True
    r_r_foot.fill_color = 'pink'
    r_r_foot.color = 'pink'
    window.add(r_r_foot)

    r_head = GOval(200, 150, x=100, y=200)
    r_head.filled = True
    r_head.fill_color = 'pink'
    r_head.color = 'pink'
    window.add(r_head)

    r_l_eye = GOval(15, 8, x=165, y=270)
    r_l_eye.filled = True
    r_l_eye.fill_color = 'black'
    r_l_eye.color = 'black'
    window.add(r_l_eye)

    r_r_eye = GOval(15, 8, x=225, y=270)
    r_r_eye.filled = True
    r_r_eye.fill_color = 'black'
    r_r_eye.color = 'black'
    window.add(r_r_eye)

    r_mouth1 = GOval(60, 65, x=174, y=270)
    r_mouth1.filled = True
    r_mouth1.fill_color = 'white'
    r_mouth1.color = 'white'
    window.add(r_mouth1)

    r_l_beard = GArc(30, 110, 0, -140, x=176, y=255)
    r_l_beard.color = 'saddlebrown'
    window.add(r_l_beard)

    r_r_beard = GArc(30, 110, 180, 140, x=204, y=255)
    r_r_beard.color = 'saddlebrown'
    window.add(r_r_beard)

    r_mouth2 = GArc(15, 60, 0, -180, x=196, y=290)
    r_mouth2.color = 'saddlebrown'
    window.add(r_mouth2)

    r_chin = GLine(200, 330, 210, 330)
    r_chin.color = 'saddlebrown'
    window.add(r_chin)

    r_nose = GOval(15, 15, x=195, y=270)
    r_nose.filled = True
    r_nose.fill_color = 'saddlebrown'
    r_nose.color = 'saddlebrown'
    window.add(r_nose)

    r_l_blush = GOval(30, 30, x=130, y=280)
    r_l_blush.filled = True
    r_l_blush.color = 'lightpink'
    r_l_blush.fill_color = 'lightpink'
    window.add(r_l_blush)

    r_r_blush = GOval(30, 30, x=245, y=280)
    r_r_blush.filled = True
    r_r_blush.color = 'lightpink'
    r_r_blush.fill_color = 'lightpink'
    window.add(r_r_blush)

    r_l_hand = GOval(70, 20, x=100, y=340)
    r_l_hand.filled = True
    r_l_hand.fill_color = 'pink'
    r_l_hand.color = 'pink'
    window.add(r_l_hand)

    r_r_hand = GOval(70, 20, x=230, y=340)
    r_r_hand.filled = True
    r_r_hand.fill_color = 'pink'
    r_r_hand.color = 'pink'
    window.add(r_r_hand)



    # Bird

    b_body1 = GOval(150, 150, x=350, y=250)
    b_body1.filled = True
    b_body1.fill_color = 'white'
    b_body1.color = 'white'
    window.add(b_body1)

    b_body2 = GRect(140, 100, x=355, y=300)
    b_body2.filled = True
    b_body2.fill_color = 'white'
    b_body2.color = 'white'
    window.add(b_body2)

    b_l_foot1 = GLine(400, 400, 400, 450)
    b_l_foot1.color = 'saddlebrown'
    window.add(b_l_foot1)

    b_l_foot2 = GLine(390, 450, 400, 435)
    b_l_foot2.color = 'saddlebrown'
    window.add(b_l_foot2)

    b_l_foot3 = GLine(400, 435, 410, 450)
    b_l_foot3.color = 'saddlebrown'
    window.add(b_l_foot3)

    b_r_foot1 = GLine(450, 400, 450, 450)
    b_r_foot1.color = 'saddlebrown'
    window.add(b_r_foot1)

    b_r_foot2 = GLine(440, 450, 450, 435)
    b_r_foot2.color = 'saddlebrown'
    window.add(b_r_foot2)

    b_r_foot3 = GLine(450, 435, 460, 450)
    b_r_foot3.color = 'saddlebrown'
    window.add(b_r_foot3)

    b_body3 = GArc(140, 100, 0, -180, x=355, y=370)
    b_body3.filled = True
    b_body3.fill_color = 'white'
    b_body3.color = 'white'
    window.add(b_body3)

    b_l_eye = GOval(10, 10, x=400, y=300)
    b_l_eye.filled = True
    b_l_eye.color = 'black'
    b_l_eye.filled = 'black'
    window.add(b_l_eye)

    b_r_eye = GOval(10, 10, x=440, y=300)
    b_r_eye.filled = True
    b_r_eye.color = 'black'
    b_r_eye.filled = 'black'
    window.add(b_r_eye)

    b_mouth1 = GOval(25, 15, x=412, y=300)
    b_mouth1.filled = True
    b_mouth1.color = 'yellow'
    b_mouth1.fill_color = 'yellow'
    window.add(b_mouth1)

    b_mouth2 = GOval(15, 15, x=417, y=315)
    b_mouth2.filled = True
    b_mouth2.color = 'yellow'
    b_mouth2.fill_color = 'yellow'
    window.add(b_mouth2)

    b_l_blush = GOval(30, 30, x=370, y=315)
    b_l_blush.filled = True
    b_l_blush.color = 'lightpink'
    b_l_blush.fill_color = 'lightpink'
    window.add(b_l_blush)

    b_r_blush = GOval(30, 30, x=450, y=315)
    b_r_blush.filled = True
    b_r_blush.color = 'lightpink'
    b_r_blush.fill_color = 'lightpink'
    window.add(b_r_blush)

    b_l_hand = GOval(50, 20, x=320, y=340)
    b_l_hand.filled = True
    b_l_hand.fill_color = 'white'
    b_l_hand.color = 'white'
    window.add(b_l_hand)

    b_r_hand = GOval(50, 20, x=480, y=340)
    b_r_hand.filled = True
    b_r_hand.fill_color = 'white'
    b_r_hand.color = 'white'
    window.add(b_r_hand)

if __name__ == '__main__':
    main()
