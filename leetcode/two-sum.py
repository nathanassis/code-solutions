class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}

        for i, n in enumerate(nums):
            ans = target - n
            if ans in hash:
                return [hash[ans], i]
            hash[n] = i