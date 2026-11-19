class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for i in nums1:
            ans = -1

            index = nums2.index(i)

            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    ans = nums2[j]
                    break

            result.append(ans)

        return result