"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution:
    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            x = 1/x
            n = -n
        if n%2==0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x, n-1)


class Solution1:
    def myPow(self, x, n):
        if n<0:
            x = 1/x
            n = -n
        retval = 1
        while n!=0:
            if n%2 !=0:
                retval = retval*x
            x = x*x
            n = n//2
        return retval
            
        

print(Solution1().myPow(2,10))

