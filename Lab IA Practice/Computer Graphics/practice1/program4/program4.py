import matplotlib.pyplot as plt
import numpy as np

def plot_rectangle(vertices,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    rectangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(rectangle[:,0],rectangle[:,1],'b-')
    plt.show()
    
def plot_triangle(vertices,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    triangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(triangle[:,0],triangle[:,1],'b-')
    plt.show()
    
def translate_shape(vertices,tx,ty):
    translated_shape = vertices + np.array([tx,ty])
    return translated_shape

def rotate_shape(vertices,angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians),-np.sin(angle_radians)],[np.sin(angle_radians),np.cos(angle_radians)]])
    rotated_shape = np.dot(vertices,rotation_matrix)
    return rotated_shape

def scale_shape(vertices,sx,sy):
    scaled_shape = vertices * np.array([sx,sy])
    return scaled_shape

def reflect_shape_x_axis(vertices):
    reflected_vertices = np.array(vertices)
    reflected_vertices[:, 1] = -reflected_vertices[:, 1]
    return reflected_vertices

def main():
    shape_type = input("Enter a shape rectangle or triangle: ").lower()
    if shape_type =='rectangle':
        vertices = np.array([[0,0],[2,0],[2,1],[0,1]])
        plot_function = plot_rectangle
    elif shape_type =='triangle':
        vertices = np.array([[0,0],[2,0],[1,2]])
        plot_function = plot_triangle
    else:
        print("Invalid choice")
        return
    plot_function(vertices,'Original Shape')
    
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
