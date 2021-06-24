import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import math

# # pip install matplotlib
# plt.axis([0,5,0,20])
# plt.title('My first plot')
# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.show()



t = np.arange(0,2.5,0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t+math.pi/2)
y3 = np.sin(math.pi*t-math.pi/2)

plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'r-.')
plt.show()

