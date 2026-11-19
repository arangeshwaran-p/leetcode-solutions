# 3. Longest Substring Without Repeating Characters

### Difficulty: Medium

## Description
Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


Example 2:


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


 
Constraints:


	0 <= s.length <= 105
	s consists of English letters, digits, symbols and spaces.

## Submission Details
- **Status**: Accepted
- **Runtime**: 2979
- **Memory**: 19604000
- **Language**: python3

## Code
```python3
class Solution:
    def lengthOfLongestSubstring(self, s):
        ans = 0

        for i in range(len(s)):
            sub = ""

            for j in range(i, len(s)):
                if s[j] not in sub:
                    sub += s[j]
                    ans = max(ans, len(sub))
                else:
                    break

        return ans




        
        
```
