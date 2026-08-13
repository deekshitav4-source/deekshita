class Solution(object):
    def addBinary(self, a, b):
            r = ""
            carry = 0    
            a,b = a[::-1],b[::-1]
            for i in range(max(len(a),len(b))):
                digitA = ord(a[i]) - ord("0") if i<len(a) else 0
                digitb= ord(b[i]) - ord("0") if i< len(b) else 0  
                total = digitA + digitb +carry
                char= str(total%2)
                r= char +r
                carry = total//2
            if carry:
                r="1"+r
            return r

        