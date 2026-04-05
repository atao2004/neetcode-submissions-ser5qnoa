class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++) {
            for(int k = i + 1; k < nums.size(); k++) {
                if(nums[k] == nums[i]) {
                    return true;
                }
            }
        }
        return false;
    }
};
