"""
File: draw_line.py
Name: Felisa Wu
-------------------------
TODO: Use two point to create a line.
First, click on the window and show a circle.
Second, when we click the second time, remove first circle and show a line link first and second click point.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
WINDOW = GWindow()
CLICK = 0
START_POINT = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_hole)


def draw_hole(event):
    global CLICK, START_POINT
    CLICK += 1
    if CLICK % 2 == 1:
        START_POINT = (event.x, event.y)
        hole = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        WINDOW.add(hole)
    else:
        end_point = (event.x, event.y)
        remove_hole = WINDOW.get_object_at(START_POINT[0], START_POINT[1])
        line = GLine(START_POINT[0], START_POINT[1], end_point[0], end_point[1])
        WINDOW.add(line)
        WINDOW.remove(remove_hole)
        START_POINT = None


if __name__ == "__main__":
    main()
