import numpy as np 
arr = np.array([
    [32.1,34.5,40.2],
    [32.1,34.5,42.2],
    [32.1,34.5,46.2],
    [32.1,34.5,30.2],
    [32.1,34.5,36.2],
    [32.7,34.5,40.2],
    [32.1,34.5,40.9],
    [32.1,34.5,48.2],
    [32.1,34.5,40.5],
    [32.1,34.5,40.3],
    [32.1,34.5,40.7],
    [32.1,34.5,49.2]
])
ldata = []
for a in arr:
    ldata.append(np.average(a))

print(ldata)
print(ldata.index(max(ldata))+1)
print(ldata.index(min(ldata))+1)