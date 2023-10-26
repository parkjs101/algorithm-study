#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int arr[500][500];
int temp;

void arr_print(int n)
{
    for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                printf("%d ",arr[i][j]);
            }
            printf("\n");
        }
    return;
}
void arr_turn(int n, int d)
{
    if(d<0)
    {
        d=360+d;
    }
    int count=d/45;
    
    for(int k=0;k<count;k++)
    {
        
        for (int i=0;i<n/2;i++) 
        {
            temp=arr[i][i];
            arr[i][i]=arr[n/2][i];
            arr[n/2][i]=arr[n-1-i][i];
            arr[n-1-i][i]=arr[n-1-i][n/2];
            arr[n-1-i][n/2]=arr[n-1-i][n-1-i];
            arr[n-1-i][n-1-i]=arr[n/2][n-1-i];
            arr[n/2][n-1-i]=arr[i][n-1-i];
            arr[i][n-1-i]=arr[i][n/2];
            arr[i][n/2]=temp;

        }

        
    }
    return;
}

int main(void)
{
    
    int t, n, d;
    int b;
    scanf("%d",&t);
    for(int a=0;a<t;a++)
    {
        scanf("%d %d",&n,&d);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                scanf("%d",&b);
                arr[i][j]=b;
            }
        }
        
        arr_turn(n,d);
        arr_print(n);
    }
    
    



    return 0;
}