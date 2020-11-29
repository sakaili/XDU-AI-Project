/*
输入：一个整形数组成的数组a
输出：其中出现次数大于总数一半的数字
思路：先遍历一遍数组统计多少个不同的数字n，创建n个空间的数组b，再遍历一遍将每个数字在b的相应位置自增。最后将b中最大的数字输出
*/
#include<stdio.h>
#include<malloc.h>
int array_input;
int backup;
int *a;
int	b[100] = {0};
int main()
{
	int count = 0;
	int temp = 0;
	int stage = 0;
	scanf_s("%d", &array_input);
	backup = array_input;
	while (array_input>0)
	{
		temp = array_input % 10;
		array_input = array_input / 10;
		count++;
	}
	a = (int*)malloc(sizeof(int) * count);
	for (int j = 0; j < count; j++)
	{
		a[j] = backup % 10;
		backup = backup / 10;
	}
	for (int j = 0; j < count; j++)
	{
		b[a[j]] = b[a[j]]+1;
	}
	for (int j = 0; j < 100; j++)
	{
		if (b[j] > (count/2))
		{
			printf("%d", j);
			return 0;
		}
	}
	printf("no such a number");
	free(a);
	return 0;
}
