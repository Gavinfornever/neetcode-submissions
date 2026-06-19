class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroFlag = False
        firstZero = -1
        res = []
        product = 1
        for i, x in enumerate(nums):
            if x==0:
                if zeroFlag ==False:
                    zeroFlag = True
                    firstZero = i
                else:
                    res = [0]*len(nums)
                    return res
                continue
            
            product *= x
        
        if zeroFlag == True:
            res = [0]*len(nums)
            res[firstZero] = product
            return res

        for i, x in enumerate(nums):
            res.append(int(product/x))

        return res
                
        



