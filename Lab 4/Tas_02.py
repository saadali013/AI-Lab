graph = {
    "A": {"B": 2, "C": 4},
    "B": {"D": 2},
    "C": {"E": 3},
    "D": {"C": 2, "E": 4},
    "E": {"G": 7},
    "G": {}
}

heuristic = {
    "A": 20,
    "B": 4,
    "C": 3,
    "D": 5,
    "E": 10,
    "G": 0
}


def astar(start, goal):

    open_list = [(start, 0, [start])]
    visited = []
    cost = {start: 0}

    while open_list:

        open_list.sort(
            key=lambda x: x[1] + heuristic[x[0]]
        )

        node, g, path = open_list.pop(0)

        if g != cost[node]:
            continue

        visited.append(node)

        print("Checking:", node)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            print("Visited:", visited)
            return

        for neighbor, distance in graph[node].items():

            new_cost = g + distance

            if new_cost < cost.get(neighbor, float("inf")):

                cost[neighbor] = new_cost

                new_path = path + [neighbor]

                open_list.append(
                    (neighbor, new_cost, new_path)
                )


astar("A", "G")