class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size();
        int top = 0;
        int COLS = matrix[0].size()-1;
        int bot = ROWS -1;

        while(top <= bot) {
            int row = (top + bot) / 2;
            if(target == matrix[row][0] || target == matrix[row][COLS]) {
                return true;
            }
            if(target < matrix[row][COLS] && target > matrix[row][0]) {
                break;
            } else if(target < matrix[0][0]|| target > matrix[ROWS-1][COLS]) {
                return false;
            }else if(target > matrix[row][COLS]){
                top = row + 1;
            } else {
                bot = row-1;
            }
        }
        int row = (top + bot) / 2;
        int l = 0;
        int r = COLS;
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
