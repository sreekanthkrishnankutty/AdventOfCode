Day 1 - Simply mathematics - used modulo arithmetic and interval arithmetic
Day 2 - BruteForce iteration to process every number in the given ranges, combined with string slicing and reconstruction to verify specific repetitive patterns
DAY 3 - Greedy algorithm with a constrained search window to iteratively select the largest available digit that still leaves enough remaining digits to complete the sequence.
DAY 4 - simulation on a grid - where it repeatedly removes items that dont have enough neighbors, stopping only when nothing changes anymore
DAY 5- verifies if specific numbers fall within given ranges and then sorts and merges overlapping ranges to calculate the total area they cover
DAY 6 - spatial parsing approach to vertically slice the text grid into isolated blocks, then extracts numbers using different reading orientations (horizontal vs vertical) to perform the calculations.
DAY 7 - row BY row approach to simultaneously track reachable positions and aggregate the total count of distinct paths.
DAY 8 - Kruskal's Algorithm using a Disjoint Set Union to iteratively merge the closest components until the graph is fully connected
DAY 9 - It iterates through every pair of vertices to calculate the maximum potential bounding box area, 
        and for Part 2 validates if the resulting rectangle fits entirely inside the polygon using the even-odd rule to check if the center is inside and edge intersection tests to ensure no boundaries are crossed.
DAY 10 - BruteForce bitwise XOR combinations to match a binary target state, 
        while Part 2 minimizes the sum of variables in a system of linear diophantine equations by performing integer gaussian elimination - iterating over free variables 
        and using back substitution to find valid non negative integer solutions
Day 11 - recursive Depth First search with memoization to efficiently count distinct paths between nodes, and calculates 
        Part 2 by multiplying the path counts of individual segments (svr -> dac -> fft -> out and svr -> fft -> dac -> out) and summing the results.
Day 12 - if a target grid can accommodate a set of shapes by verifying that the grid's total area divided by 9 (the fixed area of a 3x3 block) is greater than or equal to the total count of shapes requested
