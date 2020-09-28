import numpy as np

g = 9.81 #kg*m/s^2

class Barra(object):

    """Constructor para una barra"""
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy
    
    def obtener_conectividad(self):
        """Implementar"""
        
        return np.array([self.ni,self.nj])

    def calcular_area(self):
        """Calculo de area de barra circular hueca"""
        area = ((self.R)**2)*(np.pi) - ((self.R-self.t)**2)*(np.pi)
        
        return area

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra.
        Con las coordenadas de 2 nodos, se obtiene el largo de la barra
        
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        
        nodo1=reticulado.obtener_coordenada_nodal(self.ni)
        nodo2=reticulado.obtener_coordenada_nodal(self.nj)
        distancia= ((nodo1[0]-nodo2[0])**2 + (nodo1[1]-nodo2[1])**2 + (nodo1[2]-nodo2[2])**2)**0.5
        return distancia

    def calcular_peso(self, reticulado):
        """ Retorna el peso de cada barra
        
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """        
        peso=self.ρ*self.calcular_largo(reticulado)*self.calcular_area()*g
        
        return peso












