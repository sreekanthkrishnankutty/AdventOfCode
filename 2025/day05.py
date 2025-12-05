def solve():
    with open("AOC2025/input05.txt") as f:
        lines = f.read().strip()

    two_sections = lines.split("\n\n")

    range_section = two_sections[0].splitlines()
    id_section = two_sections[1].splitlines()

    ranges = []
    for line in range_section:
        start_str, end_str = line.split("-")
        ranges.append((int(start_str), int(end_str)))

    part1_count = 0

    id_to_check = []
    for line in id_section:
        id_to_check.append(int(line.strip()))

    for ingredient_id in id_to_check:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        if is_fresh:
            part1_count += 1

    print("Part 1:", part1_count)

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = []

    current_start, current_end = sorted_ranges[0]
    for i in range(1, len(sorted_ranges)):
        next_start, next_end = sorted_ranges[i]
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end
        
    merged_ranges.append((current_start, current_end))

    part2_count = 0
    for start, end in merged_ranges:
        part2_count += (end - start + 1)
    
    print("Part 2:", part2_count)

if __name__ == "__main__":
    solve()