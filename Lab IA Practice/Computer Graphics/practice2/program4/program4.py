import numpy as np
import matplotlib.pyplot as plt

def plot_rectangle(vertices,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    
    rectangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(rectangle[:,0],rectangle[:,1],color='b-')
    plt.plot(rectangle[:-1,0],rectangle[:-1,1],color='bo')
    for i,(x,y) in enumerate(vertices[:-1]):
        plt.text(x,y,f'P{i}',ha='right')
    plt.show()
    
def plot_triangle(vertices,title):
    plt.figure()
    plt.title(title)
    plt.gca().set_aspect('equal',adjustable='box')
    plt.grid(True)
    
    triangle = np.concatenate((vertices,[vertices[0]]))
    plt.plot(triangle[:,0],triangle[:,1],color='b-')
    plt.plot(triangle[:-1,0],triangle[:-1,1],color='bo')
    for i,(x,y) in enumerate(vertices[:-1]):
        plt.text(x,y,f'P{i}',ha='right')
    plt.show()