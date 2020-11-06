class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        up, down = 0, 0
        M = 10**9 + 7

        while p1 < len(nums1) or p2 < len(nums2):
            if p1 == len(nums1):
                down += nums2[p2]
                p2 += 1
            elif p2 == len(nums2):
                up += nums1[p1]
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                up += nums1[p1]
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                down += nums2[p2]
                p2 += 1
            elif nums1[p1] == nums2[p2]:
                up = max(up, down) + nums1[p1]
                down = up
                p1 += 1
                p2 += 1
        return max(down, up) % M
