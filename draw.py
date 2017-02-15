from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    # General draw_line wrapper
    # Decides which octant_helper to call, modifies starting-ending points
    pass


def draw_line_octant1(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = 2*A + B
    while (x <= x1):
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += 2*B
        x += 1
        d += 2*A


def draw_line_octant2(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = A + 2*B
    while (y <= y1):
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2*A
        y += 1
        d += 2*B


def draw_line_octant7(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = A - 2*B
    while (y >= y1):
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B


def draw_line_octant8(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = 2*A - B
    while (x <= x1):
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A
