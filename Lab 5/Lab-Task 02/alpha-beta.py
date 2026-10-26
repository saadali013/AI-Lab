import math

count = 0

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global count
    if depth == target:
        count += 1
        return scores[index]

    if maxTurn:
        value = float("-inf")
        for i in range(2):
            value = max(
                value,
                alphabeta(
                    depth + 1,
                    index * 2 + i,
                    False,
                    scores,
                    target,
                    alpha,
                    beta,
                ),
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(
                value,
                alphabeta(
                    depth + 1,
                    index * 2 + i,
                    True,
                    scores,
                    target,
                    alpha,
                    beta,
                ),
            )
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))

print("Value: ", alphabeta(0, 0, True, scores, depth, float("-inf"), float("inf")))
print("Count: ", count)