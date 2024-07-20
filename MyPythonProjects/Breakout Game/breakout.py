"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    while True:
        pause(FRAME_RATE)
        if lives == 0:
            graphics.reset_ball()
            graphics.game_start = False
            graphics.game_over()
        if graphics.get_dx() != 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            while True:
                pause(FRAME_RATE)
                if graphics.game_start:
                    graphics.ball.move(dx, dy)
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        dx = - dx
                    if graphics.ball.y <= 0:
                        dy = - dy
                    if graphics.window.height - graphics.ball.y <= graphics.ball.height:
                        graphics.reset_ball()
                        lives -= 1
                        break

                    # Check for collision with objects
                    obj = check_collision(graphics)
                    if obj is not None:
                        if obj is graphics.paddle:
                            dy = -dy
                        else:
                            graphics.window.remove(obj)
                            dy = -dy


def check_collision(graphics):
    # Check for collision at four corners of the ball
    for i in range(2):
        for j in range(2):
            obj = graphics.window.get_object_at(graphics.ball.x + i * graphics.ball.width,
                                                graphics.ball.y + j * graphics.ball.height)
            if obj is not None:
                return obj
    return obj


if __name__ == '__main__':
    main()
