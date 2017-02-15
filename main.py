from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# Test Code #
draw_line_octant1(0, 0, 499, 499, screen, color)
draw_line_octant1(1, 1, 100, 10, screen, color)
draw_line_octant1(1, 1, 500, 1, screen, color)
draw_line_octant1(50, 50, 200, 150, screen, color)
draw_line_octant1(100, 60, 400, 200, screen, color)


# Octant2 Test #
color[RED] = 255
color[GREEN] = 0
draw_line_o2(0, 0, 0, 499, screen, color)
draw_line_o2(0, 0, 10, 250, screen, color)
draw_line_o2(0, 0, 50, 300, screen, color)

display(screen)
save_extension(screen, 'img.png')
