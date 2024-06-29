import matplotlib.pyplot as plt
import numpy as np

# Function to plot a rectangle
def plot_rectangle(vertices, title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Plot the rectangle
    rectangle = np.concatenate((vertices, [vertices[0]]))  # Close the rectangle
    plt.plot(rectangle[:, 0], rectangle[:, 1], 'b-')

    plt.show()

# Function to plot a triangle
def plot_triangle(vertices, title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Plot the triangle
    triangle = np.concatenate((vertices, [vertices[0]]))  # Close the triangle
    plt.plot(triangle[:, 0], triangle[:, 1], 'b-')

    plt.show()

# Function to translate a shape
def translate_shape(vertices, tx, ty):
    translated_vertices = vertices + np.array([tx, ty])
    return translated_vertices

# Function to rotate a shape (around the origin)
def rotate_shape(vertices, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                 [np.sin(angle_radians), np.cos(angle_radians)]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

# Function to scale a shape (around the origin)
def scale_shape(vertices, sx, sy):
    scaled_vertices = vertices * np.array([sx, sy])
    return scaled_vertices

# Function to reflect a shape over the x-axis
def reflect_shape_x_axis(vertices):
    reflected_vertices = np.array(vertices)
    reflected_vertices[:, 1] = -reflected_vertices[:, 1]
    return reflected_vertices

# Main function to demonstrate 2D transformations on basic shapes
def main():
    # Prompt user for the type of shape (rectangle or triangle)
    shape_type = input("Enter shape type (rectangle or triangle): ").lower()

    if shape_type == 'rectangle':
        # Define vertices of a rectangle
        vertices = np.array([[0, 0], [2, 0], [2, 1], [0, 1]])
        plot_function = plot_rectangle
    elif shape_type == 'triangle':
        # Define vertices of a triangle
        vertices = np.array([[0, 0], [2, 0], [1, 2]])
        plot_function = plot_triangle
    else:
        print("Invalid shape type. Please choose 'rectangle' or 'triangle'.")
        return

    # Plot the original shape
    plot_function(vertices, 'Original Shape')

    # Prompt user for the type of transformation
    while True:
        print("\nChoose a transformation:")
        print("1. Translate")
        print("2. Rotate")
        print("3. Scale")
        print("4. Reflect over x-axis")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            tx = float(input("Enter translation along x-axis: "))
            ty = float(input("Enter translation along y-axis: "))
            vertices = translate_shape(vertices, tx, ty)
        elif choice == '2':
            angle_degrees = float(input("Enter rotation angle in degrees: "))
            vertices = rotate_shape(vertices, angle_degrees)
        elif choice == '3':
            sx = float(input("Enter scaling factor along x-axis: "))
            sy = float(input("Enter scaling factor along y-axis: "))
            vertices = scale_shape(vertices, sx, sy)
        elif choice == '4':
            vertices = reflect_shape_x_axis(vertices)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        # Plot the transformed shape
        plot_function(vertices, 'Transformed Shape')

    print("Exiting...")

if __name__ == "__main__":
    main()
