import numpy as np

class Reticulado(object):
    """Define un reticulado"""

    def __init__(self):
        super(Reticulado, self).__init__()
        
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}

    def agregar_nodo(self, x, y, z=0):
        #Cambiar Tamaño
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        return
        
    def agregar_barra(self, barra):
        """ Recibe una barra creada y la agrega a la lista barras"""
        
        return self.barras.append(barra)

    def obtener_coordenada_nodal(self, n): 
        """ Me retorna las coordenadas del nodo"""
        
        return self.xyz[n]

    def calcular_peso_total(self):
        """ Entrega el peso total del reticulado (considera todas las barras)"""
        peso_total=0
        for i in self.barras:
            peso_total+=i.calcular_peso(self)
            
        return peso_total

    def obtener_nodos(self):
        """ Nos entrega las coordenadas de todos los nodos dentro de una lista"""
        lista=[]
        for i in range(len(self.xyz)):
            nodo_i=self.obtener_coordenada_nodal(i)
            lista.append(nodo_i)

        return np.array(lista)

    def obtener_barras(self):
        """ Me entrega una lista de elementos tipo Barra"""
        
        return self.barras

    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Implementar"""
        return

    def agregar_fuerza(self, nodo, gdl, valor):
        """Implementar"""
        return

    def ensamblar_sistema(self):
        """Implementar"""
        return

    def resolver_sistema(self):
        """Implementar"""
        return

    def recuperar_fuerzas(self):
        """Implementar"""
        return

    def __str__(self):
        """Implementar"""
        return 

