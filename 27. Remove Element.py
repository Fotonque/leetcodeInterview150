"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

by creating the "last" variable we get the last position of the array
if j-th element is val we swap j-th and last elements
"""



nums = [0,1,2,2,3,0,4,2]
val = 2

last = len(nums)-1
j = 0
copies = 0
for i in range(len(nums)):
    if nums[j] == val:
        tmp = nums[last]
        nums[last] = nums[j]
        nums[j] = tmp
        last -=1
        copies += 1
    else:
        j += 1

print(copies)
print(nums)