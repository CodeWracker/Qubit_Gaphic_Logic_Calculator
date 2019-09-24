# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from porta import *
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

def transformaQubit(qubit):
    teta = 2* np.arccos( math.sqrt(math.pow(qubit[0],2) + math.pow(qubit[1],2)) )
    ro = math.sqrt(math.pow(qubit[2],2) +math.pow(qubit[3],2))- math.sqrt(math.pow(qubit[0],2) + math.pow(qubit[1],2))
    epson =  math.sqrt(math.pow(qubit[0],2) + math.pow(qubit[1],2))
    Bx = np.cos(ro)*np.sin(teta)
    By = np.sin(ro)*np.sin(teta)
    Bz = np.cos(teta)
    print(teta)
    print(ro)
    print(qubit)
    return(Bx,By,Bz)

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')

# Make Bloch Spheare
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

'''
    |Qb> = a|0> + b|1>
    teta = 2arcos( arg(a) ) = 2arcos( sqrt(a^2 + b^2) )
    ro = arg(b) - arg(a) = sqrt(c^2 +d^2)-sqrt(a^2 + b^2)
    epson = arg(a )= sqrt(a^2 + b^2)
    x = cos(ro)sen(teta)
    y = sen(ro)sen(teta)
    z = cos(teta)
'''
qubit = []
print("|y> = (a+ib)|0> + (c+id)|1>")
qubit.append(float(input("a: ")))
qubit.append(float(input("b: ")))
qubit.append(float(input("c: ")))
qubit.append(float(input("d: ")))
Bloch =[]
bloch = transformaQubit(qubit)

for a in bloch:
    print(a)
print()
plt.xlabel('x')
plt.ylabel('y')
lineX = np.linspace(0,bloch[0],100)
lineY = np.linspace(0,bloch[1],100)
lineZ = np.linspace(0,bloch[2],100)
# Plot the surface
ax.plot_surface(x, y, z,rstride=4,cstride=4,alpha=0.3)
ax.plot(lineX, lineY, lineZ)
plt.pause(1)
plt.cla()

qubit = portaX(qubit)
bloch = transformaQubit(qubit)
lineX = np.linspace(0,bloch[0],100)
lineY = np.linspace(0,bloch[1],100)
lineZ = np.linspace(0,bloch[2],100)
ax.plot_surface(x, y, z,rstride=4,cstride=4,alpha=0.3)
ax.plot(lineX, lineY, lineZ)
plt.xlabel('x')
plt.ylabel('y')

plt.show()