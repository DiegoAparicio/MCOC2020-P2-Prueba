import numpy as np

from sympy import *
from sympy.solvers.solveset import linsolve
import itertools
from operator import itemgetter
g = 9.81 #kg*m/s^2
m=1.0
mm=m/1000

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
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        xi = reticulado.obtener_coordenada_nodal(self.ni)
        xj = reticulado.obtener_coordenada_nodal(self.nj)
        dij = xi-xj
        return np.sqrt(np.dot(dij,dij))

    def calcular_peso(self, reticulado):
        """Devuelve el largo de la barra. 
        xi : Arreglo numpy de dimenson (3,) con coordenadas del nodo i
        xj : Arreglo numpy de dimenson (3,) con coordenadas del nodo j
        """
        L = self.calcular_largo(reticulado)
        A = self.calcular_area()
        return self.ρ * A * L * g


    def obtener_rigidez(self, ret):
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy,-cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ @ Tθ.T )

    def obtener_vector_de_cargas(self, ret):
        W = self.calcular_peso(ret)
        return np.array([0,0, -W, 0,0, -W])


    def obtener_fuerza(self, ret):
        ue = np.zeros(6)
        ue[0:3] = ret.obtener_desplazamiento_nodal(self.ni)
        ue[3:] = ret.obtener_desplazamiento_nodal(self.nj)
        
        A = self.calcular_area()
        L = self.calcular_largo(ret)

        xi = ret.obtener_coordenada_nodal(self.ni)
        xj = ret.obtener_coordenada_nodal(self.nj)

        cosθx = (xj[0] - xi[0])/L
        cosθy = (xj[1] - xi[1])/L
        cosθz = (xj[2] - xi[2])/L

        Tθ = np.array([ -cosθx, -cosθy,-cosθz, cosθx, cosθy, cosθz ]).reshape((6,1))

        return self.E * A / L * (Tθ.T @ ue)





    def chequear_diseño(self, Fu,ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        revisar si esta barra cumple las disposiciones de diseño.
        """
        A=self.calcular_area()
        Fn=A*self.σy
        
        if ϕ*Fn < abs(Fu):
            return False
        else:
            return True
        

    def obtener_factor_utilizacion(self, Fu, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        calcular y devolver el factor de utilización
        """
        A=self.calcular_area()
        Fn=A*self.σy
        
        factor_de_utilizacion = abs(Fu) / (ϕ*Fn)
        return factor_de_utilizacion


    def rediseñar(self, Fu, ret, ϕ=0.9):
        """Para la fuerza Fu (proveniente de una combinacion de cargas)
        re-calcular el radio y el espesor de la barra de modo que
        se cumplan las disposiciones de diseño lo más cerca posible
        a FU = 1.0.
        """
        
        
        lista_R=np.arange(0.01,0.08,0.005)
        lista_t=np.arange(0.001,0.006,0.001)
        todas_las_combinaciones = list(itertools.product(lista_R, lista_t))
        
        lista_pasa_esbeltez=[]
        for i in todas_las_combinaciones: # Este for evalua la condicion de esbeltez
            Area_combinacion_i=np.pi*(i[0]**2) - np.pi*((i[0]-i[1])**2)
            I_combinacion_i=(np.pi/4)*(i[0]**4 - (i[0] - i[1])**4)
            Largo_combinacion_i=self.calcular_largo(ret)
            eq1=np.sqrt(Largo_combinacion_i/(np.sqrt((I_combinacion_i)/(Area_combinacion_i))))
            if eq1 <= 300.0:
                lista_pasa_esbeltez.append(i)
        
        
        lista_pasa_esbeltez_y_fu=[]
        for j in lista_pasa_esbeltez: # Este for itera sobre la lista "lista_pasa_esbeltez", para el calculo del factor de 
            Area_combinacion_j=np.pi*(j[0]**2) - np.pi*((j[0]-j[1])**2)
            I_combinacion_j=(np.pi/4)*(j[0]**4 - (j[0] - j[1])**4)
            Largo_combinacion_j=self.calcular_largo(ret)
            if Fu < 0.0: # En este caso se evaluan las barras a compresion para verificar con la condicion de carga critica de pandeo
                caso_a=Area_combinacion_j*self.σy
                caso_b=(((np.pi)**2)*self.E*I_combinacion_j)/(Largo_combinacion_j**2)
                Fn=min(caso_a,caso_b)
            if Fu >= 0: # Finalmente se evaluan las barras, con tensiones de traccion y se procede con el calculo del factor de utilizacion.
                Fn=Area_combinacion_j*self.σy
            eq2 = abs(Fu)/(ϕ*Fn)
            if eq2 < 1.0: # se verifica que el Factor de utilizacion sea menor a 1, ya que no puede ser mayor.
                lista_aux=[j[0],j[1],eq2]
                lista_pasa_esbeltez_y_fu.append(lista_aux)
                
        
        maximos_R_t=sorted(lista_pasa_esbeltez_y_fu, key=itemgetter(2))[-1] #se obtiene el radio y espesor respectivo para el maximo factor de utilizacion
        #print (maximos_R_t)
        self.R=maximos_R_t[0]
        self.t=maximos_R_t[1]
       
        return None       


