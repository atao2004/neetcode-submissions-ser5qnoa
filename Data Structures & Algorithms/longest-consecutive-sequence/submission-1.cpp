class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> unique_set;
        for(auto i : nums) {
            unique_set.insert(i);
        }

        int result = 0;
        for(auto num : unique_set) {
            int curr = num;
            int curr_longest = 1;

            if(unique_set.find(curr - 1) == unique_set.end()) {
               while(unique_set.find(curr + 1) != unique_set.end()) {
                curr++;
                curr_longest++;
               }
            }
            result = max(result, curr_longest);
        }
        return result;


    }
};
