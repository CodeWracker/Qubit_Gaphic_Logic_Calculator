# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z,rstride=4,cstride=4,alpha=0.3)

linez = np.linspace(0,(1/2),100)
linex = np.linspace(0,math.sqrt(2)/2,100) 
liney = np.linspace(0,1/2,100) 
'''for xa in linex:
    for ya in liney:
        for za in linez:
            a = math.sqrt((xa*xa)+(ya*ya)+(za*za))
            if (a == 1):
                print("--------------Certo-------------")
            else:
                if(a<1):
                    print("dentro")
                else:
                    print("errado: "+str(a))'''
print(linex)
print()
print(liney)
print()
print(linez)

ax.plot(linex, liney, linez)
plt.xlabel('x')
plt.ylabel('y')


plt.pause(0.5)
plt.cla()
ax.plot_surface(x, y, z,rstride=4,cstride=4,alpha=0.3)
linez = np.linspace(0,(1/4),100)
linex = np.linspace(0,math.sqrt(2)/2,100) 
liney = np.linspace(0,1/2,100) 
print(linex)
print()
print(liney)
print()
print(linez)
ax.plot(linex, liney, linez)

plt.show()