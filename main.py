from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

# Test Code #
draw_line(0, 0, 499, 499, screen, color)
draw_line(1, 1, 100, 10, screen, color)
draw_line(1, 1, 500, 1, screen, color)
draw_line(50, 50, 200, 150, screen, color)
draw_line(100, 60, 400, 200, screen, color)

display(screen)
save_extension(screen, 'img.png')
