import matplotlib.pyplot as plt
import numpy as np

def plot_3d_polygon(vertices,title):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title(title)
    ax.scatter(vertices[:,0],vertices[:,1],vertices[:,2],color='b')
    
    edges =[[0,1],[1,2],[2,3],[3,0],[0,4],[1,4],[2,4],[3,4]]
    
    for edge in edges:
        ax.plot(vertices[edge,0],vertices[edge,1],vertices[edge,2],color='r')
        
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_aspect('auto')
    plt.show()