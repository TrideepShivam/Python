#write a python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. 
# sample list : ['abc','xyz','aba','1221']
#expected Result : 2
list = ['abca','xyzx','aba','122']
count = 0
for x in list:
    if x[0]==x[-1]:
        count+=1
print("total words are:",count)