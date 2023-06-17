class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int ans = 0;
        int row = grid.size();
        int col = grid[0].size();
        for (int i = 0; i < row ; i++){
            for (int j = 0; j < col; j++){
                if(grid[i][j] == 1){
                    ans += 4;
                    if(j+1 != col && grid[i][j+1] == 1){ //right
                        ans -= 1;
                    }
                    if(j != 0 && grid[i][j-1] == 1){ //left
                        ans -= 1;
                    }
                    if(i+1 != row && grid[i+1][j] == 1){ //down
                        ans -= 1;
                    }
                    if(i != 0 && grid[i-1][j] == 1){ //up
                        ans -= 1;
                    }
                }
            }
        }
        return ans;
    }
};