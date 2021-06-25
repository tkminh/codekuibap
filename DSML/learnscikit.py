# pip install scikit-learn
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn import linear_model

# iris = datasets.load_iris()
# # iris.data = size of sepal & petal
# x = iris.data[:,0] # x sepal length
# y = iris.data[:,1] # y sepal length
# u = iris.data[:,2] # x petal length
# v = iris.data[:,3] # y petal length
# species = iris.target
# x_reduced = PCA(n_components=3).fit_transform(iris.data)


# x_min, x_max = x.min() - .5,x.max() + .5
# y_min, y_max = y.min() - .5,y.max() + .5
# u_min, u_max = u.min() - .5,u.max() + .5
# u_min, v_max = v.min() - .5,v.max() + .5

# fig = plt.figure()
# ax = Axes3D(fig)
# #plt.scatter(x,y, c=species)
# #plt.scatter(u,v, c=species)
# ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2], c=species)
# ax.set_xlabel('First eigenvector')
# ax.set_ylabel('Second eigenvector')
# ax.set_zlabel('Third eigenvector')
# ax.w_xaxis.set_ticklabels(())
# ax.w_yaxis.set_ticklabels(())
# ax.w_zaxis.set_ticklabels(())

# plt.show()


##############
# np.random.seed(0)
# iris = datasets.load_iris()
# x = iris.data[:,:2]
# y = iris.target
# x_min, x_max = x[:,0].min() - .5,x[:,0].max() + .5
# y_min, y_max = x[:,1].min() - .5,x[:,1].max() + .5
# cmap_light = ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
# h = .02
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# knn = KNeighborsClassifier()
# knn.fit(x,y)
# Z = knn.predict(np.c_[xx.ravel(),yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.figure()
# plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

# plt.scatter(x[:,0],x[:,1],c=y)
# plt.xlim(xx.min(),xx.max())
# plt.ylim(yy.min(),yy.max())

# plt.show()


#
diabetes = datasets.load_diabetes()
print(diabetes.data[0])
# print(diabetes.data[0,:]) # lay hang 1, tat ca column
# print(diabetes.data[:,0]) # lay tat ca hang cua column 1
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
linreg = linear_model.LinearRegression()
linreg.fit(x_train,y_train)

print(linreg.coef_)
linreg.predict(x_test)
print(y_test)