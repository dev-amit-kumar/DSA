// Link: https://leetcode.com/problems/course-schedule-ii/

#include <iostream>
#include <vector>

vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
{
}

int main()
{
    int numCourses = 2;
    vector<vector<int>> prerequisites = {{1, 0}};
    vector<int> result = findOrder(numCourses, prerequisites);
    for (int i = 0; i < prerequisites.length(); i++)
        cout << prerequisites[i] << ", ";
    cout << endl;
}