'''
331. Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we
record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where #
represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a
binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas
such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false


Reference:
    https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/

'''


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for x in preorder.split(','):
            stack += [x]
            # cut leaves node from the serialized tree
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[:-3] + ['#']  # pop *3 and append #
        return len(stack) == 1 and stack[0] == '#'


s = Solution()
print s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
