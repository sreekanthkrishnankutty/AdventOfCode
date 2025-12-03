def is_invalid_part1(s_num):
    length = len(s_num)

    if length % 2 != 0:
        return False
    
    mid=length // 2
    return s_num[:mid] == s_num[mid:]

def is_invalid_part2(s_num):
    length = len(s_num)

    for m in range(1, length // 2 + 1):
        if length % m == 0:
            pattern = s_num[:m]
            repetitions = length // m
            if pattern * repetitions == s_num:
                return True
    return False

def solve():
    with open("AOC2025/input02.txt") as f:
        content = f.read().strip()

    range_strings = content.split(",")

    sum_part1 = 0
    sum_part2 = 0

    for r_str in range_strings:
        r_str = r_str.strip()
        if not r_str:
            continue

        start_str, end_str = r_str.split("-")
        start_num = int(start_str)
        end_num = int(end_str)

        for num in range(start_num, end_num + 1):
            s_num = str(num)

            if is_invalid_part1(s_num):
                sum_part1 += num

            if is_invalid_part2(s_num):
                sum_part2 += num

    print("Part 1:", sum_part1)
    print("Part 2:", sum_part2)

if __name__ == "__main__":
    solve()