colors = ['Red', 'Green', 'Blue']

regions = ['A', 'B', 'C', 'D']
coloring = {}

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}

for region in regions:
    for color in colors:
        safe = True

        for neighbor in neighbors[region]:
            if neighbor in coloring and coloring[neighbor] == color:
                safe = False
                break

        if safe:
            coloring[region] = color
            break

print("Map Coloring Solution:")
for region in regions:
    print(region, ":", coloring[region])
