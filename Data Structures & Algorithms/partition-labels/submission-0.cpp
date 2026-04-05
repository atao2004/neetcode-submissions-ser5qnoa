class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> last_pos;

        for(int i = 0; i < s.size(); i++) {
            last_pos[s[i]] = i;
        }
        vector<int> res;
        int size, maxsub = 0;
        for(int i = 0; i < s.size(); i++) {
            size++;
            maxsub = max(maxsub, last_pos[s[i]]);

            if(i == maxsub) {
                res.push_back(size);
                size = 0;
            } 
            
        }
        return res;

    }
};
