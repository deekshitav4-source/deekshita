class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False 
        if x == 0:
            return True
        if x % 10 == 0:
            return False 
        originalx = x
        numreversed = 0    
        while x > 0:
            lastdigit = x % 10
            numreversed = numreversed * 10 + lastdigit
            x= x//10
        return numreversed == originalx