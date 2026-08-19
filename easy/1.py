class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in mp:
                return [mp[x], i]
            mp[num] = i
