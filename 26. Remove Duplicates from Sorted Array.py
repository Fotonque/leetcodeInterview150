"""
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

nums = [1,1,2,3]

id = 1

for i in range(1, len(nums)): # first element always unique
    if nums[i] != nums[i-1]: # until different elements are found insert position do not change
        nums[id] = nums[i]
        id += 1

print(nums)
print(id)