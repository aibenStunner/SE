# applied Depth-first search using recursive approach

def solution(mat):
    streams = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                stream = dfs(mat, i, j)
                streams.append(stream)
    return streams
    
def dfs(mat, i, j):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
        return 0
    if mat[i][j] == 0:
        return 0
    mat[i][j] = 0
    stream = 1

    # check immediate surrounding
    for r in range(i-1, i+2):
        for c in range(j-1, j+2):
            if r != i or c != j:
                stream += dfs(mat, r, c)

    # wrap around diagonally (check immediate right diagonal from other side)
    if j == 0:      # check if element is on left edge
        stream += dfs(mat, i-1, len(mat[0])-1)
        stream += dfs(mat, i+1, len(mat[0])-1)

    # wrap around diagonally (check immediate left diagonal from other side)
    if j == len(mat[0])-1:  # check if element is on right edge
        stream += dfs(mat, 1-1, 0)
        stream += dfs(mat, 1+1, 0)

    # wrap around diagonally (check first element in leading diagonal)
    if i == len(mat)-1 and j == len(mat[0])-1: # check if element is the last element in leading diagonal
        stream += dfs(mat, 0, 0)

    # wrap around diagonally (check last element in leading diagonal)
    if i == 0 and j == 0:    # check if element is the first element in leading diagonal
        stream += dfs(mat, len(mat)-1, len(mat[0])-1)

    # wrap around horizontally
    if j == len(mat[0])-1:   # check if element is at the right edge
        stream += dfs(mat, i, 0)
    if j == 0:               # check if element is at the left edge
        stream += dfs(mat, i, len(mat[0])-1)

    # wrap around vertically
    if i == len(mat)-1:      # check if element is at the lower edge
        stream += dfs(mat, 0, j)
    if i == 0:               # check if element is at the upper edge
        stream += dfs(mat, len(mat)-1, j)  

    return stream

mat = [
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 0, 0, 1]
]

print(solution(mat))