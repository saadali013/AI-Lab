import math
count = 0
score =[1,2,3,4,5,6,7,8]
treeDepth= math.log2(len(score))

def minmax(currDepth, nodeIndex, isMaxTurn, treeDepth):
    global count
    if currDepth == treeDepth:
        count += 1
        return score[nodeIndex]

    if isMaxTurn:
        return max(minmax(currDepth + 1, nodeIndex * 2, False, treeDepth),
                   minmax(currDepth + 1, nodeIndex * 2 + 1, False, treeDepth))
    else:
        return min(minmax(currDepth + 1, nodeIndex * 2, True, treeDepth),
                   minmax(currDepth + 1, nodeIndex * 2 + 1, True, treeDepth))
print("Value ", minmax(0, 0, True, treeDepth))
print("Count ", count)