#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>

struct Point {
    long long x, y, z;
};

struct Connection {
    int u; 
    int v; 
    long long distSq; 
};

class DSU {
    std::vector<int> parent;
    std::vector<int> size;
    int numComponents; 

public:
    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        numComponents = n; 
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
    }

    int find(int i) {
        if (parent[i] != i)
            parent[i] = find(parent[i]); 
        return parent[i];
    }

    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);

        if (root_i != root_j) {
            if (size[root_i] < size[root_j])
                std::swap(root_i, root_j);
            parent[root_j] = root_i;
            size[root_i] += size[root_j];
            numComponents--; 
            return true;
        }
        return false;
    }

    int getSize(int i) {
        return size[find(i)];
    }

    int getNumComponents() {
        return numComponents;
    }
};

int main() {
    std::ifstream inputFile("input08.txt");

    std::vector<Point> boxes;
    std::string line;

    while (std::getline(inputFile, line)) {
        if (line.empty()) continue;
        long long x, y, z;
        char comma;
        std::stringstream ss(line);
        if (ss >> x >> comma >> y >> comma >> z) {
            boxes.push_back({x, y, z});
        }
    }
    inputFile.close();

    int n = boxes.size();
    if (n == 0) return 0;

    std::vector<Connection> allConnections;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            long long dx = boxes[i].x - boxes[j].x;
            long long dy = boxes[i].y - boxes[j].y;
            long long dz = boxes[i].z - boxes[j].z;
            long long dSq = dx*dx + dy*dy + dz*dz;
            allConnections.push_back({i, j, dSq});
        }
    }

    std::sort(allConnections.begin(), allConnections.end(), 
              [](const Connection& a, const Connection& b) {
                  return a.distSq < b.distSq;
              });

    // PART 1
    DSU dsu1(n);
    int limit = std::min((int)allConnections.size(), 1000);

    for (int i = 0; i < limit; ++i) {
        dsu1.unite(allConnections[i].u, allConnections[i].v);
    }

    std::map<int, int> uniqueCircuits;
    for (int i = 0; i < n; ++i) {
        int root = dsu1.find(i);
        uniqueCircuits[root] = dsu1.getSize(root);
    }

    std::vector<long long> sizes;
    for (std::map<int, int>::iterator it = uniqueCircuits.begin(); it != uniqueCircuits.end(); ++it) {
        sizes.push_back(it->second);
    }
    std::sort(sizes.rbegin(), sizes.rend());

    long long part1Result = 1;
    for (size_t i = 0; i < sizes.size() && i < 3; ++i) {
        part1Result *= sizes[i];
    }
    
    std::cout << "Part 1:" << part1Result << std::endl;

    // PART 2
    DSU dsu2(n); 
    long long part2Result = 0;

    for (size_t i = 0; i < allConnections.size(); ++i) {
        int u = allConnections[i].u;
        int v = allConnections[i].v;

        bool merged = dsu2.unite(u, v);

        if (merged && dsu2.getNumComponents() == 1) {
            std::cout << "Fully connected at connection between: " 
                      << boxes[u].x << "," << boxes[u].y << "," << boxes[u].z << " and "
                      << boxes[v].x << "," << boxes[v].y << "," << boxes[v].z << std::endl;
            
            part2Result = boxes[u].x * boxes[v].x;
            break;
        }
    }

    std::cout << "Part 2:" << part2Result << std::endl;

    return 0;
}