#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {
    int n;
    scanf("%d", &n);

    int arr[1000];
    int dp[1000];

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        dp[i] = 1;
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    
    int max_length = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] > max_length) {
            max_length = dp[i];
        }
    }

    printf("%d\n", max_length);
    
    return 0;
}