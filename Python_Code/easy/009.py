'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        tempV = x
        newV = 0
        while tempV != 0:
            newV = newV * 10 + tempV % 10
            tempV = int(tempV/10)
        if newV == x: return True
        return False

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
