import matplotlib.pyplot as plt
import numpy as np

def plot_rectangle(vertices,title):
    plt.figure()
    plt.gca().set_aspect('equal',adjustable='box')
    plt.title(title)
    plt.grid(True)
    
    rectangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(rectangle[:,0],rectangle[:,1],'b-')
    plt.show()
    
def plot_triangle(vertices,title):
    plt.figure()
    plt.gca().set_aspect('equal',adjustable='box')
    plt.title(title)
    plt.grid(True)
    
    triangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(triangle[:,0],triangle[:,1],'b-')
    plt.show()

def translate_object(vertices,tx,ty):
    translated_object = vertices+ np.array([tx,ty])
    return translated_object
def scale_object(vertices,sx,sy):
    scaled_object = vertices* np.array([sx,sy])
    return scaled_object
def rotate_object(vertices,angle_degrees):
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians),-np.sin(angle_radians)],[np.sin(angle_radians),np.cos(angle_radians)]])
    rotated_object = np.dot(vertices,rotation_matrix)
    return rotated_object

def reflect_x_axis(vertices):
    reflected_x_axis = np.array(vertices)
    reflected_x_axis[:,1] = -reflected_x_axis[:,1]
    return reflect_x_axis

def main():
    object = input("Either rectangle or triangle").lower()
    if object =='rectangle':
        vertices = np.array([[0,0],[2,0],[2,1],[0,1]])
        plot_polygon = plot_rectangle
    elif object =="triangle":    
        vertices = np.array([[0,0],[2,0],[2,1]])
        plot_polygon=plot_triangle
    else:
        print("Invalid input. Enter Triangle or Rectangle")
        return
    
    plot_polygon(vertices,'Original Polygon')
    
    while True:
        print("\nOptions:")
        print("1. Translate")
        print("2. Scale")
        print("3. Rotate")
        print("4. Reflect")
        print("5. Quit")
        choice = input("Enter a choice(1-5)")
        if choice == '1':
            tx = float(input("Enter translation along x-axis: "))
            ty = float(input("Enter translation along y-axis: "))
            vertices = translate_object(vertices, tx, ty)
        elif choice == '2':
            angle_degrees = float(input("Enter rotation angle in degrees: "))
            vertices = rotate_object(vertices, angle_degrees)
        elif choice == '3':
            sx = float(input("Enter scaling factor along x-axis: "))
            sy = float(input("Enter scaling factor along y-axis: "))
            vertices = scale_object(vertices, sx, sy)
        elif choice == '4':
            vertices = reflect_x_axis(vertices)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        # Plot the transformed shape
        plot_polygon(vertices, 'Transformed Shape')

    print("Exiting...")

if __name__ == "__main__":
    main()
    