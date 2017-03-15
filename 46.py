class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursive_p(prefix, nnums):
            if len(nnums) <= 1:
                res = [prefix + nnums]
            else:
                res = []
                for i in range(0, len(nnums)):
                    if i == 0:
                        #print 'here', nnums
                        del_i = nnums[1:]
                    elif i == len(nnums)-1:
                        del_i = nnums[:-1]
                    else:
                        del_i = nnums[:i] + nnums[i+1:]
                    #print prefix + [nnums[i]],  del_i
                    res += recursive_p(prefix + [nnums[i]],  del_i)
            return res

        #print nums
        return recursive_p([], nums)
        


if __name__ == '__main__':

    d = [1, 2, 3]
    s = Solution()
    print s.permute(d)