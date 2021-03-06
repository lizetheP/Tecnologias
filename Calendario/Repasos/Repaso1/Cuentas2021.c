/*Algoritmo: Cuentas bancarias
var
   caracter : opcion1, opcion2
   real : saldo, saldof, interes
inicio
   escribir("MENU
                a. Mostrar tabla
                b. Calcular saldo
                s. Salir   ")
   escribir("Introduce una opcion")
   leer(opcion1)
   caso_de (opcion1) hacer
      'A':
      'a':
           escribir("Mostrar tabla...")
      'B':
      'b':
           escribir ("Dame el saldo inicial");
           leer(saldo)
           escribir ("MENU 2
                TIPO DE CUENTA
                a. Libreton
                b. Banorte F?cil
                c. Ahorro Scotiabank ")
           escribir ("Introduce una opcion")
           leer(opcion2)
           caso_de (opcion2) hacer
              'a':
              'A':
                  si (saldo < 750)
                      saldof = saldo - 75
                  si_no
                      interes = saldo*1.05/100
                      saldof = saldo + interes
                  escribir("saldof")
              'b':
              'B':
                  si (saldo < 1000)
                      saldof = saldo - 75
                  si_no
                      interes = saldo*1.35/100
                      saldof = saldo + interes
                  escribir("saldof")
              'c':
              'C':
                  si (saldo < 2000)
                      saldof = saldo - 60
                  si_no
                      interes = saldo*0.9/100
                      saldof = saldo + interes
                  escribir("saldof")
               default:
                  esciribr("Opci?n invalida")
      's':
      'S':
           salir del programa
      default:
           escribir ("Opci?n invalida")
    fin_caso
  fin                      */

#include <stdio.h>
#include <stdlib.h>

void main()
{
  char opcion1, opcion2;
  float saldo, saldof, interes;

  printf("\n MENU PRINCIPAL");
  printf("\n a. Muestra los tipos de cuenta de ahorro");
  printf("\n b. Calcular el saldo despu?s de intereses o comisiones");
  printf("\n s. Salir  \n");
  printf("\n Introduce una opcion: ");
  scanf("%c", &opcion1);
  fflush(stdin); // LIBERA LA MEMORIA
  switch(opcion1)
  {
     case 'A':
     case 'a':
            printf("\n Banco \t \t Nombre de  \t \t Tasa de    \t Saldo     Cuota por ");
            printf("\n            \t cuenta            \t interes         minimo    manejo");
            printf("\n                                      \t mensual                   de cuenta");
            printf("\n----------------------------------------------------------------------------------------");
            printf("\n Bancomer \t Libreton     \t \t 1.05% \t\t $750.00    $75.00 ");
            printf("\n Banorte  \t Banorte Facil  \t 1.35% \t\t $1000.00   $75.00 ");
            printf("\n Scotiabank \t Ahorro Scotiabank  \t 0.9% \t\t $2000.00   $60.00 ");
     break;
     case 'B':
     case 'b':
            printf("\n Dame el saldo inicial: ");
            scanf("%f", &saldo);
            printf("\n\n TIPO DE CUENTA \n\n");
            printf("\n a. Libreton ");
            printf("\n b. Banorte facil");
            printf("\n c. Ahorro Scotiabank \n");
            printf("\n\n Introduce una opcion: ");
            fflush(stdin);
            scanf("%c", &opcion2);
            switch (opcion2)
            {
              case 'a':
              case 'A':
                  if (saldo < 750)
                     saldof = saldo - 75;
                  else
                  {
                     interes = saldo * 1.05/100;
                     saldof = saldo + interes;
                  }
                  printf("\n El saldo final es %f", saldof);
              break;
              case 'b':
              case 'B':
                  if (saldo < 1000)
                     saldof = saldo - 75;
                  else
                  {
                     interes = saldo * 1.35/100;
                     saldof = saldo + interes;
                  }
                  printf("\n El saldo final es %f", saldof);
              break;
              case 'c':
              case 'C':
                  if (saldo < 2000)
                     saldof = saldo - 60;
                  else
                  {
                     interes = saldo * .9/100;
                     saldof = saldo + interes;
                  }
                  printf("\n El saldo final es %f", saldof);
              break;
              default:
                  printf("\n ERROR opcion invalida");
            }
      break;
      case 's':
      case 'S':
            printf("\n ADIOS \n\n");
            _exit(0);
      break;
      default:
           printf("\n ERROR Opcion invalida");
    }
  printf("\n\n");
  system("PAUSE");
}
