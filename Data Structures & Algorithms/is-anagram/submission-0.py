class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 0
        length = len(s)
        letters = []
        while counter < length:
            letters.append(s[counter])
            counter += 1 
        length = len(t)
        counter = 0
        letters2 = []
        while counter < length:
            letters2.append(t[counter])
            counter += 1
        if sorted(letters) == sorted(letters2):
            return True
        return False