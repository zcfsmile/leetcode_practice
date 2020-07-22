'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0 or x % 10 == 0: return False
        newX = 0
        while x > newX:
            newX = newX * 10 + x % 10
            x = int(x/10)
        return x == newX or x == int(newX / 10)

    def isPalindrome2(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        strX = str(x)
        startPoint = 0

        while startPoint < int(len(strX) / 2):
            if strX[startPoint] != strX[len(strX) - 1 - startPoint]: 
                 return False
            startPoint += 1
        return True

    def isPalindrome3(self, x: int) -> bool:
        if x < 0: return False
        strX = str(x)
        if strX == strX[::-1]:
            return True
        return False

print(Solution().isPalindrome3(1213))
