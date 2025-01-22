class Solution:
    def myAtoi(self, s: str) -> int:
        trim, res = s.strip(), ""
        if trim == "":
            return 0

        if not trim[0].isdigit():
            if trim[0] == "+" or trim[0] == "-":
                res += trim[0]
                trim = trim[1:]
            else:
                return 0

        for i in trim:
            if i.isdigit():
                res += i
            else:
                break
        
        if not res[0].isdigit() and len(res) <= 1:
            return 0

        res = int(res)
        if res < (-2)**31:
            return (-2)**31
        elif res > (2**31) - 1:
            return (2**31) - 1

        return res