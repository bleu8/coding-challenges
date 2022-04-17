# add two numbers:

# https://leetcode.com/problems/two-sum/

# arr1=[1,2,4,5]
# target1=3
# def two_sum(arr,target):

#     values=dict()
#     for i ,el in enumerate(arr):
#         comp=target-el

#         if comp in values:

            
#             return [values[comp],i]

#         values[el]=i
#     return []

# list1=two_sum(arr1,target1)
# print(list1)


class Solution(object):
    def twoSum(self, nums, target):
      for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            if sum ==target:
                return [i,j]


