import turtle

def draw_square(size, color):
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_triangle(size, color):
    turtle.color(color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def draw_circle(size, color):
    turtle.color(color)
    turtle.circle(size)

def clear_drawing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def main():
    turtle.speed(1)  # Set the drawing speed

    while True:
        shape = input("Enter the shape to draw (square, triangle, circle) or 'exit' to quit: ").lower()
        if shape == 'exit':
            break

        size = int(input("Enter the size of the shape: "))
        color = input("Enter the color of the shape: ")

        if shape == 'square':
            draw_square(size, color)
        elif shape == 'triangle':
            draw_triangle(size, color)
        elif shape == 'circle':
            draw_circle(size, color)
        else:
            print("Invalid shape. Please try again.")

        clear = input("Do you want to clear the drawing and start over? (yes/no): ").lower()
        if clear == 'yes':
            clear_drawing()

    turtle.done()

if __name__ == "__main__":
    main()
