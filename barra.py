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
        return [self.ni, self.nj]

    def calcular_area(self):
        A = np.pi*(self.R**2) - np.pi*((self.R-self.t)**2)
        return A

    def calcular_largo(self, reticulado):
        """Devuelve el largo de la barra. 
        ret: instancia de objeto tipo reticulado
        """
        x_i = reticulado.obtener_coordenada_nodal(self.ni)
        x_j = reticulado.obtener_coordenada_nodal(self.nj)
        
        dij = x_i-x_j
        
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        ret: instancia de objeto tipo reticulado
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        return self.ρ * A * L * g



    def obtener_rigidez(self, ret):
        """Devuelve la rigidez ke del elemento. Arreglo numpy de (4x4)
        ret: instancia de objeto tipo reticulado
        """
        
        #implementar
        xi=ret.xyz[self.ni,0]
        yi=ret.xyz[self.ni,1]
        
        xj=ret.xyz[self.nj,0]
        yj=ret.xyz[self.nj,1]
        
        menos_cos_teta = (xi-xj)/self.calcular_largo(ret)
        menos_sin_teta = (yi-yj)/self.calcular_largo(ret)
        mas_cos_teta   = (xj-xi)/self.calcular_largo(ret)
        mas_sin_teta   = (yj-yi)/self.calcular_largo(ret)

        T_teta= np.array([[menos_cos_teta], [menos_sin_teta], [mas_cos_teta], [mas_sin_teta]])

        
        A=self.calcular_area()
        E_barra = self.E
        L=self.calcular_largo(ret)
        
        ke = T_teta @ T_teta.T * (A*E_barra)/L
        
        return ke

    def obtener_vector_de_cargas(self, ret):
        """Devuelve el vector de cargas nodales fe del elemento. Vector numpy de (4x1)
        ret: instancia de objeto tipo reticulado
        """

        #Implementar
        W_partido_2=self.calcular_peso(ret)/2.0
        fe=np.array([[0],[-1],[0],[-1]])*W_partido_2 #[[],[]]
          
        return fe


    def obtener_fuerza(self, ret):
        """Devuelve la fuerza se que debe resistir la barra. Un escalar tipo double. 
        ret: instancia de objeto tipo reticulado
        """

        #Implementar
        A=self.calcular_area()
        E_barra = self.E
        L=self.calcular_largo(ret)
        
        nodo1=self.ni
        nodo2=self.nj
        ue=np.array([ret.u[nodo1*2], ret.u[((2*nodo1)+1)], ret.u[2*nodo2], ret.u[((2*nodo2)+1)]])
        
        xi=ret.xyz[self.ni,0]
        yi=ret.xyz[self.ni,1]
        
        xj=ret.xyz[self.nj,0]
        yj=ret.xyz[self.nj,1]
        
        menos_cos_teta = (xi-xj)/L
        menos_sin_teta = (yi-yj)/L
        mas_cos_teta   = (xj-xi)/L
        mas_sin_teta   = (yj-yi)/L

        T_teta= np.array([[menos_cos_teta], [menos_sin_teta], [mas_cos_teta], [mas_sin_teta]])
        
        
        se = (A*E_barra)/L * T_teta.T @ ue

        return se



