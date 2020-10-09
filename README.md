# MCOC2020-P2

## Entrega 1

En un principio se clonó el repertorio del profesor en github desktop. Sin embargo al momento de intentar realizar los pull, nos indicaba que no eramos administradores y que teniamos que pedir autorizacion.
Para facilitar el proceso, tanto para nosotros como para los correctores, decidimos crear un repositorio nuevo ("MCOC2020-P2-Prueba"). Este repositorio fue creado por Diego Aparicio (Jefe) y se hizo colaboradores a Juan Pablo Silva y Matías León. Una vez creado, se cargaron los archivos del profesor en blanco (es decir, las funcniones no definidas), y posteriormente cada integrante subio los cambios correspondientes para poder correr la Entrega 1.
Dado que fue la primera entrega, el `__string__(self)` fue subido en el archivo reticulado.py por Juan Pablo Silva, en vez de Diego Aparicio. Sin embargo fue Diego quien se encargo de esta parte. Para evitar un desorden en los changes del repositorio, esto se dejo asi en vez de eliminar un par de lineas y volver a subirlas con otro usuario.

### Gráfico 2D
![image](https://user-images.githubusercontent.com/43451947/94461302-53561180-0190-11eb-82bf-1ead6895add5.png)

### Imagen salida código entrega 1
![image](https://user-images.githubusercontent.com/43451947/94461311-594bf280-0190-11eb-9569-fce93473ee26.png)

*Dato:* nosotros utilizamos el mismo tipo de indentacion todo el tiempo, el profesor afirmo en clases que windows y linux eran distintos en cuendo a este tema pero que su computador o programa era "inteligente" y transformaba unos en otros, por lo que no habría problemas.

## Entrega 2

### Gráfico 2D
![image](https://user-images.githubusercontent.com/43451947/94840041-36b71500-03ee-11eb-9b09-b3e239d59dc2.png)

### Imagen salida código entrega 2
![image](https://user-images.githubusercontent.com/43451947/94840200-71b94880-03ee-11eb-8483-0e243c3b53c0.png)
![image](https://user-images.githubusercontent.com/43451947/94840233-7d0c7400-03ee-11eb-9e66-1c545049ea23.png)

## Entrega 4

Programa entrega los siguientes graficos:
### Reticulado
![RETICULADO](https://user-images.githubusercontent.com/43649125/95604093-8ec4cb80-0a2d-11eb-8667-510610c5a3d7.png)

### Tensiones Caso 1
![TENSIONES 1 (D)](https://user-images.githubusercontent.com/43649125/95604110-97b59d00-0a2d-11eb-9d3d-9d5b8108790a.png)

### Tensiones Caso 2
![TENSIONES 2 (D+L)](https://user-images.githubusercontent.com/43649125/95604116-9ab08d80-0a2d-11eb-8e87-e63bd50f82b6.png)

### Factor de Utilización Caso 1
![FU 1 (D)](https://user-images.githubusercontent.com/43649125/95604137-a0a66e80-0a2d-11eb-9f9f-c6af956e1c42.png)

### Factor de Utilización Caso 2
![FU (D+L)](https://user-images.githubusercontent.com/43649125/95604141-a3a15f00-0a2d-11eb-9310-0a49fe8b967e.png)

Peso total de la estructura: `24.197,44 [N]`

### Informe

#### 1)
Las barras a rediseñar serán: 
* Barra 9: nodos(1,7)
* Barra 10: nodos(10,8)
* Barra 13: nodos(1,9)
* Barra 15: nodos(3,9)
* Barra 16: nodos(2,10)

En primer lugar se debe calcular el largo inicial de las barras. En este caso todas las barras poseerán el mismo largo debido a la simetria del problema en los rectangulos de la base (largo = 5m, ancho = 2m). Por lo que para encontrar el largo inicial de las barras solo hace falta aplicar el Teorema de Pitagoras. Con esto llegamos a que `L = 5,38516 [m]`.
Una vez calculado el largo, se procede a calcular el area inicial. Para esto hay que considerar que la barra es hueca y posee un radio `R = 8 [cm]`y un espesor `t = [5 mm]`. Para calcular el area se utiliza la siguiente formula:

![CodeCogsEqn](https://user-images.githubusercontent.com/43649125/95619189-96dc3580-0a44-11eb-872c-92a031fb27a0.gif)

Con esto llegamos a que el area de las barras es `A = 0.00243473 [m2]`.
El paso siguiente es calcular el peso de cada barra, para esto se debe multiplicar el volumen por la densidad, lo cual se puede reescribir de la siguiente forma:

![CodeCogsEqn (1)](https://user-images.githubusercontent.com/43649125/95620406-82993800-0a46-11eb-8e65-4037413d6d95.gif)

La densidad tiene un valor de:

![CodeCogsEqn (9)](https://user-images.githubusercontent.com/43649125/95626377-87fb8000-0a50-11eb-8283-8991f247ad7a.gif)

Desarrollando se llega a que el peso es `P = 977,534 [N]`
Para obtener el Factor de Utilizacion de las barras utilizamos la función:

![CodeCogsEqn (2)](https://user-images.githubusercontent.com/43649125/95621487-27684500-0a48-11eb-9198-7ac82172ab63.gif)

Donde:

![CodeCogsEqn (7)](https://user-images.githubusercontent.com/43649125/95624690-a7dd7480-0a4d-11eb-87a0-669675064843.gif)

![CodeCogsEqn (8)](https://user-images.githubusercontent.com/43649125/95624741-baf04480-0a4d-11eb-88c3-77712f6b6329.gif)

Los valores de las tensiones se obtuvieron de los graficos generados. Desarrollando llegamos a que los Factores de Utilizacion de las barras son:
* FU Barra 9 `= 0,011455`
* FU Barra 10 `= 0,011455`
* FU Barra 13 `= 0,022808`
* FU Barra 15 `= 0,011455`
* FU Barra 16 `= 0,011455`

Para rediseñar las barras, se consideró el hecho de que estaban en tracción, por lo tanto se descarto el calculo de la condición de la carga critica de pandeo. Despues se disminuyó el radio en razon de 5 [mm] para asi disminuir el area transversal. De la misma manera se disminuyo el espesor en razon de 1 [mm] para asi aumentar el factor de utilización. Para las condiciones de borde se consideró un radio minimo de 1 [cm] y un espesor minimo de 1[mm] para asi mantener la veracidad del reticulado con las solicitaciones de la vida real.
En primer lugar se evaluó la condición de esbeltez. La cual tenia que cumplir lo siguiente:

![CodeCogsEqn (5)](https://user-images.githubusercontent.com/43649125/95624021-95167000-0a4c-11eb-94bb-35cd68461926.gif)

Donde I corresponde a la inercia y se define como:

![CodeCogsEqn (4)](https://user-images.githubusercontent.com/43649125/95623681-1ae5eb80-0a4c-11eb-92e6-20b58cd577a7.gif)

Desarrollando se llegó a que la esbeltez de las barras fue la siguiente:
* Barra 9 `= 9,91044`
* Barra 10 `= 9,91044`
* Barra 13 `= 9,91044`
* Barra 15 `= 9,91044`
* Barra 16 `= 9,91044`

Utilizando esta informacion, se prodeció a iterar posibles valores de R y t. Finalmente el rediseño consideró los valores minimos posibles establecidos por las condiciones de borde `R = 1 [cm]` y `t = 1[mm]`.
Finalmente utilizando las ecuaciones mencionadas anteriormente se llegó a los siguientes valores:
* FU Optimizado Barra 9 `= 0,467233`
* FU Optimizado Barra 10 `= 0,467233`
* FU Optimizado Barra 13 `= 0,930338`
* FU Optimizado Barra 15 `= 0,467233`
* FU Optimizado Barra 16 `= 0,467233`

El peso total de la estructura optimizada, considerando solo el cambio de las 5 barras mencionadas fue de: `19.429,58 [N]`

#### 2)

#### 3)

##### Factor de Utilización Caso 1 OPTIMIZADO
![FU 1 (D) OPTIMIZADO](https://user-images.githubusercontent.com/43649125/95617442-d3f2f880-0a41-11eb-90ef-95f5d74457e5.jpeg)

##### Factor de Utilización Caso 2 OPTIMIZADO
![FU 2 (D+L) OPTIMIZADO](https://user-images.githubusercontent.com/43649125/95617458-d7867f80-0a41-11eb-9599-0c0ccc0bd223.png)

#### 4)
#### 5)
