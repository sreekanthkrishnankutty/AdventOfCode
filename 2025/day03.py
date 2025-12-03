def get_max_joltage(line, k):
    digits = [int(c) for c in line if c.isdigit()]

    if len(digits) < k:
        return 0
    
    result = []
    start_index = 0
    items_needed = k

    while items_needed > 0:
        end_index = len(digits) - items_needed + 1
        window = digits[start_index : end_index]
        max_digit = max(window)
        offset = window.index(max_digit)
        actual_index = start_index + offset
        result.append(max_digit)

        start_index = actual_index + 1
        items_needed -= 1

    return int("".join(map(str, result)))

def solve():
    part1_total = 0
    part2_total = 0

    with open("AOC2025/input03.txt") as f:
        lines = f.readlines()

    for line in lines:
        line=line.strip()
        if not line:
            continue
        p1 = get_max_joltage(line, 2)
        part1_total += p1

        p2 = get_max_joltage(line, 12)
        part2_total += p2

    print("Part 1:", part1_total)
    print("Part 2:", part2_total)

if __name__ == "__main__":
    solve()