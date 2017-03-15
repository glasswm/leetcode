class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = -1
        else:
            flag = 1
        
        x = abs(x)
        rev_x = 0
        while x>0:
            rev_x = rev_x * 10
            tmp = x % 10
            rev_x += tmp
            x = x / 10
        
        if (rev_x > 2147483647):
            return 0
        return rev_x * flag
