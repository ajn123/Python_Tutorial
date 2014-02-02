

//#include <stdio.h>
int fib(int );

int main(int argc, char const *argv[])
{
	printf("%d \n" , fib(23));
	return 0;
}



int fib(int n)
{
	if(n <= 1)
		return n;
	else
	{
		return fib(n-1) + fib(n-2);
	}
}