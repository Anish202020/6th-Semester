import matplotlib.pyplot as plt
import numpy as np

# Function to plot a polygon
def plot_polygon(polygon, title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    # Plot the polygon
    polygon = np.concatenate((polygon, [polygon[0]])) # Close the polygon
    plt.plot(polygon[:, 0], polygon[:, 1], 'b-')
    # Plot vertices
    plt.plot(polygon[:-1, 0], polygon[:-1, 1], 'bo')
    for i, (x, y) in enumerate(polygon[:-1]):
        plt.text(x, y, f'P{i}', ha='right')
    plt.show()

# Function to translate a polygon
def translate_polygon(polygon):
    tx = float(input("Enter translation along x-axis: "))
    ty = float(input("Enter translation along y-axis: "))
    translated_polygon = polygon + np.array([tx, ty])
    return translated_polygon

# Function to rotate a polygon
def rotate_polygon(polygon):
    angle_degrees = float(input("Enter rotation angle in degrees: "))
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],[np.sin(angle_radians), np.cos(angle_radians)]])
    rotated_polygon = np.dot(polygon, rotation_matrix)
    return rotated_polygon
    
# Function to scale a polygon
def scale_polygon(polygon):
    sx = float(input("Enter scaling factor along x-axis: "))
    sy = float(input("Enter scaling factor along y-axis: "))
    scaled_polygon = polygon * np.array([sx, sy])
    return scaled_polygon
    
# Function to reflect a polygon over x-axis
def reflect_polygon_x_axis(polygon):
    reflected_polygon = np.array(polygon)
    reflected_polygon[:, 1] = -reflected_polygon[:, 1]
    return reflected_polygon

# Main function to demonstrate geometric operations
def main():
    # Define a simple polygon as a list of vertices (x, y)
    polygon = np.array([[2, 2], [5, 4], [7, 6], [4, 8], [1, 6]])
    # Plot the original polygon
    plot_polygon(polygon, 'Original Polygon')
    # Prompt user for the geometric operation

    while True:
        print("\nChoose a geometric operation:")
        print("1. Translate the polygon")
        print("2. Rotate the polygon")
        print("3. Scale the polygon")
        print("4. Reflect the polygon over x-axis")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            polygon = translate_polygon(polygon)
        elif choice == '2':
            polygon = rotate_polygon(polygon)
        elif choice == '3':
            polygon = scale_polygon(polygon)
        elif choice == '4':
            polygon = reflect_polygon_x_axis(polygon)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        # Plot the transformed polygon
        plot_polygon(polygon, 'Transformed Polygon')
        print("Exiting...")
if __name__ == "__main__":
    main()