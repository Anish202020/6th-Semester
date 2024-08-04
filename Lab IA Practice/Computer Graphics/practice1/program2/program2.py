import matplotlib.pyplot as plt
import numpy as np

def plot_polygon(polygon,title):
    plt.figure() # Imp
    plt.title(title) # Imp
    plt.gca().set_aspect('equal',adjustable='box') # Imp
    plt.grid(True) # Imp
    polygon = np.concatenate((polygon,[polygon[0]])) # Imp
    plt.plot(polygon[:,0],polygon[:,1],'b-') # Imp
    plt.plot(polygon[:-1,0],polygon[:-1,1],'bo')
    
    for i,(x,y) in enumerate(polygon[:-1]):
        plt.text(x,y,f'P{i}',ha='right')
    plt.show() # Imp
    
def translate_polygon(polygon):
    tx = float(input("Enter tx: "))
    ty = float(input("Enter ty: "))
    translated_polygon = polygon + np.array([tx,ty])
    return translated_polygon

def scale_polygon(polygon):
    sx = float(input("Enter sx: "))
    sy = float(input("Enter sy: "))
    scaled_polygon = polygon * np.array([sx,sy])
    return scaled_polygon

def rotate_polygon(polygon):
    angle_degrees = float(input("Enter angle: "))
    angle_radians = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians),-np.sin(angle_radians)],[np.sin(angle_radians),np.cos(angle_radians)]])
    rotated_polygon = np.dot(polygon,rotation_matrix)
    return rotated_polygon

def reflect_polygon_x_axis(polygon):
    reflected_polygon = np.array(polygon)
    reflected_polygon[:,1] = -reflected_polygon[:,1]
    return reflected_polygon


def main():
    polygon = np.array([[0,0],[5,0],[3,4],[2,3]])
    
    plot_polygon(polygon,'Original Polygon')
    
    while True:
        print("\nOptions:")
        print("1. Translate")
        print("2. Rotate")
        print("3. Scale")
        print("4. Reflect")
        print('5.Exiting')
        ch = input("Enter a choice(1-5)")
        if ch =='1':
            polygon = translate_polygon(polygon)
            plot_polygon(polygon,'Translated Polygon')
        elif ch=='2':
            polygon = rotate_polygon(polygon)
            plot_polygon(polygon,'Rotated Polygon')
        elif ch=='3':
            polygon = scale_polygon(polygon)
            plot_polygon(polygon,'Scaled Polygon')
        elif ch=='4':
            polygon = reflect_polygon_x_axis(polygon)
            plot_polygon(polygon,'Reflect Polygon')
        elif ch=='5':
            break
        else:
            print("Invalid choice")
            break
        print('Exiting...')
        
if __name__ =="__main__":
    main()
        