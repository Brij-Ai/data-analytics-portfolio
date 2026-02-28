import numpy as np;

# arr = np.array([1,23,1]);
# print(arr)
# print(type(arr))

arr = np.array([2,13,4,24,5],str)
# print(arr.ndim)
arr2 = np.array([[[1,24,5],
                  [32,12,4],
                  [4,2,4]]])
# print(arr2.ndim)
# print(arr2.shape)
# print(arr.shape)
# print(arr);
# print(type(arr))
# print(arr [0])
# print(len(arr))

# print(arr2[0,1])
# print(arr)
# print(arr2[0,2,1])

# zero = np.zeros((3,3))
# print(zero)

# ones = np.ones((3,3),int)
# print(ones)
# print('----')
# strOnes = np.ones((4,5,2),str)
# print(strOnes)

# print('--------')
# mulDim = np.ones((2,2,2,3))
# print(mulDim)

# # Full 

# full = np.full((3,3),"Str")
# print(full)

randMat = np.random.randint(-9,4,(3,3));
print(randMat)

# Identity
idn = np.identity(6)
print(idn)