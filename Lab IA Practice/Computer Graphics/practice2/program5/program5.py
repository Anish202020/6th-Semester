import matplotlib.pyplot as plt
import numpy as np

def plot_3d_object(vertices,title):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.set_title(title)
    
    for i in range(len(vertices)):
        ax.scatter(vertices[i,0],vertices[i,1],vertices[i,2],color='b')
        ax.text(vertices[i,0],vertices[i,1],vertices[i,2],f'P{i}',ha='right')
    
    edges = [[0,1,2,3,0],[4,5,6,7,4],[0,4],[1,5],[2,6],[3,7]]
    
    for edge in edges:
        ax.plot(vertices[edge,0],vertices[edge,1],vertices[edge,2],color='r')
    
    plt.show
    
vertices = np.array([
                    [0,0,0],
                    [1,0,0],
                    [1,1,0],
                    [0,1,0],
                    [0,0,1],
                    [1,0,1],
                    [1,1,1],
                    [0,1,1],
                    ])