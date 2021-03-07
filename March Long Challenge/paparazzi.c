#include<stdio.h>
#include<stdlib.h>

int val(float arr[],int i,int j)
{   
    if(j-i==1){return 0;}
    int k;
    for(k=j-1;k<i;k--)
    {
        if(arr[k]>arr[i]+((arr[j]-arr[i])*(k-i)/(j-i)))
        {
            return 0;
        }
    }

    return j-i;
    
}

int main()
{
    int t,n,i,j,max;
    float* a;
    int pair1=0,pair2=1;
    scanf("%d",&t);

    while(t!=0)
    {
        scanf("%d",&n);
        a=(float*)malloc(sizeof(float)*n);
        for(i=0;i<n;i++)
        {
            scanf("%f",&a[i]);
        }

        max=1;
        
        for(i=0;i<n-1;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(val(a,i,j)>max)
                {
                    max=j-i;
                    pair1=i;
                    pair2=j;
                }
            }
        }

        printf("%d\n",max);
        free(a);
        t--;
    }
    return 0;
}