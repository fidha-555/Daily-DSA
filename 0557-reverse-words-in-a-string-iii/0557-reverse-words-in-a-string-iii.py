class Solution:
    def reverseWords(self, s: str) -> str:
        res =[]
        words = s.split(" ")
        for w in words:
            res.append(w[::-1])
        return " ".join(res)
       
        