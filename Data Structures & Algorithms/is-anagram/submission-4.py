class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list_1 = [char for char in s]
        list_2 = [char for char in t]

        list_1.sort()
        list_2.sort()
        
        for i in range(len(list_1)):
            if list_1[i] == list_2[i]:
                continue
            else:
                return False
        return True