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
    
def reflect_polygon_x_axis(polygon):
    reflected_polygon = np.array(polygon)
    reflected_polygon[:,1]=-reflected_polygon[:,1]
    return reflected_polygon