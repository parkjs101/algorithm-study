#include <stdio.h>

int field[50][50];
int visited[50][50];
int M, N;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void dfs(int x, int y) {
    visited[x][y] = 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
            if (field[nx][ny] == 1 && !visited[nx][ny]) {
                dfs(nx, ny);
            }
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int K;
        scanf("%d %d %d", &M, &N, &K);

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                field[i][j] = 0;
                visited[i][j] = 0;
            }
        }

        for (int i = 0; i < K; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            field[x][y] = 1;
        }

        int count = 0;

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (field[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j);
                    count++;
                }
            }
        }

        printf("%d\n", count);
    }

    return 0;
}
