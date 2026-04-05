class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> chars;
        int l = 0;
        int result= 0;

        for(int i = 0; i < s.size(); i++) {
            while(chars.find(s[i]) != chars.end()) {
                chars.erase(s[l]);
                l++; // move up
            }
            chars.insert(s[i]);
            result = max(result, (int)chars.size());
        }
        return result;
    }
};
