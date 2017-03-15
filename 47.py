import  copy

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursive_p(prefix, nnums):
            res = []
            ks = nnums.keys()
            if len(ks) == 1:
                last_one, count = nnums.popitem()
                tail = [last_one for i in range(0, count)]
                res.append(prefix + tail)
            else:
                for i in range(0, len(ks)):
                    nnums_copy = copy.copy(nnums)
                    nnums_copy[ks[i]] = nnums_copy[ks[i]] - 1
                    if nnums_copy[ks[i]] == 0:
                        del nnums_copy[ks[i]]
                    res += recursive_p(prefix + [ks[i]],  nnums_copy)
            return res

        sd = dict()
        for i in nums:
            if sd.has_key(i):
                sd[i] += 1
            else:
                sd[i] = 1
        return recursive_p([], sd)
        


if __name__ == '__main__':

    d = [3,3,0,0,2,3,2]
    s = Solution()
    print s.permuteUnique(d)