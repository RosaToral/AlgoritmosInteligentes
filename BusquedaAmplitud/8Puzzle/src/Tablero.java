/**@author Toral Maldonado Rosa Guadalupe
 * 2153045948
 * Inteligencia Artificial
 * Práctica 1: 8-puzzle
 */
import java.util.ArrayList;
import java.util.Queue;

public class Tablero {
    private static int[][] configuracion;
    private static int n;
    //Variables que guardan la posicion del espacio en blanco
    private static int col = 0, fil = 0;

    /**Metodo que genera todas las posibles configuraciones
     * @return una cola con las configuraciones del tablero
     */
    public static ArrayList<Estado> generaEstadosVecinos(Estado estado){
        Tablero.configuracion = estado.getConfiguracion();
        Tablero.n = estado.getTamano();
        if(buscarEspacio() == 0)
            return null;
        else{
            //Arreglo para guardar todas las configuraciones
            ArrayList<Estado> lista = new ArrayList<>();
            //Variable que indica el movimiento: 1 para abajo o derecha; o -1 para hacia arriba o izquierda
            int mov = 1;
            //Se hace un for doble ya que se tienen 4 posibles movimientos (izquierda, derecha, arriba o abajo)
            for (int k = 0; k < 2; k++) {
                //Esquina inferior derecha. Solo se puede mover hacia arriba o hacia la izquierda
                if ((col == n-1 && fil == n-1)) 
                    mov = -1;
                
                //Se mueven las columnas
                if(col == n-1 && fil == 0 && mov == 1){//Esquina superior derecha. No se puede mover hacia la derecha
                }else{
                    if(col == 0 && fil == n-1 && mov == -1){//Esquina inferior izquierda. No se puede mover a la izquierda
                    }else{
                         if(col == n-1 && fil < n-1 && mov == 1){//Orilla derecha. No se puede mover a la derecha
                         }else{ 
                             if(col == 0 && fil < n-1 && mov == -1){//Orilla izquierda. No se puede mover hacia la izquierda
                             }else{//Centro. Tiene los 4 movimientos
                                //Variable que va a guardar el estado actual del tablero
                                int[][] auxiliar = new int[n][n];
                                Estado resultado = new Estado(auxiliar,n);
                                //Se mueven las columnas y se guarda la nueva configuración en la última posición para simular una cola
                                lista.add(lista.size(),moverColumnas(resultado, mov));
                             }
                        }
                    }
                }
                //Se mueven las filas
                if(col == n-1 && fil == 0 && mov == -1){//Esquina superior derecha. No se puede mover hacia arriba
                }else{
                    if(col == 0 && fil == n-1 && mov == 1){//Esquina inferior izquierda. No se puede mover hacia abajo
                    }else{
                        if(col < n-1 && fil == n-1 && mov == 1){//Orilla inferior. No se puede mover hacia abajo
                        }else{
                            if(col < n-1 && fil == 0 && mov == -1){//Orilla superior. No se puede mover hacia arriba
                            }else{//Centro. Tiene los 4 movimientos
                                //Se reinicia el contenido de la variable resultado
                                int[][] auxiliar = new int[n][n];
                                Estado resultado = new Estado(auxiliar,n);
                                //Se mueven las filas y se guarda la nueva configuración en la última posición para simular una cola
                                lista.add(lista.size(),moverFilas(resultado, mov));
                            }
                        }
                    }
                }
                //Esquina superior izquierda. Solo se puede mover hacia la derecha o hacia la izquierda
                if (col == 0 && fil == 0){
                }else 
                    mov = -1;
                //Esquinas inferior derecha o superior izquierda. Solo tienen 2 movimientos
                if ((col == n-1 && fil == n-1) || (col == 0 && fil == 0)) 
                    break;//Se detiene el for para que sólo hayan 2 movimientos
            }
            return lista;
        }
    }
    
    /**Método que busca el espacio vacío
     * @return 1 si se encontró el espacio vacío, 0 si no se encontró
     */
    private static int buscarEspacio(){
        for(fil = 0; fil < n; fil++)
            for(col = 0; col < n; col++)
                if(configuracion[fil][col] == -2)//El espacio se representa con un -2
                    return 1;
            
        return 0;
    }
    
    /**Método que mueve las columnas
     * @param resultado
     * @param mov
     * @return una matriz con la nueva configuración
     */
    private static Estado moverColumnas(Estado resultado, int mov) {
        //Auxiliar que ayuda a intercambiar las posiciones
        int aux;
        //Se copia el contenido de la matriz configuración a la matriz resultado
        for (int i = 0; i < n; i++) {
            System.arraycopy(configuracion[i], 0, resultado.getConfiguracion()[i], 0, n);
        }
        aux = resultado.getConfiguracion()[fil][col];
        resultado.getConfiguracion()[fil][col] = resultado.getConfiguracion()[fil][col + mov];
        resultado.getConfiguracion()[fil][col + mov] = aux;
        return resultado;
    }
    
    /**Método que mueve las filas
     * @param resultado
     * @param mov
     * @return una matriz con la nueva configuración
     */
    private static Estado moverFilas(Estado resultado, int mov) {
        //Auxiliar que ayuda a intercambiar las posiciones
        int aux;
        //Se copia el contenido de la matriz configuración a la matriz resultado
        for (int i = 0; i < n; i++) {
            System.arraycopy(configuracion[i], 0, resultado.getConfiguracion()[i], 0, n);
        }
        aux = resultado.getConfiguracion()[fil][col];
        resultado.getConfiguracion()[fil][col] = resultado.getConfiguracion()[fil + mov][col];
        resultado.getConfiguracion()[fil + mov][col] = aux;
        return resultado;
    }
}