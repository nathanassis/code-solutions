class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        res = ""
        i = 0
        while num > 0:
            curr = num % 10
            symbol = ""
            if curr == 4 or curr == 9:
                symbol = roman[1 * 10**i] + roman[(curr + 1) * 10**i]
            elif curr >= 5:
                symbol = roman[5 * 10**i] + roman[1 * 10**i] * (curr - 5)
            elif 0 < curr < 5:
                symbol = roman[1 * 10**i] * curr

            res += symbol[::-1]
            i += 1
            num //= 10

        return res[::-1]
