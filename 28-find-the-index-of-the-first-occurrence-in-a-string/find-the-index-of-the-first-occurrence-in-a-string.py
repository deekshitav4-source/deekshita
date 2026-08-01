class Solution(object):
    def strStr(self, haystack, needle ):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        lenh,lenn= len(haystack), len(needle)
        for i in range (lenh- lenn+1):
            if haystack[i:i+ lenn]== needle:
                return i
        return -1