from graphics import CanvasWrapper
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.canvas.itemconfig(overlapping_object, fill='green')

def update(canvas, eraser):
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    canvas.moveto(eraser, mouse_x, mouse_y)
    
    erase_objects(canvas, eraser)

    # Call this function again after 50ms
    canvas.root.after(50, update, canvas, eraser)

def main():
    canvas = CanvasWrapper(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    eraser = canvas.create_rectangle(50, 50, 50 + ERASER_SIZE, 50 + ERASER_SIZE, 'black')

    # Start update loop
    update(canvas, eraser)
    
    canvas.run()

if __name__ == '__main__':
    main()
