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


### Informe

#### 1
Las barras a rediseñar serán: 9 nodos(1,7), 10 nodos(10,8), 13 nodos(1,9), 15 nodos(3,9), 16 nodos(2,10).
En primer lugar se debe calcular el largo inicial de las barras. En este caso todas las barras poseerán el mismo largo debido a la simetria del problema en los rectangulos de la base (largo = 5m, ancho = 2m). Por lo que para encontrar el largo inicial de las barras solo hace falta aplicar el Teorema de Pitagoras. Con esto llegamos a que `L = 5,38516 [m]`.
Una vez calculado el largo se procede a claular el area inicial. Para esto hay que considerar que la barra es hueca y posee un radio `R = 8 [cm]`y un espesor `t = [5 mm]`. Para calcular el area se utiliza la siguiente formula:
![CodeCogsEqn](https://user-images.githubusercontent.com/43649125/95619189-96dc3580-0a44-11eb-872c-92a031fb27a0.gif)
Con esto llegamos a que el area de las barras es `A = 0.00243473 [m2]`.
El paso siguiente es calcular el peso de cada barra, para esto se debe multiplicar el volumen por la densidad, lo cual se puede reescribir de la siguiente forma:
![CodeCogsEqn (1)](https://user-images.githubusercontent.com/43649125/95620406-82993800-0a46-11eb-8e65-4037413d6d95.gif)
Desarrollando se llega a que el peso es `P = 977,534 [N]`
Para obtener el Factor de Utilizacion de las barras utilizamos la función:
![CodeCogsEqn (2)](https://user-images.githubusercontent.com/43649125/95621487-27684500-0a48-11eb-9198-7ac82172ab63.gif)

#### 2
#### 3

##### Factor de Utilización Caso 1 OPTIMIZADO
![FU 1 (D) OPTIMIZADO](https://user-images.githubusercontent.com/43649125/95617442-d3f2f880-0a41-11eb-90ef-95f5d74457e5.jpeg)

##### Factor de Utilización Caso 2 OPTIMIZADO
![FU 2 (D+L) OPTIMIZADO](https://user-images.githubusercontent.com/43649125/95617458-d7867f80-0a41-11eb-9599-0c0ccc0bd223.png)

#### 4
#### 5
