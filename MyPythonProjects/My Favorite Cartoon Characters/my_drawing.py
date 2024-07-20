"""
File: my_drawing.py
Name: Felisa Wu
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Crayon ShinChan
    This is my favorite cartoon- Crayon ShinChan.
    I love this cartoon for its unique humor, relatable characters,
    and the heartwarming yet hilarious portrayal of everyday family life.
    """
    window = GWindow(800, 400, title='Crayon ShinChan')

    face = GOval(200, 210, x=280, y=80)
    face.filled = True
    face.fill_color = 'navajowhite'
    face.color = 'navajowhite'
    window.add(face)

    chop = GOval(140, 120, x=395, y=150)
    chop.filled = True
    chop.fill_color = 'navajowhite'
    chop.color = 'navajowhite'
    window.add(chop)

    ear = GOval(50, 80, x=250, y=140)
    ear.filled = True
    ear.fill_color = 'navajowhite'
    ear.color = 'navajowhite'
    window.add(ear)

    l_eyebrow1 = GArc(250, 130, 120, 30)
    l_eyebrow1.filled = True
    l_eyebrow1.fill_color = 'black'
    l_eyebrow1.color = 'black'
    window.add(l_eyebrow1, x=335, y=120)

    l_eyebrow2 = GArc(250, 130, 30, 30)
    l_eyebrow2.filled = True
    l_eyebrow2.fill_color = 'black'
    l_eyebrow2.color = 'black'
    window.add(l_eyebrow2, x=275, y=120)

    r_eyebrow1 = GArc(250, 130, 120, 30)
    r_eyebrow1.filled = True
    r_eyebrow1.fill_color = 'black'
    r_eyebrow1.color = 'black'
    window.add(r_eyebrow1, x=420, y=115)

    r_eyebrow2 = GArc(250, 130, 30, 30)
    r_eyebrow2.filled = True
    r_eyebrow2.fill_color = 'black'
    r_eyebrow2.color = 'black'
    window.add(r_eyebrow2, x=360, y=115)

    l_eye = GOval(40, 40, x=350, y=160)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    l_eye.color = 'black'
    window.add(l_eye)

    r_eye = GOval(40, 40, x=420, y=155)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    r_eye.color = 'black'
    window.add(r_eye)

    l_eyeball = GOval(20, 20, x=360, y=170)
    l_eyeball.filled = True
    l_eyeball.fill_color = 'white'
    l_eyeball.color = 'white'
    window.add(l_eyeball)

    r_eyeball = GOval(20, 20, x=430, y=165)
    r_eyeball.filled = True
    r_eyeball.fill_color = 'white'
    r_eyeball.color = 'white'
    window.add(r_eyeball)

    mouth = GOval(30, 30, x=430, y=250)
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'red'
    window.add(mouth)

    m_hair = GArc(165, 80, 0, 210)
    m_hair.filled = True
    m_hair.fill_color = 'black'
    m_hair.color = 'black'
    window.add(m_hair, x=290, y=80)

    l_hair = GArc(80, 100, 30, 180)
    l_hair.filled = True
    l_hair.fill_color = 'black'
    l_hair.color = 'black'
    window.add(l_hair, x=280, y=95)

    blush = GOval(50, 10, x=300, y=210)
    blush.filled = True
    blush.fill_color = 'pink'
    blush.color = 'pink'
    window.add(blush)

    rect = GRect(200, 60, x=300, y=320)
    rect.filled = True
    rect.fill_color = 'blue'
    rect.color = 'grey'
    window.add(rect)

    label = GLabel('Shin Chan', x=320, y=370)
    label.font = '-30'
    label.color = 'white'
    window.add(label)


if __name__ == '__main__':
    main()
