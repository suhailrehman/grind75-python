
# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring

# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every 
# character in t (including duplicates) is included in 
# the window. If there is no such substring, return the 
# empty string "".

def minWindow(s: str, t: str):
    map = dict()




##### FAILED ATTEMPT
## Doesnt slide the window correctly; returns length of string substring always

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map = {k: False for k in t} # Initialize Hashmap for checking t in windows of s
        i, w_start, w_end = 0,0,0
        shortest_indices = (0,len(s))
        
        while w_end < len(s) :
            # Check if current value is of interest
            if s[w_end] in hash_map.keys():
                hash_map[s[w_end]] = True
            
            # Check if valid substring
            if all(hash_map.values()):
                if w_end-w_start < shortest_indices[1] - shortest_indices[0]:
                    shortest_indices = (w_start,w_end)
            
            # Slide window end
            w_end +=1
                
            # Now decide if we need to move the start of the window
            if s[w_start] not in hash_map.keys(): # Always move if not possibly start of sequence
                w_start += 1
            else:
                # Possible start of sequence, decide if current window length is longer than min
                if w_end - w_start > shortest_indices[1] - shortest_indices[0]:
                    hash_map[s[w_start]] = False
                    w_start +=1
                    if s[w_start] in hash_map.keys():
                        hash_map[s[w_start]] = True
                        
            return s[shortest_indices[0]:shortest_indices[1]]