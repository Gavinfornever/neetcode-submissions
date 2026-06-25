
class Solution:
    # -4, -1, -1, 0, 1, 2
    # -1,-1,2
    # -1,0,1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        dic = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                dic[-nums[i]-nums[j]] = (i,j)
                # print(-nums[i]-nums[j], (i,j))
        
        # print(dic)
        # for key in dic:
        #     print()
        #     print(key,":", dic[key][0], nums[dic[key][0]], "|",  dic[key][1], nums[dic[key][1]])
        for i,x in enumerate(nums):
            if x in dic:
                val = dic[x]
                # print(i, val[0], val[1])
                # print(x, nums[val[0]], nums[val[1]])
                if i!=val[0] and i!=val[1]:
                    # print((x, nums[val[0]], nums[val[1]]))
                    tmp = [x, nums[val[0]], nums[val[1]]]
                    tmp = sorted(tmp)
                    res.add(tuple(tmp))

        return list(res)

