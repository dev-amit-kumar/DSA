// Link: https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution
{
public:
    int target;
    vector<vector<int>> res;
    vector<int> temp;
    void dfs(vector<vector<int>> &graph, int currNode)
    {
        temp.push_back(currNode);
        if (currNode == target)
            res.push_back(temp);
        else
        {
            for (int next : graph[currNode])
            {
                dfs(graph, next);
            }
        }
        temp.pop_back();
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {
        target = graph.size() - 1;
        dfs(graph, 0);
        return res;
    }
};