#include <stdio.h>

void funcion1()
{
int i = 5, res = 10, j;
while (i > 0)
{
   j = 0;
   while ( j < 3)
   {
       res = res + j;
       j++;
   }
   i--;
}
printf("%i" ,res);
}

void funcion2()
{
int i = 9, res = 3, j = 0;
do
{
   j = 1;
   do
   {
      res = res + j;
      j++;
   }while(j <= 4);
   i--;
} while(i > 6);
printf("%i" ,res);
}

void funcion3()
{
int n, m, a = 0, b = 4 ;
for (m=1; m <= 4; m++)
{
   for (n=1; n <= b; n++)
   {
          printf("*");
   }
   for (n=1; n <= a ; n++)
   {
          printf("#");
   }
   b--;
   a++;
   printf("\n");
}
}

void funcion4()
{
int n, m;
for (m = 1; m <= 4; m++)
{
  for (n = 4; n > 0; n--)
  {
    if (n == 1 || n == 4 || m == 1 || m == 4)
    {
	 printf("*");
    }
    else
    {
	printf("#");
    }
  }
  printf("\n");
}
}

void funcion5()
{
int i, j;
for (i = 1; i <= 4; i++)
{
   for (j = 1; j <= i; j++)
   {
	printf("*");
   }
   printf("\n");
}
}

void funcion6()
{
int i, j;
for (i = 4; i >= 1; i--)
{
  for (j = 1; j <= i; j++)
  {
	printf("*");
  }
  printf("\n");
}
}

void main()
{
 funcion6();
}
