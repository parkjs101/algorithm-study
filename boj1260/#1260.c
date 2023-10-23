#include <stdio.h>
#include <stdlib.h>


int N, M, V; 
int graph[1001][1001]; 
int visited[1001]; 


void dfs(int v) {
    printf("%d ", v); 
    visited[v] = 1;

    for (int i = 1; i <= N; i++) {
        if (graph[v][i] && !visited[i]) {
            dfs(i); 
        }
    }
}


void bfs(int v) {
    int queue[1001];
    int front = 0, rear = 0;

    printf("%d ", v);
    visited[v] = 1;
    queue[rear++] = v;

    while (front < rear) {
        int u = queue[front++];

        for (int i = 1; i <= N; i++) {
            if (graph[u][i] && !visited[i]) {
                printf("%d ", i);
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    scanf("%d %d %d", &N, &M, &V);

    for (int i = 0; i < M; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u][v] = graph[v][u] = 1; 
    }

    dfs(V); 
    printf("\n");

    
    for (int i = 1; i <= N; i++) {
        visited[i] = 0;
    }

    bfs(V); 
    printf("\n");

    return 0;
}