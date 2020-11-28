import matplotlib.pyplot as plt
import numpy as np

xv = np.array([0,0.5])
yv = np.array([0,0.46211716])

lxv, lyv = np.zeros(6), np.zeros(6)
for i in range(6) : 
  lxv[i] = xv[0] + i*(xv[1]-xv[0]) / 5
  # Your code to linearly interpolate for the value of lyv[i] goes here
  lyv[i] = 
  

# You should not need to modify anything from here onwards
plt.plot( lxv, lyv, 'ko' )
plt.savefig("interpolation.png")
