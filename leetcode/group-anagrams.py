class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {str(sorted(strs[0])): [strs[0]]}
        for s in strs[1:]:
            s_sorted = str(sorted(s))
            if s_sorted in res:
                res[s_sorted].append(s)
            else:
                res[s_sorted] = [s]

        return res.values()