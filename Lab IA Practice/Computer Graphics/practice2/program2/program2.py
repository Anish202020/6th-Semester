import matplotlib.pyplot as plt
import numpy as np

def plot_polygon(polygon,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    polygon = np.concatenate((polygon,[polygon[0]]))
    plt.plot(polygon[:,0],polygon[:,1],'b-')
    plt.plot(polygon[:-1,0],polygon[:-1,1],'bo')
    for i,(x,y) in enumerate(polygon[:-1]):
        plt.text(x,y,f'P{i}',ha='right')
    plt.show()
    
def translate_polygon(polygon):
    tx = float(input("Enter tx value"))
    ty = float(input("Enter ty value"))
    translated_polygon = polygon + np.array([tx,ty])
    return translated_polygon

def scale_polygon(polygon):
    sx = float(input("Enter sx value"))
    sy = float(input("Enter sy value"))
    scaled_polygon = polygon * np.array([sx,sy])
    return scaled_polygon

def rotate_polygon(polygon):
    degree = float(input("Enter rotation angle in degree"))
    angle_radian = np.radians(degree)
    rotation_matrix = np.array([[np.cos(angle_radian),-np.sin(angle_radian)],[np.sin(angle_radian),np.cos(angle_radian)]])
    rotated_polygon = np.dot(polygon,rotation_matrix)
    return rotated_polygon

def reflect_polygon_x_axis(polygon):
    reflected_polygon = np.array(polygon)
    reflected_polygon[:,1] = - reflected_polygon[:,1]
    return reflected_polygon

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
        
if __name__ =="__main__":
    main()