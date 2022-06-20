
# Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring

# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every 
# character in t (including duplicates) is included in 
# the window. If there is no such substring, return the 
# empty string "".

def minWindow(s: str, t: str):
    map = dict()
