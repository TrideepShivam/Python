import numpy as np
nums = np.array([[5.54,3.38,7.99],[3.54,4.38,6.99],[1.54,2.39,9.29]])
print(nums)
n=5
l=np.array(nums[nums>5])
n=7
r=np.array(nums[nums<7])

print(np.subtract(nums,l))