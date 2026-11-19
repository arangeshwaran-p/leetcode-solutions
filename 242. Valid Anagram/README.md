# 242. Valid Anagram

### Difficulty: Easy

## Description
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:


Input: s = "anagram", t = "nagaram"

Output: true


Example 2:


Input: s = "rat", t = "car"

Output: false


 
Constraints:


	1 <= s.length, t.length <= 5 * 104
	s and t consist of lowercase English letters.


 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Submission Details
- **Status**: Accepted
- **Runtime**: 19
- **Memory**: 20396000
- **Language**: python3

## Code
```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
```
