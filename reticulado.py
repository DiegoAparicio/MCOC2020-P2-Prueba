import numpy as np
from scipy.linalg import solve,inv

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    def __init__(self):
        super(Reticulado, self).__init__()
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        self.Ndimensiones = 2
        self.tiene_solucion = False

    def agregar_nodo(self, x, y, z=0):
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
            self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos +=1
        if z != 0.:
            self.Ndimensiones = 3
        
    def agregar_barra(self, barra):
        self.barras.append(barra)

    def obtener_coordenada_nodal(self, n): 
        if n >= self.Nnodos:
            return 
        return self.xyz[n, :]

    def calcular_peso_total(self):
        peso = 0.
        for b in self.barras:
            peso += b.calcular_peso(self)
        return peso

    def obtener_nodos(self):
        return self.xyz[0:self.Nnodos,:].copy()

    def obtener_barras(self):
        return self.barras








    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Agrega una restriccion, dado el nodo, grado de libertad y valor 
        del desplazamiento de dicho grado de libertad
        """
        if nodo not in self.restricciones:
            self.restricciones[nodo]=[[gdl,valor]]
        else:
            self.restricciones[nodo].append([gdl,valor])

        #Implementar



    def agregar_fuerza(self, nodo, gdl, valor):
        """Agrega una fuerza, dado el nodo, grado de libertad y valor 
        del la fuerza en la direccion de dicho GDL
        """
        if nodo not in self.cargas:
            self.cargas[nodo]=[[gdl,valor]]
        else:
            self.cargas[nodo].append([gdl,valor])
        #Implementar
        


    def ensamblar_sistema(self):
        """Ensambla el sistema de ecuaciones"""
        
        Ngdl = self.Nnodos * self.Ndimensiones

        self.K = np.zeros((Ngdl,Ngdl), dtype=np.double)
        self.f = np.zeros((Ngdl), dtype=np.double)
        self.u = np.zeros((Ngdl), dtype=np.double)
        
        #Implementar
        for barra in self.barras:
            nodo1=barra.ni
            nodo2=barra.nj
            d=[2*nodo1, ((2*nodo1)+1), 2*nodo2, ((2*nodo2)+1)]
            
            for i in range (len(d)):
                p=d[i]
                for j in range(len(d)):
                    q=d[j]
                    ke=barra.obtener_rigidez(self)
                    self.K[p,q]+=ke[i,j]
                #p puede tomar los valores de 2*n1, 2*n1+1,....+=
                    fe=barra.obtener_vector_de_cargas(self)
                    
                self.f[p]+=fe[i]
        
        for carga in self.cargas:
            # nodo 4
            x_o_y=self.cargas[carga][0][0] # x=0, y=1
            fuerza=self.cargas[carga][0][1]
            nodo_a_considerar=carga*2+x_o_y
            self.f[nodo_a_considerar]+=fuerza
        
        return self.K,self.f



    def resolver_sistema(self):
        """Resuelve el sistema de ecuaciones.
        La solucion queda guardada en self.u
        """

        # 0 : Aplicar restricciones
        Ngdl = self.Nnodos * self.Ndimensiones
        gdl_libres = np.arange(Ngdl)
        gdl_restringidos = []

        #Identificar gdl_restringidos y llenar u 
        # en valores conocidos.
        #
        # Hint: la funcion numpy.setdiff1d es util


        #Agregar cargas nodales a vector de cargas 
        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                gdl = carga[0]
                valor = carga[1]
                gdl_global = 2*nodo + gdl
                


        #1 Particionar:
        #       K en Kff, Kfc, Kcf y Kcc.
        #       f en ff y fc
        #       u en uf y uc
        

        # Resolver para obtener uf -->  Kff uf = ff - Kfc*uc
        
        #Asignar uf al vector solucion
        self.u[gdl_libres] = uf

        #Marcar internamente que se tiene solucion
        self.tiene_solucion = True

    def obtener_desplazamiento_nodal(self, n):
        """Entrega desplazamientos en el nodo n como un vector numpy de (2x1) o (3x1)
        """
        dofs = [2*n, 2*n+1]
        return self.u[dofs]



    def recuperar_fuerzas(self):
        """Una vez resuelto el sistema de ecuaciones, se forma un
        vector con todas las fuerzas de las barras. Devuelve un 
        arreglo numpy de (Nbarras x 1)
        """
        
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)

        return fuerzas















    def __str__(self):
        s = "nodos:\n"
        for n in range(self.Nnodos):
            s += f"  {n} : ( {self.xyz[n,0]}, {self.xyz[n,1]}, {self.xyz[n,2]}) \n "
        s += "\n\n"

        s += "barras:\n"
        for i, b in enumerate(self.barras):
            n = b.obtener_conectividad()
            s += f" {i} : [ {n[0]} {n[1]} ] \n"
        s += "\n\n"
        
        s += "restricciones:\n"
        for nodo in self.restricciones:
            s += f"{nodo} : {self.restricciones[nodo]}\n"
        s += "\n\n"
        
        s += "cargas:\n"
        for nodo in self.cargas:
            s += f"{nodo} : {self.cargas[nodo]}\n"
        s += "\n\n"

        if self.tiene_solucion:
            s += "desplazamientos:\n"
            if self.Ndimensiones == 2:
                uvw = self.u.reshape((-1,2))
                for n in range(self.Nnodos):
                    s += f"  {n} : ( {uvw[n,0]}, {uvw[n,1]}) \n "
        s += "\n\n"

        if self.tiene_solucion:
            f = self.recuperar_fuerzas()
            s += "fuerzas:\n"
            for b in range(len(self.barras)):
                s += f"  {b} : {f[b]}\n"
        s += "\n"

        return s
