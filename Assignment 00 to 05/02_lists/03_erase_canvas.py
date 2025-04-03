import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x, mouse_y = canvas.winfo_pointerx() - canvas.winfo_rootx(), canvas.winfo_pointery() - canvas.winfo_rooty()
    left_x, top_y = mouse_x, mouse_y
    right_x, bottom_y = left_x + ERASER_SIZE, top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white', outline='white')

def update_eraser(canvas, eraser):
    mouse_x, mouse_y = canvas.winfo_pointerx() - canvas.winfo_rootx(), canvas.winfo_pointery() - canvas.winfo_rooty()
    canvas.coords(eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
    erase_objects(canvas, eraser)
    canvas.after(50, update_eraser, canvas, eraser)

def main():
    root = tk.Tk()
    root.title("Eraser Grid")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
    canvas.pack()
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline='black')
    
    canvas.bind("<Button-1>", lambda event: start_eraser(event, canvas))
    
    root.mainloop()

def start_eraser(event, canvas):
    eraser = canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill='pink', outline='pink')
    update_eraser(canvas, eraser)

if __name__ == '__main__':
    main()