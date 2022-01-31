from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")
    #Sun
    draw_oval(canvas, 0, 500, 100, 400, width=0, fill="yellow")

    #Clouds
    draw_oval(canvas, 275, 350, 725, 400, outline="", fill="white")
    draw_oval(canvas, 300, 340, 450, 410, outline="", fill="white")
    draw_oval(canvas, 350, 330, 425, 425, outline="", fill="white")
    draw_oval(canvas, 385, 315, 550, 450, outline="", fill="white")
    draw_oval(canvas, 400, 340, 630, 425, outline="", fill="white")

    # Bird 1
    draw_polygon(canvas, 200, 420, 180, 412, 180, 420, outline="", fill="#B03615")
    draw_polygon(canvas, 200, 420, 210, 420, 210, 440, outline="", fill="#B03615")
    draw_polygon(canvas, 225, 425, 228, 432, 240, 431, outline="", fill="yellow")
    draw_oval(canvas, 190, 412, 220, 430, outline="", fill="#E34E26")
    draw_oval(canvas, 214, 420, 231, 435, outline="", fill="#F14C20")
    draw_polygon(canvas, 200, 420, 210, 420, 193, 440, outline="", fill="#B03615")
    draw_oval(canvas, 223, 430, 226, 433, outline="", fill="black")
   
    # Bird 2
    draw_polygon(canvas, 170, 390, 150, 382, 150, 390, outline="", fill="#B03615")
    draw_polygon(canvas, 170, 390, 180, 390, 180, 410, outline="", fill="#B03615")
    draw_polygon(canvas, 195, 395, 198, 402, 210, 401, outline="", fill="yellow")
    draw_oval(canvas, 160, 382, 190, 400, outline="", fill="#E34E26")
    draw_oval(canvas, 184, 390, 201, 405, outline="", fill="#F14C20")
    draw_polygon(canvas, 170, 390, 180, 390, 163, 410, outline="", fill="#B03615")
    draw_oval(canvas, 193, 400, 196, 403, outline="", fill="black")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

    # Grass
    diameter = 30
    space = -12
    interval = diameter + space
    x = 0
    y = 145
    for i in range(50):
        draw_rectangle(canvas, x, y, x +10, y + diameter, outline="", fill="green")
        x += interval
    ######   
    diameter = 25
    space = -10
    interval = diameter + space
    x = 0
    y = 145
    for i in range(100):
        draw_rectangle(canvas, x, y, x +10, y + diameter, outline="#374B18", fill="green")
        x += interval
    ######
    diameter = 20
    space = -8
    interval = diameter + space
    x = 0
    y = 145
    for i in range(100):
        draw_rectangle(canvas, x, y, x +10, y + diameter, outline="#374B18", fill="green")
        x += interval
    ######
    diameter = 15
    space = -6
    interval = diameter + space
    x = 0
    y = 145
    for i in range(100):
        draw_rectangle(canvas, x, y, x +10, y + diameter, outline="#374B18", fill="green")
        x += interval
    ######
    diameter = 10
    space = 10
    interval = diameter + space
    x = 0
    y = 145
    for i in range(70):
        draw_rectangle(canvas, x, y, x +10, y + diameter, outline="#374B18", fill="green")
        x += interval

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # House
    draw_rectangle(canvas, 300, 140, 700, 150, outline="", fill="green")
    draw_polygon(canvas, 275, 275, 500, 275, 525, 320, 350, 320, fill="#C0392B")
    draw_rectangle(canvas, 450,150,700,275, width=1, fill="#AAB7B8")
    draw_rectangle(canvas, 300,150,450,275, width=1, fill="#AAB7B8")
    draw_rectangle(canvas, 325,150,425,250, width=1, fill="#4D5656")
    draw_rectangle(canvas, 550,150,600,225, width=1, fill="#7E5109")
    draw_oval(canvas, 590, 180, 595, 185, fill="black")
    draw_rectangle(canvas, 475,175,525,225, width=1, outline="black", fill="#2471A3")
    draw_rectangle(canvas, 625,175,675,225, width=1, outline="black", fill="#2471A3")
    draw_line(canvas, 475,200, 525, 200, width=1, fill="black")
    draw_line(canvas, 500,175, 500, 225, width=1, fill="black")
    draw_line(canvas, 625,200,675,200, width=1, fill="black")
    draw_line(canvas, 650,175,650,225, width=1, fill="black")
    draw_line(canvas, 370, 160, 380, 160, width=2, fill="black")
    draw_polygon(canvas, 435, 275, 715, 275, 575, 400, fill="#C0392B")
    draw_oval(canvas, 550, 300, 600, 350, outline="black", fill="#2471A3")
    draw_line(canvas, 575,300,575,350, width=1, fill="black")
    draw_line(canvas, 550,325,600,325, width=1, fill="black")
    draw_polygon(canvas, 550, 150, 600, 150, 625, 0, 525, 0, fill="#AC9F7F")
    draw_polygon(canvas, 325, 150, 425, 150, 450, 0, 300, 0, fill="#AC9F7F")
    

def draw_pine_tree(canvas, center_x, bottom, height):
 
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

#def draw_house(canvas, center_x, bottom, height):

    


def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Call the main function so that
# this program will start executing.
main()