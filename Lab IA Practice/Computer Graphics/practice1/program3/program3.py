import numpy as np
import matplotlib.pyplot as plt

def plot_3d_object(vertices,title):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title(title)
    ax.scatter(vertices[:,0],vertices[:,1],vertices[:,2],color='b')
    edges=[[0,1],[1,2],[2,3],[3,0],[0,4],[1,4],[2,4],[3,4]]
    for edge in edges:
        ax.plot(vertices[edge,0],vertices[edge,1],vertices[edge,2],color='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('auto')
    plt.show()

def translate_3d_object(vertices):
    tx = float(input("Enter tx"))
    ty = float(input("Enter ty"))
    tz = float(input("Enter tz"))
    translated_3d_object = vertices + np.array(tx,ty,tz)
    return translated_3d_object

def rotate_x_3d_object(vertices):
    angle_degree=float(input("Enter degree"))
    angle_radian=np.radians(angle_degree)
    rotation_matrix=np.array([[1,0,0],[0,np.cos(angle_radian),-np.sin(angle_radian)],[0,np.sin(angle_radian),np.cos(angle_radian)]])
    rotated_vertices = np.dot(vertices,rotation_matrix)
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

def scale_3d_object(vertices):
    sx=float(input("Enter sx"))
    sy=float(input("Enter sy"))
    sz=float(input("Enter sz"))
    scaled_3d_object = vertices * np.array([sx,sy,sz])
    return scaled_3d_object

def main():
    vertices = np.array([[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[0,0,-1]])
    plot_3d_object(vertices,'Original 3D Object')
    while True:
        print("\nOption Below")
        print("1. Translate")
        print("2. X Rotate")
        print("3. Y Rotate")
        print("4. Z Rotate")
        print("5. Scale")
        print("6. Exit")
        choice = input("Enter a choice(1-6)")
        if choice =='1':
            vertices = translate_3d_object(vertices)
        elif choice=='2':
            vertices = rotate_x_3d_object(vertices)
        elif choice=='3':
            vertices = rotate_y_3d_object(vertices)
        elif choice=='4':
            vertices = rotate_z_3d_object(vertices)
        elif choice=='5':
            vertices = scale_3d_object(vertices)
        elif choice=='6':
            break
        else:
            print("Invalid Choice")
        plot_3d_object(vertices,'Transformed 3D Object')
    print('Exiting...')
    
if __name__=="__main__":
    main()
        
            