#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const int MAX_N = 100;

int n, m;
char labyrinth[MAX_N][MAX_N];

int max_path_length = -1;
vector<pair<int, int> > max_path;

void dfs(int i, int j, int path_length, vector<pair<int, int> > path)
{
    // check if we have reached the bottom of the labyrinth
    if (i == n - 1)
    {
        if (path_length > max_path_length)
        {
            max_path_length = path_length;
            max_path = path;
        }
        return;
    }

    // mark current hole as visited
    labyrinth[i][j] = path.size() + '0';
    path.push_back({i, j});

    // explore adjacent holes
    int di[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dj[] = {-1, 0, 1, -1, 1, -1, 0, 1};
    for (int k = 0; k < 8; k++)
    {
        int ni = i + di[k];
        int nj = j + dj[k];
        if (ni >= 0 && ni < n && nj >= 0 && nj < m && labyrinth[ni][nj] == '.')
        {
            dfs(ni, nj, path_length + 1, path);
        }
    }

    // unmark current hole
    labyrinth[i][j] = '.';
}

int main()
{
    // read labyrinth from file
    ifstream fin("labyrinth.txt");
    fin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            fin >> labyrinth[i][j];
        }
    }
    fin.close();

    // find max path
    for (int j = 0; j < m; j++)
    {
        if (labyrinth[0][j] == '.')
        {
            dfs(0, j, 1, {0, j});
        }
    }

    // print max path or -1 if no path was found
    if (max_path_length == -1)
    {
        cout << "-1\n";
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cout << labyrinth[i][j];
            }
            cout << "\n";
        }
    }
    else
    {
        for (auto p : max_path)
        {
            labyrinth[p.first][p.second] = p.second - max_path[0].second + '0';
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cout << labyrinth[i][j];
            }
            cout << "\n";
        }
    }

    return 0;
}