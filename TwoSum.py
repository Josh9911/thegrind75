class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through the indexes of the list
        for i in range (len(nums)):
            # iterate through each index of the list again
            for j in range(len(nums)):
                # if result is the sum of two iterations, return the indexes if the indexes of the indexes are not the same
                res = nums[i] + nums[j]
                if res == target and i != j :
                    return [i,j]

"""
The solution I did was to use a nested for loop to iterate through through each element twice and add it to each other, if the indexes of the element are the same, we do not consider that result. 

"""
