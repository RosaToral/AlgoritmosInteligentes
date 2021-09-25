/**@author Toral Maldonado Rosa Guadalupe
 * 2153045948
 * Inteligencia Artificial
 * Práctica 2: Algoritmo de primero en amplitud
 */
import java.util.ArrayList;

public class Principal {
    public static void main(String[]args){
        int n = 3;
        int[][] prueba1 = {{-2,1,2},{4,5,3},{7,8,6}};//{1,2,3},{-2,5,6},{7,8,4}
        int[][] fin = {{1,2,3},{4,5,6},{7,8,-2}};//{1,2,3},{4,5,6},{7,8,-2}{-2,1,2},{3,4,5},{6,7,8}
        Estado edofin = new Estado(fin,n);
        Estado prueba = new Estado(prueba1,n);
        //Tablero tab = new Tablero(prueba);
        ArrayList<Estado> lista;// = Tablero.generaEstadosVecinos(prueba);
        
        BusquedaAmplitud busca = new BusquedaAmplitud();
        lista = busca.busquedaAmpitud(prueba, edofin);
        try{
            for (int k = 0; k < lista.size(); k++) {
                for (int i = 0; i < n; i++) {
                    System.out.print("|");
                    for (int j = 0; j < n; j++) {
                        if (lista.get(k).getConfiguracion()[i][j] == -2) {
                            System.out.print(" |");
                        } else {
                            System.out.print(lista.get(k).getConfiguracion()[i][j] + "|");
                        }
                    }
                    System.out.println();
                }
                System.out.println();
            }
        }catch(NullPointerException e){
            System.out.println("No se encontró el espacio en blanco");
        }
    }
}   
