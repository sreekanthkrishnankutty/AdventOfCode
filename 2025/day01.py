def solve():
    with open("AOC2025/input01.txt", 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    DIAL_SIZE = 100
    current_position = 50

    part1_count = 0
    part2_count = 0

    for instruction in lines:
        direction = instruction[0]
        amount = int(instruction[1:])

        full_circles = amount // DIAL_SIZE
        part2_count += full_circles

        remainder = amount % DIAL_SIZE

        if direction == 'R':
            if remainder > 0 and (current_position + remainder) >= DIAL_SIZE:
                part2_count += 1
            current_position = (current_position + amount) % DIAL_SIZE

        elif direction == 'L':
            if remainder > 0 and current_position > 0 and (current_position - remainder) <= 0:
                part2_count += 1
            current_position = (current_position - amount) % DIAL_SIZE

        if current_position == 0:
            part1_count += 1

    print("Part 1: ", part1_count)
    print("Part 2: ", part2_count)

if __name__ == "__main__":
    solve()