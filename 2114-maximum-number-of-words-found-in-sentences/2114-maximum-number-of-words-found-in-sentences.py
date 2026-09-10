class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        no_of_words = 0
        for s in sentences:
            words = s.split(" ")
            if no_of_words < len(words):
                no_of_words = len(words)
        return no_of_words



        