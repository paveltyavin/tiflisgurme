import os
from PIL.ImageDraw import Image, Draw

PINK = (229, 91, 79)
BORD = (146, 41, 53)
YELLOW = (253, 246, 236)
VIOLET = (240, 225, 250)


def hex():
    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/hex.png')
    im = Image.new("RGBA", (18, 25), )
    draw = Draw(im)
    for (x1, y1, x2, y2) in [
        (17, 4, 9, 0),
        (17, 12, 9, 16,),
        (1, 4, 8, 0),
        (1, 12, 8, 16),
        (0, 4, 0, 12),
        (9, 16, 9, 24),
    ]:
        draw.line(((x1, y1), (x2, y2)), VIOLET, width=1)
    im.save(file_name)

    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/hex_bord.png')
    im = Image.new("RGBA", (18, 25))
    draw = Draw(im)
    for (x1, y1, x2, y2) in [
        (17, 4, 9, 0),
        (17, 12, 9, 16,),
        (1, 4, 8, 0),
        (1, 12, 8, 16),
        (0, 4, 0, 12),
        (9, 16, 9, 24),
    ]:
        draw.line(((x1, y1), (x2, y2)), BORD, width=1)
    im.save(file_name)


def ribbon():
    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/ribbon_white.png')
    im = Image.new("RGBA", (500, 60), )
    draw = Draw(im)
    file_name_2 = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/ribbon_pink.png')
    im_2 = Image.new("RGBA", (500, 60), )
    draw_2 = Draw(im_2)

    for (x1, y1, x2, y2) in [
        (500, 0, 0, 0),
        (0, 0, 15, 30),
        (15, 30, 0, 59),
        (0, 59, 500, 59),
    ]:
        draw.line(((x1, y1), (x2, y2)), (255, 255, 255), width=1)
        draw_2.line(((x1, y1), (x2, y2)), PINK, width=1)
    im.save(file_name)
    im_2.save(file_name_2)


def angle():
    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/angle_bottom.png')
    im = Image.new("RGBA", (59, 15), )
    draw = Draw(im)
    for (x1, y1, x2, y2) in [
        (0, 0, 29, 14),
        (29, 14, 58, 0),
    ]:
        draw.line(((x1, y1), (x2, y2)), (255, 255, 255), width=1)
    im.save(file_name)

    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/angle_left.png')
    im = Image.new("RGBA", (30, 108), )
    draw = Draw(im)
    for (x1, y1, x2, y2) in [
        (28, 108, 1, 58),
        (1, 58, 28, 0),
    ]:
        draw.line(((x1, y1), (x2, y2)), (255, 255, 255), width=2)
    im.save(file_name)

    file_name = os.path.join(os.path.dirname(__file__), 'frontend/dist/img/angle_right.png')
    im = Image.new("RGBA", (30, 108), )
    draw = Draw(im)
    for (x1, y1, x2, y2) in [
        (1, 0, 28, 58),
        (28, 58, 1, 108),
    ]:
        draw.line(((x1, y1), (x2, y2)), (255, 255, 255), width=2)
    im.save(file_name)


if __name__ == '__main__':
    hex()
    ribbon()
    # angle()
