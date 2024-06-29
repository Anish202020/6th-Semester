import turtle

def bresenham_line(x1, y1, x2, y2):
    # Calculate the deltas
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the step direction for each axis
    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1

    # Initialize the error term
    error = 2 * dy - dx

    # Initialize the line points
    line_points = []

    # Start at the first point
    x, y = x1, y1

    # Draw the line
    for _ in range(dx + 1):
        # Add the current point to the line
        line_points.append((x, y))

        # Update the error term and adjust the coordinates
        if error > 0:
            y += y_step
            error -= 2 * dx
        error += 2 * dy
        x += x_step

    return line_points

# Example usage
turtle.setup(500, 500)
turtle.speed(0)  # Fastest drawing speed

x1, y1 = 100, 100
x2, y2 = 400, 300

line_points = bresenham_line(x1, y1, x2, y2)

# Draw the line
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for x, y in line_points:
    turtle.goto(x, y)

turtle.exitonclick()