import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot a 3D object
def plot_3d_object(vertices, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)

    # Plot the 3D object
    for i in range(len(vertices)):
        ax.scatter(vertices[i, 0], vertices[i, 1], vertices[i, 2], color='b')
        ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], f'P{i}', ha='right')

    # Connect vertices to form edges of the object
    edges = [[0, 1, 2, 3, 0],
             [4, 5, 6, 7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    for edge in edges:
        ax.plot(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2], 'b-')

    plt.show()

# Function to translate a 3D object
def translate_3d_object(vertices, tx, ty, tz):
    translated_vertices = vertices + np.array([tx, ty, tz])
    return translated_vertices

# Function to rotate a 3D object around x, y, or z-axis
def rotate_3d_object(vertices, axis, angle_degrees):
    angle_radians = np.radians(angle_degrees)
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0],
                                     [0, np.cos(angle_radians), -np.sin(angle_radians)],
                                     [0, np.sin(angle_radians), np.cos(angle_radians)]])
    elif axis == 'y':
        rotation_matrix = np.array([[np.cos(angle_radians), 0, np.sin(angle_radians)],
                                     [0, 1, 0],
                                     [-np.sin(angle_radians), 0, np.cos(angle_radians)]])
    elif axis == 'z':
        rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), 0],
                                     [np.sin(angle_radians), np.cos(angle_radians), 0],
                                     [0, 0, 1]])
    else:
        print("Invalid axis. Rotation aborted.")
        return vertices

    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

# Function to scale a 3D object
def scale_3d_object(vertices, sx, sy, sz):
    scaled_vertices = vertices * np.array([sx, sy, sz])
    return scaled_vertices

# Function to reflect a 3D object over the xy-plane, yz-plane, or zx-plane
def reflect_3d_object(vertices, plane):
    if plane == 'xy':
        reflected_vertices = vertices * np.array([1, 1, -1])
    elif plane == 'yz':
        reflected_vertices = vertices * np.array([-1, 1, 1])
    elif plane == 'zx':
        reflected_vertices = vertices * np.array([1, -1, 1])
    else:
        print("Invalid plane. Reflection aborted.")
        return vertices

    return reflected_vertices

# Main function to demonstrate 3D transformations on a 3D object
def main():
    # Define vertices of a 3D object (e.g., cube)
    vertices = np.array([[0, 0, 0],
                          [1, 0, 0],
                          [1, 1, 0],
                          [0, 1, 0],
                          [0, 0, 1],
                          [1, 0, 1],
                          [1, 1, 1],
                          [0, 1, 1]])

    # Plot the original 3D object
    plot_3d_object(vertices, 'Original 3D Object')

    # Prompt user for the type of transformation
    while True:
        print("\nChoose a transformation:")
        print("1. Translate")
        print("2. Rotate")
        print("3. Scale")
        print("4. Reflect")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            tx = float(input("Enter translation along x-axis: "))
            ty = float(input("Enter translation along y-axis: "))
            tz = float(input("Enter translation along z-axis: "))
            vertices = translate_3d_object(vertices, tx, ty, tz)
        elif choice == '2':
            axis = input("Enter rotation axis (x, y, z): ")
            angle_degrees = float(input("Enter rotation angle in degrees: "))
            vertices = rotate_3d_object(vertices, axis, angle_degrees)
        elif choice == '3':
            sx = float(input("Enter scaling factor along x-axis: "))
            sy = float(input("Enter scaling factor along y-axis: "))
            sz = float(input("Enter scaling factor along z-axis: "))
            vertices = scale_3d_object(vertices, sx, sy, sz)
        elif choice == '4':
            plane = input("Enter reflection plane (xy, yz, zx): ")
            vertices = reflect_3d_object(vertices, plane)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        # Plot the transformed 3D object
        plot_3d_object(vertices, 'Transformed 3D Object')

    print("Exiting...")

if __name__ == "__main__":
    main()
