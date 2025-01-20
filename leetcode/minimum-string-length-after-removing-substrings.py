class Solution:
    def minLength(self, s: str) -> int:
        tam = len(s)
        s = s.replace('AB', '').replace('CD', '')

        while tam != len(s):
            tam = len(s)
            s = s.replace('AB', '').replace('CD', '')

        return len(s)