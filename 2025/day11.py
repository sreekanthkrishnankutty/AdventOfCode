import sys

def count_paths(start_node, end_node, graph):
    memo = {}

    def search(current):
        if current == end_node:
            return 1

        if current in memo:
            return memo[current]

        if current not in graph:
            return 0

        total = 0
        for neighbor in graph[current]:
            total += search(neighbor)
            
        memo[current] = total
        return total

    return search(start_node)

def solve():
    graph = {}
    with open('AOC2025/input11.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.split(':')
            node = parts[0].strip()
            if len(parts) > 1 and parts[1].strip():
                graph[node] = parts[1].strip().split()
            else:
                graph[node] = []

    p1_ans = count_paths('you', 'out', graph)
    print("Part 1:", p1_ans)

    leg1_a = count_paths('svr', 'dac', graph)
    leg2_a = count_paths('dac', 'fft', graph)
    leg3_a = count_paths('fft', 'out', graph)
    
    path_dac_then_fft = leg1_a * leg2_a * leg3_a

    leg1_b = count_paths('svr', 'fft', graph)
    leg2_b = count_paths('fft', 'dac', graph)
    leg3_b = count_paths('dac', 'out', graph)

    path_fft_then_dac = leg1_b * leg2_b * leg3_b

    p2_ans = path_dac_then_fft + path_fft_then_dac
    
    print("Part 2:",p2_ans)

if __name__ == "__main__":
    solve()