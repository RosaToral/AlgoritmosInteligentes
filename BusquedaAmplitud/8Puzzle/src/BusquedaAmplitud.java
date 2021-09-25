/**@author Toral Maldonado Rosa Guadalupe
 * 2153045948
 * Inteligencia Artificial
 * Práctica 2: Algoritmo primero en amplitud
 */

import java.util.ArrayList;
import java.util.Arrays;

public class BusquedaAmplitud {
    //Los arreglos representarán colas con recorrido (Se toman de la primer 
    //posición y se recorre el resto de los datos)
    private ArrayList<Estado> cola = new ArrayList<>();
    private ArrayList<Estado> hijos = new ArrayList<>();
    private ArrayList<Estado> edosNuevos = new ArrayList<>();
    private ArrayList<Estado> revisados = new ArrayList<>();
    private Estado siguiente, revisado;
            
    public ArrayList<Estado> busquedaAmpitud(Estado edoIni, Estado edoFin){
        cola.add(edoIni);
        //Debido a que es una cola, entonces se toma el primer elemento
        siguiente = cola.get(0);
        edosNuevos = Tablero.generaEstadosVecinos(siguiente);
        insertaEnHijos(edosNuevos, revisados);
        while(!cola.isEmpty()){
            revisado = cola.remove(0);
            revisados.add(revisado);
            //Se comopara. Si la configuración del estado revisado es igual a 
            //la confugiración del estado final, devuelve la cola revisados y se sale del método.
            if(Arrays.deepEquals(revisado.getConfiguracion(), edoFin.getConfiguracion()))
                return revisados;
            else{
                //Se mueven los estados de la cola hijos a la cola
                while(!hijos.isEmpty())
                    cola.add(hijos.remove(0));
                siguiente = cola.get(0);
                edosNuevos = Tablero.generaEstadosVecinos(siguiente);
                insertaEnHijos(edosNuevos, revisados);
            }
        }
        System.out.println("No se encontró la solución");
        return revisados;
    }

    private void insertaEnHijos(ArrayList<Estado> edosNuevos, ArrayList<Estado> revisados) {
        //Si en revisados no hay contra qué comparar, se agregan todos los estados nuevos a la cola hijos
        if(revisados.isEmpty())
            for(int i = 0; i < edosNuevos.size(); i++)
                hijos.add(edosNuevos.get(i));
        else{
            // Para indicar si dos configuraciones son iguales: 1 si sin iguales, 0 si son distintas
            int bandera = 0;
            for(int k = 0; k < edosNuevos.size(); k++){//Recorre el arreglo edosNuevos
                for(int m = 0; m < revisados.size(); m++){//Recorre el arreglo revisados
                    //Se reinicia bandera para poder comparar el siguiente elemento
                    bandera = 0;
                    //Se compara, si el estado m de la cola revisados es igual 
                    //al estado m del arreglo edosNuevos, cambia la bandera a 1 y se sale del primer for
                    if(Arrays.deepEquals(edosNuevos.get(k).getConfiguracion(), revisados.get(m).getConfiguracion())){
                        bandera = 1;
                        break;
                    }
                }
                //Se evita guardar el mismo elemento en revisados 2 veces
                if(bandera == 0)
                    hijos.add(edosNuevos.get(k));
            }
        }
    } 
}
