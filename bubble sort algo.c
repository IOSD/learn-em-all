#include <stdio.h>
#include <stdlib.h>
int k,n,i,j=1,l;
int main() {
	printf("enter the no. of element you wnt to take in array\n");
	scanf("%d",&n);
	printf("enter the values of element in the array");
	int a[n];
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(k=1;k<n;k++)
	{
		for(j=0;j<=n-k;j++)
		{
			if(a[j]>a[j+1])
			{
				int x;
				x=a[j+1];
				a[j+1]=a[j];
				a[j]=x;
			}
		}
	}
	for(l=0;l<n;l++)
	{
		printf("%d  ",a[l]);
	}
	return 0;
