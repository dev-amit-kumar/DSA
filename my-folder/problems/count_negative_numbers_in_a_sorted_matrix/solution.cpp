class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int len = grid[0].size();
        int row_len = grid.size();
        for (int i = 0; i < row_len; i++)
        {
            vector<int> col = grid[i];
            int left = 0;
            int right = len - 1;
            while (left <= right)
            {
                int mid = (right + left) / 2;
                if (col[mid] < 0)
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            count += (len - left);
        }
        return count;
    }
};