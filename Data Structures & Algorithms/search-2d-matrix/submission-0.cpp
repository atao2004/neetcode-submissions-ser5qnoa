class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row_max = matrix.size() - 1;
        int top = 0;
        int n = matrix[0].size()-1;
        int bot = row_max;

        while(top <= bot) {
            int row = (top + bot) / 2;
            if(target == matrix[row][0] || target == matrix[row][n]) {
                return true;
            }
            if(target < matrix[row][n] && target > matrix[row][0]) {
                break;
            } else if(target < matrix[0][0]|| target > matrix[row_max][n]) {
                return false;
            }else if(target > matrix[row][n]){
                top = row + 1;
            } else {
                bot = row-1;
            }
        }
        int row = (top + bot) / 2;
        int l = 0;
        int r = n;
        while(l <= r) {
            int m = l + (r-l)/2;
            if(target == matrix[row][m]) {
                return true;
            } else if(target> matrix[row][m]) {
                l = m+1;
            } else{
                r = m-1;
            }
        }

        return false;
    }
};
