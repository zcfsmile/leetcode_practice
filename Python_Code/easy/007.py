'''
题目：
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例：
输入: 123
输出: 321

输入: -123
输出: -321

输入: 120
输出: 21

注意：
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

class Solution:

    '''
    整数取余
    '''
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        flag = 1 if x > 0 else -1
        res = 0
        while x != 0:
            res = res * 10 + (abs(x) % 10) * flag
            if res > INT_MAX or res < INT_MIN: 
                return 0
            x = int(x / 10)
        return res 

    '''
    字符串翻转
    '''
    def reverse2(self, x: int) -> int:
        tempS = str(x)
        newS = ''
        result = 0
        for s in reversed(tempS):
            newS += s

        if x >= 0:
            result = int(newS)
        else:
            result = int(newS[:-1]) * -1

        if result.bit_length() <= 31:
            return result
        else: 
            return 0

print(Solution().reverse2(-123))
