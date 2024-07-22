import numpy as np
import matplotlib.pyplot as plt 

def plot_3d_object(verticles,title):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title(title)
    
    ax.scatter(verticles[:,0],verticles[:,1],verticles[:,2],color='b')