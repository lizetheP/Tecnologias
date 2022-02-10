#include <stdio.h>
#include <stdlib.h>

#define renglones 5
#define columnas 5

void iniciaMatriz (int M[renglones][columnas])
{
	   for (int i=0; i<renglones; i++)
       {
		   for (int j=0; j<columnas; j++)
              {
                    M[ i ][ j ] = 5;
              }
        }
}

void imprimeMatriz (int M[renglones][columnas])
{
	   for (int i=0; i<renglones; i++)
       {
		   for (int j=0; j<columnas; j++)
              {
                    printf("%3i", M[i][j]);
              }
           printf("\n");
        }
}

void iniciaMatriz2 (int M[renglones][columnas])
{
	   int cont = 1;
	   for (int i=0; i<renglones; i++)
       {
		   for (int j=0; j<columnas; j++)
              {
                    M[i][j] = cont;
                    cont++;
              }
        }
}

void sumaMatrices (int A[renglones][columnas], int B[renglones][columnas], int C[renglones][columnas])
{
	   for (int i=0; i<renglones; i++)
       {
		   for (int j=0; j<columnas; j++)
              {
                  C[i][j] = A[i][j] + B[i][j];
              }
        }
}

void main()
{
    int m1[renglones][columnas], m2[renglones][columnas], m3[renglones][columnas];;

    printf("\n MATRIZ 1\n");
    iniciaMatriz(m1);
    imprimeMatriz(m1);

    printf("\n MATRIZ 2 \n");
    iniciaMatriz2(m2);
    imprimeMatriz(m2);

    printf("\n SUMA MATRICES \n");
    sumaMatrices(m1, m2, m3);
    imprimeMatriz(m3);

    printf("\n\n");
    system("PAUSE");

}


