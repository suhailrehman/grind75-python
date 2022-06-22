### O(n) solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 1
            else:
                s_map[char] += 1
        
        for char in t:
            if char not in s_map:
                return False
            else:
                s_map[char] -= 1
        
        if any(s_map.values()):
            return False
        
        return True

### Non optimal Solution nlog(n) * 2
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
'''