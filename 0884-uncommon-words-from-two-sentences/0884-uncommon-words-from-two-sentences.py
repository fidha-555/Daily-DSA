class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        all_words = (s1 + " "+ s2).split()
        count = {}
        for word in all_words:
            if word in count:
                count[word]+=1
            else:
                count[word] = 1
            result = []
            for word in count:
                if count[word] ==1:
                    result.append(word)
        return result
        