# LABORATORIO 01 

## Descripción General
- El siguiente laboratorio consiste en una serie de ejercicios para el desarrollo de programación en **sintaxis de Python**, además de evaluación de conceptos vistos en clases anteriores.
- El objetivo de este laboratorio está en el uso de la **condicional IF**, **creación de funciones**, **validación de los parámetros** y recuerde que en cada función que desarrollen agregar los **comentarios** (nombre, parámetros entrada, salida y restricciones).
- Finalizado el laboratorio subir el archivo con el nombre de **Laboratorio01.py**, la entrega cierra a las **3pm del 7 de marzo del 2025** y será a través del Github Classroom...
- Deben ser muy claros con los mensajes de error que programen en su código.
- Como observación, no solo se califica el correcto funcionamiento del código sino también las validaciones, comentarios y el uso correcto de las funciones o bloques de código permitidos


## calcularRenta(monto)
Implemente una función que ayude a calcular el valor a tributar por concepto del **impuesto de renta sobre el salario**. El parámetro **monto** debe ser de tipo entro y mayor a CERO. En la imagen adjunta viene el rango de salarios para aplicar el porcentaje correcto de los impuestos

Ilustración 1 Impuesto de renta para asalariados
![image](https://user-images.githubusercontent.com/1167750/156645626-d394119c-ec54-4368-8df4-0d4a09d2b186.png)
Fuente: https://www.hacienda.go.cr/contenido/14448-ejemplos-calculos-impuesto-sobre-la-renta

Cómo se calcula:

-	Si el salario es de 700,000 mensuales, no pago impuesto de renta, ¿por qué?, según la tabla estoy exento ya que este salario está por debajo de los 817,000 colones

-	Si mi salario es de un 1,000,000 de colones, entonces este ingreso está dentro del rango del 817,000 y 1,226,000 entonces el exente de este se le aplica un 10%, es decir: (1,000,000 – 817,000) * 10% = 18,300

-	Ahora, si mi salario es de 2,000,000, aplicaría el 15%, entonces:
  Menor a 817,000 no pago
  (1,226,000 – 817,000) * 10% = 40,900
  (2,000,000 – 1,226,000) * 15% = 116,100
  Entonces el impuesto de renta que tengo que pagar por un salario de 2,000,000 de colones es 157,000, que es el resultado de la suma 40,900 + 116,100

``` python
>>> calcularRenta(700000)
0
>>> calcularRenta(1000000)
18300
>>> calcularRenta(2000000)
157000

``` 

## contadorDigitos(num, digito)
Implemente una función llamada contadorDigitos(num, digito) donde se espera que la salida retorne el número de veces que el dígito aparece en el número. Ambos parámetros deben ser de tipo entero, el párametro llamado **digito** debe ser menor a 10 y mayor igual a 0. Ejemplo
``` python
>>> contadorDigitos(102039480, 0)
3
>>> contadorDigitos(132033483, 3)
4
``` 

## calculadora(operacion, op1, op2)
Escriba una calculadora, que reciba 3 parámetros, el primero consiste en la operación y después los dos operadores, y que calcule el resultado y posteriormente lo imprima en pantalla. Las operaciones soportadas son **suma=1, resta=2, multiplicación=3 y división=4** (no es posible la división entre 0). Los parámetros deben ser de tipo entero, el parámetros **operacion** debe permitir valores 1,2,3 y 4, loa operadores deben ser de tipo entero.
``` python
>>> calculadora (1, 4, 8)
12
>>> calculadora (2, 4, 8)
-4
>>> calculadora (3, 4, 8)
32
>>> calculadora (4, 4, 8)
0.5
``` 
