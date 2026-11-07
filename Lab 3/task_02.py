
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

GOAL = 'H'


def dls(node, goal, limit, path):

    if node == goal:
        return "FOUND", path

    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None

    cutoff = False

    for child in graph[node]:

        if child not in path:

            status, result = dls(
                child, goal, limit - 1, path + [child]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff = True

    if cutoff:
        return "CUTOFF", None

    return "FAILURE", None


def iddfs(start, goal, max_depth):

    for limit in range(1, max_depth + 1):

        status, path = dls(start, goal, limit, [start])

        if status == "FOUND":
            return status, path, limit

    return status, None, max_depth



print("DLS RESULTS")

for limit in [1, 2, 3, 4]:

    status, path = dls('A', GOAL, limit, ['A'])

    print("Limit:", limit)
    print("Status:", status)
    print("Path:", path)
    print()



print("IDDFS RESULTS")

for depth in [1, 2, 3, 4]:

    status, path, used_limit = iddfs('A', GOAL, depth)

    print("Maximum Depth:", depth)
    print("Status:", status)
    print("Path:", path)
    print("Limits Attempted:", list(range(1, used_limit + 1)))
    print()