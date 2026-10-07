class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        balanced = 0
    
        for letter in s:
            if letter  == 'R':
                r_count += 1
            elif letter == 'L':
                l_count += 1
            if r_count == l_count:
                balanced += 1
        return balanced

        