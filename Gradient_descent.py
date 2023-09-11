import numpy as np
import matplotlib.pyplot as plt

def Y(x):
    return x**2

def dY(x):
    return 2*x

x=np.arange(-100,100,0.5)
y=Y(x)

learning_rate=0.01
epochs=1000
pos=(75,Y(75))


for _ in range(epochs):
    x_new=pos[0] - learning_rate*dY(pos[0])
    y_new=Y(x_new)
    pos=(x_new,y_new)
    plt.plot(x,y)
    plt.scatter(pos[0],pos[1],color='r')
    plt.pause(0.001)
    plt.clf()
