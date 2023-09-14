import numpy as np
students = [[15,0,17,0,18,0,3,11,18,20],[9,10,4,0,8,12,0,18,0,17],[16,6,0,2,10,0,11,0,9,5]]
for s in students:
    for e in range(0,10):
        if(s[e]==0):
            for x in range(e,9):
                s[x]=s[x+1]
            s[9]=0

print(students)