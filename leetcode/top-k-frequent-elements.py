class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1
        return sorted(hash, key=hash.get, reverse=True)[:k]