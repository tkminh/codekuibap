import numpy as np

arr = [1, 2, 3, 4]
arr2 = [9, 8, 7, 6]
arr_np = np.array([arr, arr2])
#print(arr_np)

# print(arr_np.ndim)
# print (arr_np.size)
# print (arr_np.itemsize)
# print(arr_np.shape)

# print(np.ones(5))
# print(np.arange(0,10))
# print(np.arange(0,10, 3))
# print(np.arange(0,10, 0.5))
# print(np.arange(0,10).reshape(5,2))

# print(np.random.random(4))

# print(arr*2)
# print(arr_np*2)

# A = np.array(range(3))
# B = np.array(range(4,7))
# print(A)
# print(B)
# print(A*B)
# print(A.dot(B))
# print(B.dot(A))

# print(A.mean())
# print(B.std())

# print(B[[0,1]])

# c = np.arange(10,20).reshape(2,5)
# print(c)
# #print(c.reshape(2,5))
# #print(c[1:3])
# #print(c.reshape(1, c.ndim * c.size))
# print(c[1,3:4])

# for i in c:
#     print(i)

# #print(np.apply_along_axis(lambda x: x+3, axis=0, arr=c))

# print(np.random.random(4))
# # print(np.random.random((4,4)))
# print(np.transpose(c))

a = np.array([0,1,2])
b = np.array([3,4,5])
c = np.array([6,7,8])

print(np.column_stack((a,b,c)))
print(np.row_stack((a,b,c)))

# print("########")
# F = np.arange(16).reshape((4, 4))
# print(F)
# [A1,A2,A3] = np.split(F,[2,3],axis=1)
# print(A1)
# print(A2)
# print(A3)

m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
print(m.shape)
print(n.shape)