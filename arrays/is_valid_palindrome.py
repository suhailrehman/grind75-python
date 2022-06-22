class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## Discussion
        # Two pointers, check if same char until crossover
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(s) - 1
        
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True


### Initial Solution
### Messy, uses stack and indexing issues
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## Discussion
        # I'm thinking stack based solution, since we can push and pop 
        # the characters in a natural order to check
        # The main question is when to stop pushing and start popping
        # intuitively, it needs to be at the middle of the word.
        # I'm concerned about off-by-one and integer division not being correct.
        # Palindromes by def should be even or the middle char is not considered when odd.
        # 3 letters = 0,1,2 ; 3/2 = 1.5 ; floor(n/2)
        # 4 letters = 0,1,2,3 ; 4/2 = 2 ; floor(n/2)
        
        s = ''.join(char for char in s if char.isalnum())
        n = len(s)
        i = 0
        stack = []
        
        for char in s:
            if i < (n // 2):
                stack.append(char.lower())
            elif (i == (n//2) and n % 2 != 0):
                i += 1
                continue
            else:
                if not stack:
                    return False
                if char.lower() != stack.pop():
                    return False
            i += 1
                    
        if stack:
            return False
            
        return True
'''