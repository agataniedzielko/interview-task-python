from dataclasses import dataclass


@dataclass
class Rectangle:
    # I would like to draw the results in my code to make it easier to check whether what the functions returns is correct,
    # so I take it into account in the coordinate marking and conditions - the y axis increases in the opposite direction than standard.
    x: float  # x-coordinate of the bottom left corner 
    y: float  # y-coordinate of the bottom left corner
    width: float  # width of the rectangle
    height: float  # height of the rectangle

    def contains(self, other: "Rectangle") -> bool:
         # Calculate the coordinates of the other rectangle's corners
        other_x1 = other.x
        other_x2 = other.x + other.width #top right corner
        other_y1 = other.y
        other_y2 = other.y - other.height #top right corner

        # Check if all corners of the other rectangle are in the current rectangle
        return (
            self.x <= other_x1
            and self.x + self.width >= other_x2
            and self.y >= other_y1
            and self.y - self.height <= other_y2
        )

    def intersect(self, other: "Rectangle") -> bool:
        # Calculate the coordinates of the other rectangle's corners
        other_x1 = other.x
        other_x2 = other.x + other.width
        other_y1 = other.y
        other_y2 = other.y - other.height

        # Check if the rectangles do not intersect
        if (
            self.x > other_x2 
            or self.x + self.width < other_x1
            or self.y < other_y2 
            or self.y - self.height > other_y1
        ):
            return False
        # Situation when the other rectangle is inside the current rectangle
        elif (
            self.x < other_x1
            and self.x + self.width > other_x2
            and self.y > other_y2
            and self.y - self.height < other_y1
        ):
            return False
        else:
            return True

            