class Solution(object):
    def toHex(self, num):
        if num == 0: return "0"
        if num < 0: num = num + 2**32
        res = ""
        hexChar = "0123456789abcdef"
        while num > 0:
            rem = num % 16
            res = res + hexChar[rem]
            num = num // 16
        res = "".join(reversed(res))
        return res

        