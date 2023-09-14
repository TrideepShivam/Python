import numpy as np
arr = np.array([4,5,6,7,8,9,10,11,12])
reshapedArr=arr.reshape(3,3)
print(reshapedArr)
print("diagonal elements are:")
sum = 0
for i in range(0,3):
    print(reshapedArr[i][i])      
    sum+=reshapedArr[i][i]
print("sum of diagonal is:")
print(sum) 