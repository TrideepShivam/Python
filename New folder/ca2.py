import numpy as np 
arr = np.empty((8,8),'i')
for a in range(0,8):
    for e in range(0,8):
        if a%2==0 and e%2!=0 or a%2!=0 and e%2==0:
            arr[a][e]=1
        else:
            arr[a][e]=0

print(arr)