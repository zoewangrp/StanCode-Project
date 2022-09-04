"""
File: babygraphics.py
Name: Zoe
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_interval = (width - GRAPH_MARGIN_SIZE*2)//len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + line_interval*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # top fixed horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # bottom fixed horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # vertical lines indicates Years
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    rank_level_height = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            name = lookup_names[i]
            year_rank_dict = name_data[name]
            for j in range(len(YEARS)):
                if str(YEARS[j]) not in year_rank_dict:
                    year_rank_dict[str(YEARS[j])] = str(MAX_RANK+1)
            # To get the x, y coordinates for drawing lines and locating texts
            for k in range(len(YEARS)-1):
                x0 = get_x_coordinate(CANVAS_WIDTH, k)
                x1 = get_x_coordinate(CANVAS_WIDTH, k+1)
                year0 = str(YEARS[k])
                year1 = str(YEARS[k+1])
                rank0 = year_rank_dict[year0]
                rank1 = year_rank_dict[year1]
                y0 = GRAPH_MARGIN_SIZE+(int(rank0)-1)*rank_level_height
                y1 = GRAPH_MARGIN_SIZE+(int(rank1)-1)*rank_level_height
                if rank0 == str(MAX_RANK + 1):
                    rank0 = '*'
                if rank1 == str(MAX_RANK + 1):
                    rank1 = '*'
                if len(lookup_names) > len(COLORS):
                    color = COLORS[i-len(COLORS)]
                else:
                    color = COLORS[i]
                canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=color)
                canvas.create_text(x0+TEXT_DX, y0, text=name + rank0, anchor=tkinter.SW, fill=color)
                canvas.create_text(x1+TEXT_DX, y1, text=name + rank1, anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
