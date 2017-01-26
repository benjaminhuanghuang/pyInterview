'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''


class Solution(object):
    def searchInsert_niave_niave(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0

        if target == nums[-1]:
            return len(nums) - 1

        if target > nums[-1]:
            return len(nums)

        for i in xrange(len(nums) - 1):
            if nums[i] < target and target <= nums[i + 1]:
                return i + 1
        return -1

    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return right + 1


s = Solution()
print s.searchInsert([1, 3], 2)

print s.searchInsert([1, 3], 3)
