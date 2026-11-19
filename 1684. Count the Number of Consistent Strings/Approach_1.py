
class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0

        for word in words:
            good = True

            for ch in word:
                if ch not in allowed:
                    good = False
                    break

            if good:
                count += 1

        return count
