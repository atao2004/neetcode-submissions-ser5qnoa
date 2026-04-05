class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxnum = nums[0];
        if(nums.size() == 1) return nums[0];
        int curr = 0;
        for(int i = 0;i < nums.size(); i++){
            curr += nums[i];
            maxnum = max(maxnum, curr);
            if(curr < 0) {
                curr = 0;
            }
        }
        return maxnum;
    }
};

