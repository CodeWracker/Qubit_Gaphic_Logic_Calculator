# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')
a = 1/4
b = 1/math.sqrt(2)
c = 1/2
# Make Bloch Spheare
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
d =0

#|a> = cos(teta/2)|0> + (esin(teta/2))iro |1>                                                                                                                                          
#teta = 90-arcsin(c/b)
#ro = 90-arsin(a/b)

#isso fica no while

plt.cla()

teta = (np.pi/2)-np.arcsin(c/b)
ro = (np.pi/2)-np.arcsin(a/b)
qubit =[]
qubit.append( complex(np.cos(teta/2),0) )
qubit.append( np.exp(ro*complex(0,1))*np.sin(teta/2) )
strqb = str(qubit[0]) + "|0> + " + str(qubit[1]) + "|1>"
ax.set_title("|Qb> = {}".format(strqb))
print(teta)
print(ro)
print(qubit)
lineX = np.linspace(0,a,100)
lineY = np.linspace(0,b,100)
lineZ = np.linspace(0,c,100)
# Plot the surface
ax.plot_surface(x, y, z,rstride=4,cstride=4,alpha=0.3)
ax.plot(lineX, lineY, lineZ)
plt.pause(1)

# ate aqui o while

plt.xlabel('x')
plt.ylabel('y')
plt.show()