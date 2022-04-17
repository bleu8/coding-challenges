def twoSum(nums,target):
    compMap=dict()
    for i in range(len(nums)):
        num=nums[i] #2
        comp=target-nums[i] #7

        if num in compMap:
            return [compMap[num],i]
        compMap[comp]=i
           
    



arr=[1,4,6,83]
print(twoSum(arr,5))

#https://www.youtube.com/watch?v=2uWRxgN1Sbo