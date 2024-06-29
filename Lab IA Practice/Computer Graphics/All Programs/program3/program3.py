import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to plot a 3D object
def plot_3d_object(vertices, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)

    # Plot vertices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

    # Connect vertices to form edges
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 4], [1, 4], [2, 4], [3, 4]]
    for edge in edges:
        ax.plot(vertices[edge, 0], vertices[edge, 1], vertices[edge, 2], color='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('auto')

    plt.show()

# Function to translate a 3D object
def translate_3d_object(vertices):
    tx = float(input("Enter translation along x-axis: "))
    ty = float(input("Enter translation along y-axis: "))
    tz = float(input("Enter translation along z-axis: "))
    translated_vertices = vertices + np.array([tx, ty, tz])
    return translated_vertices

# Function to rotate a 3D object around x-axis
def rotate_x_3d_object(vertices):
    angle_degrees = float(input("Enter rotation angle around x-axis in degrees: "))
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[1, 0, 0],
                                 [0, np.cos(angle_radians), -np.sin(angle_radians)],
                                 [0, np.sin(angle_radians), np.cos(angle_radians)]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

# Function to rotate a 3D object around y-axis
def rotate_y_3d_object(vertices):
    angle_degrees = float(input("Enter rotation angle around y-axis in degrees: "))
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), 0, np.sin(angle_radians)],
                                 [0, 1, 0],
                                 [-np.sin(angle_radians), 0, np.cos(angle_radians)]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

# Function to rotate a 3D object around z-axis
def rotate_z_3d_object(vertices):
    angle_degrees = float(input("Enter rotation angle around z-axis in degrees: "))
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians), 0],
                                 [np.sin(angle_radians), np.cos(angle_radians), 0],
                                 [0, 0, 1]])
    rotated_vertices = np.dot(vertices, rotation_matrix)
    return rotated_vertices

# Function to scale a 3D object
def scale_3d_object(vertices):
    sx = float(input("Enter scaling factor along x-axis: "))
    sy = float(input("Enter scaling factor along y-axis: "))
    sz = float(input("Enter scaling factor along z-axis: "))
    scaled_vertices = vertices * np.array([sx, sy, sz])
    return scaled_vertices

# Main function to demonstrate geometric operations on a 3D object
def main():
    # Define a simple 3D object as a numpy array of vertices
    vertices = np.array([[1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1], [0, 0, -1]])

    # Plot the original 3D object
    plot_3d_object(vertices, 'Original 3D Object')

    # Prompt user for the geometric operation
    while True:
        print("\nChoose a geometric operation:")
        print("1. Translate the 3D object")
        print("2. Rotate the 3D object around x-axis")
        print("3. Rotate the 3D object around y-axis")
        print("4. Rotate the 3D object around z-axis")
        print("5. Scale the 3D object")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            vertices = translate_3d_object(vertices)
        elif choice == '2':
            vertices = rotate_x_3d_object(vertices)
        elif choice == '3':
            vertices = rotate_y_3d_object(vertices)
        elif choice == '4':
            vertices = rotate_z_3d_object(vertices)
        elif choice == '5':
            vertices = scale_3d_object(vertices)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        # Plot the transformed 3D object
        plot_3d_object(vertices, 'Transformed 3D Object')

    print("Exiting...")

if __name__ == "__main__":
    main()
