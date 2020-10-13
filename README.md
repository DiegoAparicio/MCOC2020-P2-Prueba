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
*Nota: el código entregado imprime los gráficos pedidos y el peso de la estructura, ademas imprime los gráficos utilizados en este informe junto con sus deformadas y su desplazamiento máximo.*

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

Desarrollando se llega a que el peso es `P = 977,534 [N]`.
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

El objetivo de la función rediseñar era aumentar el factor de utilización de las barras mediante un cambio tanto en el radio como en el espesor de las barras.
Para esto se creó un arange `lista_R`, el cual poseía todos los valores posibles para el radio. Partiendo por la condición de borde de 1 centímetro y con un incremento de 5 milímetros hasta llegar a los 8 centímetros. Se hizo lo mismo con el espesor creando un arange `lista_t` con todos los valores posibles para el espesor. Partiendo por 1 milimetro y con un incremento de 1 milímetro por iteración hasta llegar a 5 milímetros.
Luego se creo una lista llamada `todas_las_combinaciones` la cual con ayuda de `itertools.product` creaba una lista con todas las combinaciones posibles. Una vez realizado esto se evaluó la condición de esbeltez para todas las combinaciones posibles mediante un ciclo for, donde se redefinió el área, inercia y largo de cada barra. Si la ecuación de esbeltez cumplía con que era menor o igual a 300, las combinaciones se guardaban en una lista llamada `lista_pasa_esbeltez`.
Una vez comprobado el criterio de esbeltez, se procedió a evaluar la condición de carga critica de pandeo. Para esto se redefinió el área, inercia y largo con los valores de la lista `lista_pasa_esbeltez`. Si FU era menor que 0 (lo que implicaría que estaba en pandeo) se procedería a calcular el Fn mínimo. Si FU era mayor o igual a 0 se evaluarían las barras, con sus tensiones de tracción correspondientes y se calcularía el Factor de Utilización con la ecuación `eq2`. Finalmente se evaluaría si la ecuación del factor de utilización era efectivamente menor que 1 (como se pedía en el enunciado). De cumplir con lo anterior, los valores de combinaciones entre el radio y el espesor fueron guardados en la lista `lista_pasa_esbeltez_y_fu`.
Con esta lista creada solo basto ordenar los valores existentes (que contenían el radio, espesor y factor de utilización) y buscar el máximo valor del factor de utilización existente, de manera de asegurar que de todas las posibles combinaciones se estaba retornando el máximo valor posible. Una vez hecho esto se reemplazo los valores de R y t correspondientes y se rediseño la barra.
Gracias a esta función, este proceso se repitió en cada una de las 30 barras. El peso de la estructura muerta, al igual que el peso de la estructura muerta más la carga viva fue de aproximadamente 1 decimo del peso original (del orden de los `2400 N`).


#### 3)
Los criterios de rediseño utilizados son los que se comentaron en 2). Se buscó los valores mas bajos posibles de radio y espesor en cada barra para optimizar su peso y gracias a esto aumentar su factor de utilización. Lo anterior sin descuidar las condiciones de borde impuestas (radio mínimo = 1 cm y espesor mínimo = 1 mm). Los criterios mas importantes fueron definir si la barra se encontraba bajo condiciones de pandeo, y si el FU era mayor a 1 o no. 
Dado que la carga viva es mayo a la carga muerta, la combinación 1.2 (D) + 1.6 (L) produce tensiones mayores a las de la combinación que solo considera la carga muerta 1.4 (D). Por lo tanto se utilizó siempre la combinación de cargas mayor.

##### Tensiones Caso 1.4*D OPTIMIZADO
![image](https://user-images.githubusercontent.com/43451947/95917049-040f0400-0d80-11eb-83ad-d263c988504c.png)

##### Factor de utilizacion Caso 1.4*D OPTIMIZADO
![image](https://user-images.githubusercontent.com/43451947/95917062-0a04e500-0d80-11eb-8bd0-f5a6fc9bfecb.png)

##### Tensiones Caso 1.2*D + 1.6*L OPTIMIZADO
![image](https://user-images.githubusercontent.com/43451947/95917077-0f622f80-0d80-11eb-9b52-0e0b8a3f13e4.png)

##### Factor de Utilización Caso 1.2*D + 1.6*L OPTIMIZADO
![image](https://user-images.githubusercontent.com/43451947/95917094-14bf7a00-0d80-11eb-9d52-6ce3ec8dae00.png)

##### Tensiones Caso eleccion de 5 barras utilizando la combinacion: 1.2*D + 1.6*L 
![image](https://user-images.githubusercontent.com/43451947/95917119-1e48e200-0d80-11eb-8fb8-f2bb5a958729.png)

##### Factor de utilizacion eleccion de 5 barras utilizando la combinacion: 1.2*D + 1.6*L
![image](https://user-images.githubusercontent.com/43451947/95917134-23a62c80-0d80-11eb-8653-a4adf06c2922.png)


#### 4)

##### Antes y despues para combinación de carga: 1,4*D
![image](https://user-images.githubusercontent.com/43451947/95917512-c2328d80-0d80-11eb-85c2-ffff11735605.png)![image](https://user-images.githubusercontent.com/43451947/95917545-d080a980-0d80-11eb-984c-f74cfa756bb0.png)
- El desplazamiento vertical maximo en los nodos antes de los cambios fue de: -0.153 mm
- El desplazamiento vertical maximo en los nodos después de los cambios fue de: -0.228 mm
##### Antes y despues para combinación de carga: 1,2*D + 1,6*L
![image](https://user-images.githubusercontent.com/43451947/95917559-d6768a80-0d80-11eb-86be-97ffa0d51175.png)![image](https://user-images.githubusercontent.com/43451947/95917585-de362f00-0d80-11eb-9c81-538f5d615df3.png)
- El desplazamiento vertical maximo en los nodos antes de los cambios fue de: -2.739 mm
- El desplazamiento vertical maximo en los nodos después de los cambios fue de: -60.259 mm
#### 5)

Se puede observar que el FU se distribuyo de mejor manera. Las barras superiores disminuyeron considerablemente su factor. EL promedio global del FU en la estructura subió, sin que en ningún caso superara el valor máximo FU =1. Debido al rediseño de las barras de la estructura, el cual se tradujo en un cambio en el área de cada sección, el peso total de la estructura disminuyo a 1 decimo de su peso original no rediseñado.

Para mejorar aun más el costo de la estructura, se podría remover las barras cuyo FU es igual a cero (barras 4 y 8) que no estarían aportando a la estructura. Adicional a lo anterior, se podría reemplazar aquellas barras que estén en tracción por cables, disminuyendo aun mas el peso total de la estructura.
