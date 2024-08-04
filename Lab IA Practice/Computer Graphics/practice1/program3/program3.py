import numpy as np
import matplotlib.pyplot as plt

def plot_3d_object(vertices,title):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title(title)
    
    ax.scatter(vertices[:,0],vertices[:,1],vertices[:,2],color='b')
    
    edges = [[0,1],[1,2],[2,3],[3,0],[0,4],[1,4],[2,4],[3,4]]
    for edge in edges:
        ax.plot(vertices[edge,0],vertices[edge,1],vertices[edge,2],color='r')
        
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('auto')
    plt.show()
    
def translate_3d_object(vertices):
    tx = float(input("Enter translation along x-axis: "))
    ty = float(input("Enter translation along y-axis: "))
    tz = float(input("Enter translation along z-axis: "))
    translated_vertices = vertices + np.array([tx, ty, tz])
    return translated_vertices
def scale_3d_object(vertices):
    sx = float(input("Enter scaling along x-axis: "))
    sy = float(input("Enter scaling along y-axis: "))
    sz = float(input("Enter scaling along z-axis: "))
    scaled_vertices = vertices * np.array([sx, sy, sz])
    return scaled_vertices

def rotate_x_3d_object(vertices):
    angle_degree = float(input("Enter rotation angle around x axis in degree"))
    angle_radians = np.radians(angle_degree)
    rotation_matrix = np.array([[1,0,0],[0,np.cos(angle_radians),-np.sin(angle_radians)],[0,np.sin(angle_radians),np.cos(angle_radians)]])
    rotated_vertices = np.dot(vertices,rotation_matrix)
    return rotated_vertices

def rotate_y_3d_object(vertices):
    angle_degree = float(input("Enter rotation angle around y axis in degree"))
    angle_radians = np.radians(angle_degree)
    rotation_matrix = np.array([
                                [np.cos(angle_radians),0,np.sin(angle_radians)],
                                [0,1,0],
                                [-np.sin(angle_radians),0,np.cos(angle_radians)]
                            ])
    rotated_vertices = np.dot(vertices,rotation_matrix)
    return rotated_vertices


def rotate_z_3d_object(vertices):
    angle_degree = float(input("Enter rotation angle around z axis in degree"))
    angle_radians = np.radians(angle_degree)
    rotation_matrix = np.array([[1,0,0],[0,np.cos(angle_radians),-np.sin(angle_radians)],[0,np.sin(angle_radians),np.cos(angle_radians)]])
    rotated_vertices = np.dot(vertices,rotation_matrix)
    return rotated_vertices

def main():
    vertices = np.array([[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[0,0,-1]])
    
    plot_3d_object(vertices,'Original Polygon')
    
    while True:
        print("\nOptions:")
        print('1. Translate')
        print('2. Scale')
        print('3. Rotate X')
        print('4. Rotate Y')
        print('5. Rotate Z')
        print('6. Exit')
        ch = input("Enter a choice(1-5)")
        if ch =='1':
            translated_vertices = translate_3d_object(vertices)
            plot_3d_object(translated_vertices,'Translated Polygon')
        elif ch =='2':
            scaled_vertices = scale_3d_object(vertices)
            plot_3d_object(scaled_vertices,'Scaled Polygon')
        elif ch =='4':
            rotate_y_vertices = rotate_y_3d_object(vertices)
            plot_3d_object(rotate_y_vertices,'Rotate Y')
        elif ch =='5':
            rotate_z_vertices = rotate_z_3d_object(vertices)
            plot_3d_object(rotate_z_vertices,'Rotate Z')
        elif ch=='3':
            rotate_x_vertices = rotate_x_3d_object(vertices)
            plot_3d_object(rotate_x_vertices,'Rotate X')
        elif ch=='6':
            break
        else:
            print("Invalid choice")
        
    print('Exiting')
    
if __name__ =="__main__":
    main()

