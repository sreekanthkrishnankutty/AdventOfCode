import sys

def solve():
    with open('AOC2025/input06.txt', 'r') as f:
        lines = f.read().splitlines()

    groups = []
    current_group = []
    for line in lines:
        if not line.strip():
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(line)
    if current_group:
        groups.append(current_group)

    grand_total_p1 = 0
    grand_total_p2 = 0

    for group_lines in groups:
        if not group_lines:
            continue
            
        max_len = max(len(line) for line in group_lines)
        padded_lines = [line.ljust(max_len) for line in group_lines]

        is_separator = []
        for col_idx in range(max_len):
            col_chars = [line[col_idx] for line in padded_lines]
            if all(c == ' ' for c in col_chars):
                is_separator.append(True)
            else:
                is_separator.append(False)

        blocks = []
        current_block_cols = []
        for col_idx, is_sep in enumerate(is_separator):
            if not is_sep:
                current_block_cols.append(col_idx)
            else:
                if current_block_cols:
                    blocks.append(current_block_cols)
                    current_block_cols = []
        if current_block_cols:
            blocks.append(current_block_cols)

        for block_cols in blocks:
            start_col = block_cols[0]
            end_col = block_cols[-1] + 1
            
            block_grid = [line[start_col:end_col] for line in padded_lines]
            
            operator = None
            for row in block_grid:
                for char in row:
                    if char in ('+', '*'):
                        operator = char
                        break
                if operator: break
            
            p1_text = " ".join(block_grid)
            p1_tokens = p1_text.split()
            p1_operands = []
            
            for token in p1_tokens:
                if token.isdigit():
                    p1_operands.append(int(token))
            
            val_p1 = 0
            if operator == '+':
                val_p1 = sum(p1_operands)
            elif operator == '*':
                val_p1 = 1
                for x in p1_operands:
                    val_p1 *= x
            grand_total_p1 += val_p1

            p2_operands = []
            block_width = end_col - start_col
            
            for c in range(block_width - 1, -1, -1):
                col_digits = []
                for r in range(len(block_grid)):
                    char = block_grid[r][c]
                    if char.isdigit():
                        col_digits.append(char)
                
                if col_digits:
                    number_str = "".join(col_digits)
                    p2_operands.append(int(number_str))
            
            val_p2 = 0
            if operator == '+':
                val_p2 = sum(p2_operands)
            elif operator == '*':
                val_p2 = 1
                for x in p2_operands:
                    val_p2 *= x
            grand_total_p2 += val_p2

    print("Part 1:", grand_total_p1)
    print("Part 2:", grand_total_p2)

if __name__ == "__main__":
    solve()