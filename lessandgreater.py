#wap to extract all numners from a given array less and greater than a specified number.
import numpy as np
nums = np.array([[5.54,3.38,7.99],[3.54,4.38,6.99],[1.54,2.39,9.29]])
print(nums)
n=5
print(nums[nums>n])
print(nums[nums<n])