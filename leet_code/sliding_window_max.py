'''
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the
very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''

import collections
import heapq


class Solution(object):
    # Use double-ended-queue
    # put number index into deque. d[0] contains the index of the biggest one
    # O(n) time,  O(k)space
    def maxSlidingWindow_deque(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []
        d = collections.deque()

        for i, n in enumerate(nums):
            # if n > d[-1], clear d
            while d and nums[d[-1]] < n:
                d.pop()

            d.append(i)

            if d[0] == i - k:
                d.popleft()

            if i >= k - 1:
                res.append(nums[d[0]])

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
print s.maxSlidingWindow_deque(nums, k)
