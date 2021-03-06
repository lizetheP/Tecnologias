#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/*Algoritmo: Escribir frases en archivo
1. Declarar arch, cadena[50], i
2. Abrir arch en modo de escritura
3. Si arch existe
        for (i=1; i <= 5; i++)
              Escribir("Dame una frase")
              Leer (frase)
              Escribir frase en arch
        cerrar (arch)
4. sino
        Escribir("ERROR")*/

void escribirEnArchivo()
{ FILE *arch;
   char  cadena[50];
   int i;
   arch = fopen("frases.txt", "w");
   if (arch != NULL)
   {
       for (i=1; i <= 5; i++)
       {
              printf("\n Dame una frase: ");
              fflush(stdin);
              gets(cadena);
              fputs(cadena, arch);
              fputc('\n', arch);
       }
       fclose(arch);
   }
   else
        printf("\n ERROR EL ARCHIVO NO SE PUDO CREAR");
}

/*Algoritmo: Contar consonantes de un archivo
1. Declarar arch, cont=0, letra
2. Abrir arch en modo de lectura
3. Si arch existe
       leer letra de arch
       while (letra sea distinto de fin de archivo)
            si (letra es consonante)
                 cont++
             leer letra de arch
      cerrar(arch)
4. Sino
         Escribir("ERROR")
5. return cont*/

int cuentaConsonantes()
{  FILE *arch;
   int cont=0;
   char letra;
   arch = fopen("frases.txt", "r");
   if (arch != NULL)
   {
       letra = fgetc(arch);
       while (letra != EOF)
       {
            letra = toupper(letra);
            if (letra >= 66 && letra <= 90 && letra != 'E' && letra != 'I' && letra != 'O' && letra != 'U')
      //      if (letra >= 'B' && letra <= 'Z' && letra != 'E' && letra != 'I' && letra != 'O' && letra != 'U') ESTA ES OTRA SOLUCI?N CORRECTA
                 cont++;
            letra = fgetc(arch);
       }
       fclose(arch);
   }
   else
      printf("\n ERROR EL ARCHIVO NO SE PUDO LEER");
   return cont;
}

/*Algoritmo: Escribir datos del alumno en archivo
1. Declarar arch, nombre[15], carrera[5], calif
2. Abrir arch en modo de escritura
3. si (arch existe)
         Escribir("Dame tu nombre")
         leer(nombre)
         Escribir("Dame tu carrera")
         leer(carrera)
         Escribir("Dame tu calificacion")
         leer(calif)
         Escribir nombre, carrera y calif en arch
         cerrar(arch)
4. sino
      escribir("ERROR")*/

void escribirConFormato()
{
  FILE *arch;
  char nombre[15], carrera[5];
  float calif;
   arch = fopen("calis.txt", "w");
   if (arch != NULL)
   {
         printf("\n Dame tu nombre: ");
         fflush(stdin);
         gets(nombre);
         printf("\n Dame tu carrera: ");
         fflush(stdin);
         gets(carrera);
         printf("\n Dame tu calificacion: ");
         scanf("%f", &calif);

         fprintf(arch, "%s %s %.2f", nombre, carrera, calif);

         fclose(arch);
   }
   else
      printf("\n ERROR EL ARCHIVO NO SE PUDO CREAR");
}

/*Algoritmo: Leer datos del alumno
1. Declarar arch, nombre[15], carrera[5], calif
2. Abrir arch en modo de lectura
3. si (arch existe)
         Leer (nombre, carrera y calif) del arch
         Escribir(nombre, carrera y calif)
         cerrar(arch)
4. sino
      escribir("ERROR")*/

void leerConFormato()
{
  FILE *arch;
  char nombre[15], carrera[5];
  float calif;
   arch = fopen("calis.txt", "r");
   if (arch != NULL)
   {
         fscanf(arch, "%s %s %f", &nombre, &carrera, &calif);
         printf("\n %s %s %.2f", nombre, carrera, calif);
         fclose(arch);
   }
   else
      printf("\n ERROR EL ARCHIVO NO SE PUDO CREAR");
}

int main ()
{
  char ruta[50], opcion;
  int res;
  do
  {
    printf("\n\n MENU\n");
    printf("\n A. Escribir en archivo\n");
    printf("\n B. Cuenta Consonantes\n");
    printf("\n C. Guarda datos de alumnos\n");
    printf("\n D. Muestra datos de alumnos\n");
    printf("\n S. Salir\n");
    printf("\n Pulse la opcion deseada: ");
    fflush(stdin);
    scanf("%c", &opcion);
    switch (opcion)
    {
        case 'A':
        case 'a':
            escribirEnArchivo();
        break;
        case 'B':
        case 'b':
            res=cuentaConsonantes();
            printf("\n El archivo tiene %i consonantes\n", res);
        break;
        case 'C':
        case 'c':
            escribirConFormato();
        break;
        case 'D':
        case 'd':
            leerConFormato();
        break;
        case 'S':
        case 's':
            _exit(0);
        break;
    }
    printf("\n\n");
    system("PAUSE");
    system("cls");
  }while (opcion!='S'&& opcion!='s');
}


