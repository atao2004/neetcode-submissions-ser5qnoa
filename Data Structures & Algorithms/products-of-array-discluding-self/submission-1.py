class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr_L = [1] * len(nums)
        product_arr_R = [1] * len(nums)
        # left prod arr
        prod = 1
        for i in range(1, len(nums)):
            prod = prod*nums[i-1]
            product_arr_L[i] = prod
        prod=1
        # right prod arr
        for i in range(len(nums)-2, -1, -1):
            prod = prod*nums[i+1]
            product_arr_R[i] = prod
        output=[1]* len(nums)
        for i in range(len(nums)):
            output[i] = product_arr_L[i] * product_arr_R[i]
        return output


        