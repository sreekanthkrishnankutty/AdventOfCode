import sys
import re
from itertools import combinations, product

def solve():
    with open("AOC2025/input10.txt", "r") as f:
        content = f.read()

    total_presses_lights = 0
    total_presses_joltages = 0

    lines = content.splitlines()

    for line in lines:
        if not line.strip():
            continue

        parts = line.split(" ")
        
        lights_part = parts.pop(0)
        lights_str = lights_part[1:-1]

        required_state = int(lights_str.replace('.', '0').replace('#', '1'), 2)
        L = len(lights_str)

        buttons = []
        required_joltages = []

        for part in parts:
            numbers = [int(x) for x in re.findall(r'\d+', part)]
            
            if part.startswith('('):
                buttons.append(numbers)
            else:
                required_joltages = numbers
                break

        button_count = len(buttons)
        
        button_masks = []
        for btn in buttons:
            mask = 0
            for idx in btn:
                mask |= (1 << (L - 1 - idx))
            button_masks.append(mask)

        found_part1 = False
        for presses in range(1, button_count + 1):
            for combo in combinations(button_masks, presses):
                state = 0
                for m in combo:
                    state ^= m
                
                if state == required_state:
                    total_presses_lights += presses
                    found_part1 = True
                    break
            
            if found_part1:
                break

        num_vars = len(buttons) 
        num_eqs = len(required_joltages) 

        matrix = []
        for r in range(num_eqs):
            row = []
            for c in range(num_vars):
                if r in buttons[c]:
                    row.append(1)
                else:
                    row.append(0)
            row.append(required_joltages[r])
            matrix.append(row)

        pivot_columns = []
        free_columns = []
        curr_row = 0

        for col in range(num_vars):
            pivot_row = -1
            
            for r in range(curr_row, num_eqs):
                if matrix[r][col] != 0:
                    pivot_row = r
                    break
            
            if pivot_row == -1:
                free_columns.append(col)
                continue

            matrix[curr_row], matrix[pivot_row] = matrix[pivot_row], matrix[curr_row]

            pivot_val = matrix[curr_row][col]
            for r in range(curr_row + 1, num_eqs):
                val = matrix[r][col]
                if val != 0:
                    for c in range(num_vars + 1): 
                        matrix[r][c] = matrix[r][c] * pivot_val - matrix[curr_row][c] * val
            
            pivot_columns.append(col)
            curr_row += 1

        ranges = []
        for col in free_columns:

            limit = float('inf')
            for counter_idx in buttons[col]:
                if counter_idx < len(required_joltages):
                    req = required_joltages[counter_idx]
                    if req < limit:
                        limit = req

            if limit == float('inf'):
                ranges.append(range(1))
            else:
                ranges.append(range(limit + 1))

        min_presses = -1

        for free_vals in product(*ranges):
            solution = [0] * num_vars

            for i, col in enumerate(free_columns):
                solution[col] = free_vals[i]
            
            valid = True

            for i in range(len(pivot_columns) - 1, -1, -1):
                col = pivot_columns[i]
                row_idx = i 

                rhs = matrix[row_idx][num_vars]

                for j in range(col + 1, num_vars):
                    rhs -= matrix[row_idx][j] * solution[j]
                
                pivot_coef = matrix[row_idx][col]
 
                if pivot_coef == 0 or rhs % pivot_coef != 0:
                    valid = False
                    break
                
                val = rhs // pivot_coef
                
                if val < 0:
                    valid = False
                    break
                
                solution[col] = val

            if valid:
                current_total = sum(solution)
                if min_presses == -1 or current_total < min_presses:
                    min_presses = current_total

        if min_presses != -1:
            total_presses_joltages += min_presses

    print("Part 1:", total_presses_lights)
    print("Part 2:", total_presses_joltages)

if __name__ == "__main__":
    solve()