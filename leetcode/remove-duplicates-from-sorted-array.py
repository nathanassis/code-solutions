class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos, i = 0, 0

        while i < len(nums):
            aux = nums.count(nums[i])
            nums[pos] = nums[i]
            pos += 1
            i += aux
        
        return pos