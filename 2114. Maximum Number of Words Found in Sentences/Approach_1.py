
class Solution:
    def mostWordsFound(self, sentences):
        maximum = 0

        for i in sentences:
            count = len(i.split())

            if count > maximum:
                maximum = count

        return maximum
