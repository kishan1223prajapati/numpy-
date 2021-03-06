#NUMPY ARRAY JOIN
import numpy as np
print("Joining two 1D arrays using concatenate() function")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print("\n")
print("Joining two 2D arrays using concatenate() function")
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr5 = np.concatenate((arr3, arr4), axis=1)
print(arr5)
print("\n")
print("Joining Arrays Using stack() Functions")
arr = np.stack((arr1, arr2), axis=1)
print(arr)
print("\n")
print("Stacking along rows")
arr = np.hstack((arr1, arr2))
print(arr)
print("\n")
print("Stacking along columns")
arr = np.vstack((arr1, arr2))
print(arr)
print("Stacking along height (depth)")
arr = np.dstack((arr1, arr2))
print(arr)
