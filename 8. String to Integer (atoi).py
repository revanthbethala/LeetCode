class Solution:
    def myAtoi(self, s: str) -> int:
        digits = "0123456789"
        s=s.strip()
        if not s:
            return 0 
        sign=num=""
        if s[0]=="-"or s[0]=="+":
            sign+=s[0]
            s=s[1:]            
        for i in range(len(s)):
            if s[i] in digits:
                num+=s[i]
            else:
                break
        if not num:
            return 0
        result = int(sign+num)
        return max(-2**31,min(result,2**31-1))