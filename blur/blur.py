"""
File: blur.py
Name: Zoe
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    This code is to blur the picture.
    """
    old_img = SimpleImage("smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img:jpg, the picture to be blurred.
    :return:jpg, the blurred picture.
    """
    old_img = SimpleImage("smiley-face.png")
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0

            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    neighbor_x = x+i
                    neighbor_y = y+j

                    if 0 <= neighbor_x < old_img.width:
                        if 0 <= neighbor_y < old_img.height:

                            neighbor_pixel = old_img.get_pixel(neighbor_x, neighbor_y)
                            r_sum += neighbor_pixel.red
                            g_sum += neighbor_pixel.green
                            b_sum += neighbor_pixel.blue
                            count += 1

            blurred_pixel = blurred.get_pixel(x, y)
            blurred_pixel.red = r_sum/count
            blurred_pixel.green = g_sum/count
            blurred_pixel.blue = b_sum/count
    return blurred




if __name__ == '__main__':
    main()
