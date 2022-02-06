class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = [x for x in s.split(" ") if len(x) > 0]
        return len(s1[-1])