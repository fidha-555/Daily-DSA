class Solution:
    def reverseWords(self, s: str) -> str:
        a =""
        b =[]
        for i in range(len(s)):
            if s[i] == ' ':
                a = a[::-1] + " "
                b.append(a)
                a=""
            else:
                a += s[i]
        b.append(a[::-1])
           
        return "".join(b)   


        
        