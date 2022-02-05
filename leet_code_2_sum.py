class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

a = Solution()
b = a.twoSum([2,3,3,2],5)
print(b)