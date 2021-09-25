/**@author Toral Maldonado Rosa Guadalupe
 * 2153045948
 * Inteligencia Artificial
 * Práctica 1: 8-puzzle
 */
public class Estado {
    private int[][] configuracion;
    private int n;
    /**Constructor de la clase Estados
     * @param configuracion
     * @param n 
     */
    public Estado(int[][] configuracion, int n){
        this.configuracion = configuracion;
        this.n = n;
    }
    
    /**Método que permite obtener la configuración actual de un estado
     * @return una matriz con una configuración
     */
    public int[][] getConfiguracion(){
        return configuracion;
    }
    
    /**Método que permite editar la configuración de unestado
     * @param configuracion 
     */
    public void setConfiguracion(int[][] configuracion){
        for(int i = 0; i < n; i++)
            System.arraycopy(configuracion[i], 0, this.configuracion[i], 0, n);
    }
    
    /**Método que permite obtener el tamaño de la configuración
     * @return un entero con el tamaño de la matriz
     */
    public int getTamano(){
        return n;
    }
    
}
