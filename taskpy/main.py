import rectangle
import tkinter as tk


def draw_rectangles(canvas, rect1, rect2):
    canvas.create_rectangle(rect1.x, rect1.y, rect1.x + rect1.width, rect1.y - rect1.height, outline="blue")
    canvas.create_rectangle(rect2.x, rect2.y, rect2.x + rect2.width, rect2.y - rect2.height, outline="red")

def check_interactions(rect1, rect2):
    contains = rect1.contains(rect2)
    intersect = rect1.intersect(rect2)
    return contains, intersect

def main():

    root = tk.Tk()
    root.title("Rectangle Interactions")

    # I commented on pairs of rectangles with different positions relative to each other for testing

    # Two intersecting rectangles
    rect1 = rectangle.Rectangle(50, 150, 100, 100)
    rect2 = rectangle.Rectangle(75, 175, 100, 100)

    # Two independent rectangles
    #rect1 = rectangle.Rectangle(50, 150, 100, 70)
    #rect2 = rectangle.Rectangle(175, 150, 121, 80)

    # Two rectangles in the same place
    #rect1 = rectangle.Rectangle(50, 150, 100, 70)
    #rect2 = rectangle.Rectangle(50, 150, 100, 70)

    # Situation when the other rectangle is inside the current rectangle
    #rect1 = rectangle.Rectangle(50, 200, 100, 100)
    #rect2 = rectangle.Rectangle(80, 150, 50, 10)

    # Situation where two rectangles intersect and have the same x coordinates
    #rect1 = rectangle.Rectangle(70, 100, 100, 60)
    #rect2 = rectangle.Rectangle(70, 150, 100, 60)

    # Situation where two rectangles intersect and have the same y coordinates
    #rect1 = rectangle.Rectangle(100, 150, 100, 60)
    #rect2 = rectangle.Rectangle(70, 150, 100, 60)

    # Two rectangles intersect at the same corner
    #rect1 = rectangle.Rectangle(170, 90, 100, 60)
    #rect2 = rectangle.Rectangle(70, 150, 100, 60)

    # Two rectangles have same one side
    #rect1 = rectangle.Rectangle(170, 150, 100, 60)
    #rect2 = rectangle.Rectangle(70, 150, 100, 60)

    
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    draw_rectangles(canvas, rect1, rect2)
    contains, intersect = check_interactions(rect1, rect2)

    contains_label = tk.Label(root, text=f"Contains: {contains}")
    contains_label.pack()

    intersect_label = tk.Label(root, text=f"Intersect: {intersect}")
    intersect_label.pack()

    root.mainloop()



if __name__ == "__main__":
    main()