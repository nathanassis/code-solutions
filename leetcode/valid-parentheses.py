class Solution:
    def isValid(self, string: str) -> bool:        
        buffer = ""
        combinations = {'(': ')', '[': ']', '{': '}'}
        
        for s in string:
            if not s in combinations.keys():
                if len(buffer) == 0 or not combinations[buffer[-1]] == s:
                    return False
                else:
                    buffer = buffer[:-1]
            else:
                buffer += s
        
        if buffer == "":
            return True
        return False
            