class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        flag = 0
        while n >= 1:
            tmp = n & 1
            if tmp == 1:
                flag += 1
                if flag == 2:
                    return False
            n = n >> 1
        return True


if __name__ == '__main__':

	s = Solution()
	print s.isPowerOfTwo(7)
