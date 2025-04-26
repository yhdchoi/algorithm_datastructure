# The maze: 0==wall, 1==way
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = y + dx[i]
            ny = y + dy[i]

            # Outside the limit
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # The wall
            if graph[nx][ny] == 0:
                continue
            # Node visited for the first time
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((x, y))
    # The shortest way direction
    return graph[n - 1][m - 1]


# size input
n, m = map(int, input().split())
# wall&way input
graph = []
for j in range(n):
    graph.append(list(map(int, input())))

# up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
