"""
File: bouncing_ball.py
Name: Felisa Wu
-------------------------
TODO: To simulate the process for a ball drop and bounce.
When the ball bounce, the speed will reduce 90%. It can be implemented for 3 times and stop at the start point after the third time.
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

bounce_count = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
window.add(ball, x=START_X, y=START_Y)
started = False
falling = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)


def bouncing_ball(event):
    global bounce_count, started, falling
    bounce_count += 1
    vy = 0
    ball.move(VX, vy)
    if bounce_count <= 3:
        while True:
            vy += GRAVITY
            ball.move(VX, vy)
            pause(DELAY)
            if ball.y + SIZE >= window.height:
                vy = -vy * REDUCE
                if vy > 0:
                    vy *= -1
                pause(DELAY)
            if ball.x > window.width:
                pause(DELAY)
                break
        window.add(ball, x=START_X, y=START_Y)
    else:
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
