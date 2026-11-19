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




        
        