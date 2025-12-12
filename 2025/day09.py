import sys

def solve():
    coordinates = []
    with open('AOC2025/input09.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            parts = line.split(',')
            coordinates.append((int(parts[0]), int(parts[1])))

    n = len(coordinates)
    if n < 2:
        print("Not enough coordinates.")
        return

    # Part 1
    max_area_p1 = 0
    for i in range(n):
        for j in range(i + 1, n):
            p1 = coordinates[i]
            p2 = coordinates[j]
            # Area is inclusive: (diff + 1)
            w = abs(p1[0] - p2[0]) + 1
            h = abs(p1[1] - p2[1]) + 1
            area = w * h
            if area > max_area_p1:
                max_area_p1 = area
    
    print("Part 1:", max_area_p1)

    # Part 2
    vert_edges = [] 
    horz_edges = []
    
    for i in range(n):
        p1 = coordinates[i]
        p2 = coordinates[(i + 1) % n] 
        
        if p1[0] == p2[0]:
            vert_edges.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
        else:
            horz_edges.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))

    def is_inside(x, y):
        intersections = 0
        for vx, vy1, vy2 in vert_edges:
            if vx > x and vy1 <= y < vy2:
                intersections += 1
        return (intersections % 2) == 1

    def intersects_boundary(x1, x2, y1, y2):
        for vx, vy1, vy2 in vert_edges:
            if x1 < vx < x2:
                if max(y1, vy1) < min(y2, vy2):
                    return True

        for hy, hx1, hx2 in horz_edges:
            if y1 < hy < y2:
                if max(x1, hx1) < min(x2, hx2):
                    return True
        return False

    max_area_p2 = 0
    
    for i in range(n):
        if i % 10 == 0:
            print(f"Processing tile {i}/{n}...", end='\r')
            
        for j in range(i + 1, n):
            p1 = coordinates[i]
            p2 = coordinates[j]
            
            x1, x2 = min(p1[0], p2[0]), max(p1[0], p2[0])
            y1, y2 = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            w = (x2 - x1) + 1
            h = (y2 - y1) + 1
            area = w * h
            
            if area <= max_area_p2:
                continue
            
            mid_x = (x1 + x2) / 2.0
            mid_y = (y1 + y2) / 2.0
            
            if is_inside(mid_x, mid_y):
                if not intersects_boundary(x1, x2, y1, y2):
                    max_area_p2 = area

    print("Part 2:", max_area_p2)

if __name__ == "__main__":
    solve()