class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int per = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {
                if(grid[i][j] == 1) {
                     per += 4;
                     if( i != grid.size()-1 and grid[i+1][j] == 1 ) per--;
                     if(j != grid[i].size()-1 and  grid[i][j+1] == 1) per--;
                     if( i != 0 and grid[i-1][j] == 1) per--;
                     if(j != 0 and grid[i][j-1] == 1) per--;
                }
            }
        }
        return per;
    }
};