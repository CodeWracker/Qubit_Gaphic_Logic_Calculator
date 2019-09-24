# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')

# Make Bloch Spheare
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

#|a> = cos(teta/2)|0> + e^iro *sin(teta/2) |1>                                                                                                                                          
#teta = 90-arcsin(c/b)
#ro = 90-arsin(a/b)
'''
cos((pi/2 - arcsin(c/b))/2 ) = val|0>
arccos(val|0>) = (pi/2 - arcsin(c/b))/2
arcsin(c/b) = pi/2 - 2*arccos(val|0>)
c/b = sin(pi/2 - arcos(val|0>))

e^i(pi/2 - arcsin(a/b)) * sin((pi/2 - arcsin(c/b)/2)) = val|1>

'''
