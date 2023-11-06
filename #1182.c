#include <stdio.h>

int N, S, count = 0;
int arr[20];

void findSum(int index, int sum) {
    if (index == N) {
        if (sum == S) {
            count++;
        }
        return;
    }

    
    findSum(index + 1, sum + arr[index]);

    findSum(index + 1, sum);
}

int main() {
    scanf("%d %d", &N, &S);

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    findSum(0, 0);


    if (S == 0) {
        count--;
    }

    printf("%d\n", count);

    return 0;
}