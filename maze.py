import numpy as np


maze = np.array([[1, 0, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]])


def maze_run():
    rows, cols = maze.shape
    ans = np.zeros(maze.shape, dtype=np.uint8)

    queue = [[0, 0]]
    ans[0, 0] = 1

    # 우, 하, 좌, 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= cols or ny >= rows:
                continue

            if maze[ny, nx] == 1 and ans[ny, nx] == 0:
                queue.append([ny, nx])
                ans[ny, nx] = ans[y, x] + 1

        print(ans, "\n")




if __name__ == "__main__":
    move = maze_run()
    print(f"최소 이동 횟수는 {move}입니다.")
