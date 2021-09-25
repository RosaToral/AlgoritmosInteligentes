# Busqueda en amplitud

## Algoritmo
El programa utiliza el algoritmo primero en amplitud para encontrar las soluciones de un rompecabezas de piezas móviles.

## Rompecabezas
El rompecabezas consta de un tablero de 9 x 9 en el que se encuentran fichas del 1 al 8 desordenadas.

Las fichas se pueden mover hacia arriba, abajo, izquierda y derecha, pero nunca se pueden sacar del tablero.

El objetivo es ordenar las fichas del 1 al 8 empezando en la esquina superior izquierda del tablero y terminando con un hueco en la esquina inferior derecha.

Estado inicial del rompecabezas
```
|  | 1| 2|
| 4| 5| 3|
| 7| 8| 6|
```

Estado final
```
| 1| 2| 3|
| 4| 5| 6|
| 7| 8|  |
```

El espacio en blanco está representado por un -2.

El codigo está en la carpeta [src](8Puzzle/src)