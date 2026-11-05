import numpy as np

d1 = np.arange(1,10)
# print(d1)

d2 = np.arange(12).reshape(4,3)
# print(d2)

# d1 = np.append(d1,100)
# print(d1)

# d2 = np.append(d2,[[10,20,30]],axis=0)
# print(d2)

# d2 = np.append(d2,[[19,20,21]],axis=0)
# print(d2)

#  Row replace karne ka Tarika

# d2[4] = [1,2,3]
# print(d2)

#  Jab 2d array me append karna ho to

# d2 = np.append(d2,[[1],[4],[7],[9],[6],[4]],axis=1)
# print(d2)


a2 = np.arange(12,24).reshape(4,3)
# print(np.concat((a2,d2),axis=1))

# print(np.unique(a2))

# print(np.expand_dims(d1,axis=0).shape)

# print(np.where(d2 > 5,"Land Le","Chhod Rahe De"))

