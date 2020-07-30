'''
343. 整数拆分
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
'''

class Solution:

    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        hashMap = {}
        return self._intergerBreakWithMap(n, hashMap)

    def _intergerBreakWithMap(self, n: int, hashMap: {}) -> int: 
        res = 0
        for i in range(1, n): 
            if hashMap.hasKey(i):
                res = hashMap[i]
            else:
                res = max(res, max(i * self._intergerBreakWithMap(n - i, hashMap), i * (n - i)))
                hashMap[i] = res
        return res

print(Solution().integerBreak(8))
