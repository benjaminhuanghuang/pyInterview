'''
372. Super Pow

Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive
integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]


Result: 1024

'''

class Solution(object):
    # c % m = (a*b) % m = (a%m)*(b%m)
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        mod = 1337
        for bi in b[::-1]:
            ans = ans * a ** bi % mod
            a = a ** 10 % mod
        return ans

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        mod = 1337
        for bi in b[::-1]:
            ans = (ans% mod) * (a ** bi% mod) %mod
            a = (a %mod) ** 10 % mod
        return ans