import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from pylab import *
import math

# # pip install matplotlib
# plt.axis([0,5,0,20])
# plt.title('My first plot')
# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.show()



# t = np.arange(0,2.5,0.1)
# y1 = np.sin(math.pi*t)
# y2 = np.sin(math.pi*t+math.pi/2)
# y3 = np.sin(math.pi*t-math.pi/2)

# plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'r-.')
# plt.show()


################### linechart
# t = np.arange(0.,1.,0.05)
# y1 = np.sin(2*np.pi*t)
# y2 = np.cos(2*np.pi*t)

# print(t.ndim)
# print(y1.ndim)
# plt.subplot(121) # column row & index
# plt.plot(t,y1,'b-.')
# plt.subplot(122)
# plt.plot(t,y2,'r--')
# plt.show()

###################
# plt.axis([0.5,5,0,20])
# plt.title('My first plot',fontsize=20,fontname='Times New Roman')
# plt.xlabel('Counting')
# plt.ylabel('Square values')
# plt.text(1,1.5,'First')
# plt.text(2,4.5,'Second')
# plt.text(3,9.5,'Third')
# plt.text(4,16.5,'Fourth')
# plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
# plt.grid(True)
# plt.legend(['First series'])
# plt.plot([1,2,3,4],[1,4,9,16],'ro')

###################
# index = np.arange(5)
# values1 = [5,7,3,4,6]
# std1 = [0.8,1,0.4,0.9,1.3]
# plt.title('A Horizontal Bar Chart')
# plt.barh(index,values1,xerr=std1,error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
# plt.yticks(index+0.4,['A','B','C','D','E'])
# plt.legend(loc=5)

################### bar chart
# index = np.arange(5)
# values1 = [5,7,3,4,6]
# values2 = [6,6,4,5,7]
# values3 = [5,6,5,4,6]
# bw = 0.2
# plt.axis([0,5,0,8])
# plt.title('A Multiseries Bar Chart',fontsize=20)
# plt.bar(index+bw,values1,bw,color='b')
# plt.bar(index+bw*2,values2,bw,color='g')
# plt.bar(index+3*bw,values3,bw,color='r')
# plt.xticks(index+1.5*bw,['A','B','C','D','E'])

###################
# data = {'series1':[1,3,4,3,5], 'series2':[2,4,5,2,4], 'series3':[3,2,3,1,3]}
# df = pd.DataFrame(data)
# df.plot(kind='bar')

###################
# series1 = np.array([3,4,5,3])
# series2 = np.array([1,2,2,5])
# series3 = np.array([2,3,3,4])
# index = np.arange(4)
# plt.axis([-0.5,3.5,0,15])
# plt.title('A Multiseries Stacked Bar Chart')
# plt.bar(index,series1,color='r')
# plt.bar(index,series2,color='b',bottom=series1)
# plt.bar(index,series3,color='g',bottom=(series2+series1))
# plt.xticks(index+0.4,['Jan18','Feb18','Mar18','Apr18'])


################### pie chart
# labels = ['Nokia','Samsung','Apple','Lumia']
# values = [10,30,45,15]
# colors = ['yellow','green','red','blue']
# plt.pie(values,labels=labels,colors=colors, autopct='%1.1f%%')
# plt.axis('equal')


################### 
# data = {'series1':[1,3,4,3,5],'series2':[2,4,5,2,4],'series3':[3,2,3,1,3]}
# df = pd.DataFrame(data)
# df['series1'].plot(kind='pie',figsize=(6,6))
# df['series2'].plot(kind='pie',figsize=(8,8))


###################  3d
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-2,2,0.1)
# Y = np.arange(-2,2,0.1)
# X,Y = np.meshgrid(X,Y)
# def f(x,y):
#     return (1 - y**5 + x**5)*np.exp(-x**2-y**2)
# ax.plot_surface(X,Y,f(X,Y), rstride=1, cstride=1)
# ax.view_init(elev=70,azim=0)

################### 
fig = plt.figure()
ax = Axes3D(fig)
xs = np.random.randint(30,40,100)
ys = np.random.randint(20,30,100)
zs = np.random.randint(10,20,100)
xs2 = np.random.randint(50,60,100)
ys2 = np.random.randint(30,40,100)
zs2 = np.random.randint(50,70,100)
xs3 = np.random.randint(10,30,100)
ys3 = np.random.randint(40,50,100)
zs3 = np.random.randint(40,50,100)
ax.scatter(xs,ys,zs)
ax.scatter(xs2,ys2,zs2,c='r',marker='^')
ax.scatter(xs3,ys3,zs3,c='g',marker='*')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')





plt.show()