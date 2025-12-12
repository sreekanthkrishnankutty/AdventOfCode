#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>

using namespace std;

int main() {
    ifstream inputFile("input07.txt");

    vector<string> grid;
    string line;
    while (getline(inputFile, line)) {
        if (!line.empty()) {
            grid.push_back(line);
        }
    }
    inputFile.close();

    int rows = grid.size();
    int cols = grid[0].size();
    
    int start_row = -1;
    int start_col = -1;
    
    for (int r = 0; r < rows; ++r) {
        size_t pos = grid[r].find('S');
        if (pos != string::npos) {
            start_row = r;
            start_col = (int)pos;
            break;
        }
    }
    
    // Part 1 
    set<int> p1_beams;
    p1_beams.insert(start_col);
    long long p1_split_count = 0;

    // Part 2 
    map<int, long long> p2_timelines;
    p2_timelines[start_col] = 1; 
    long long p2_total_finished_timelines = 0;

    for (int r = start_row + 1; r < rows; ++r) {
        
        // Part 1 Logic
        set<int> p1_next_beams;
        for (int c : p1_beams) { 
            if (c < 0 || c >= cols) continue;

            char cell = grid[r][c];
            if (cell == '^') {
                p1_split_count++;
                p1_next_beams.insert(c - 1);
                p1_next_beams.insert(c + 1);
            } else {
                p1_next_beams.insert(c);
            }
        }
        p1_beams = p1_next_beams;

        // Part 2 Logic
        map<int, long long> p2_next_timelines;

        for (auto const& entry : p2_timelines) {
            int c = entry.first;           
            long long count = entry.second;
            
            char cell = grid[r][c];

            if (cell == '^') {

                if (c - 1 >= 0 && c - 1 < cols) {
                    p2_next_timelines[c - 1] += count;
                } else {
                    p2_total_finished_timelines += count;
                }

                if (c + 1 >= 0 && c + 1 < cols) {
                    p2_next_timelines[c + 1] += count;
                } else {
                    p2_total_finished_timelines += count;
                }
            } else {
                if (c >= 0 && c < cols) {
                    p2_next_timelines[c] += count;
                } 
            }
        }
        p2_timelines = p2_next_timelines;
        
        if (p1_beams.empty() && p2_timelines.empty()) break;
    }

    for (auto const& entry : p2_timelines) {
        p2_total_finished_timelines += entry.second;
    }

    cout << "Part 1:" << p1_split_count << endl;
    cout << "Part 2:" << p2_total_finished_timelines << endl;

    return 0;
}