'''
339	Nested List Weight Sum

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
'''


class Solution(object):
    def list_weight(self, list):
        return self.helper(list, 1)

    def helper(self, list, depth):
        result = 0;
        for item in list:
            if isinstance(item, int):
                weight = item * depth
            else:
                weight = self.helper(item, depth + 1)
            result += weight

        return result


a = 1
print isinstance(a, int)

b = []
print isinstance(b, list)
