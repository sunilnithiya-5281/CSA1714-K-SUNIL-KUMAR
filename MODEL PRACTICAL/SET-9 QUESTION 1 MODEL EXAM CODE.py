
import heapq

goal = (1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 0)

def manhattan(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            x1, y1 = divmod(i, 4)
            x2, y2 = divmod(tile - 1, 4)
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 4)

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 4 and 0 <= c < 4:
            new_pos = r * 4 + c
            temp = list(state)

            temp[zero], temp[new_pos] = (
                temp[new_pos], temp[zero]
            )

            neighbors.append(tuple(temp))

    return neighbors

def astar(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(next_state)

                heapq.heappush(
                    pq, (new_f, new_g, next_state,
                         path + [next_state])
                )

    return None

# Initial state (one move away from goal)
start = (1, 2, 3, 4,
         5, 6, 7, 8,
         9, 10, 11, 12,
         13, 14, 0, 15)

solution = astar(start)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        for i in range(0, 16, 4):
            print(step[i:i+4])
        print()
else:
    print("No solution found")
