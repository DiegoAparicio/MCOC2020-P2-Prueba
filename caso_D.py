# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:56:45 2020

@author: jpsil
"""


from reticulado import Reticulado
from barra import Barra
from numpy import *
def caso_D():
    # Unidades base
    m = 1.
    kg = 1.
    s = 1. 
    
    
    #Unidades derivadas
    N = kg*m/s**2
    cm = 0.01*m
    mm = 0.001*m
    KN = 1000*N
    
    Pa = N / m**2
    KPa = 1000*Pa
    MPa = 1000*KPa
    GPa = 1000*MPa
    
    # #Parametros
    # L = 5.0  *m
    # F = 100*KN
    # B = 2.0 *m
    # #Parametros cargas vivas
    # Q=400*(kg/(m**2))
    # g=9.8*(m/(s**2))
    # A0=7.5*(m**2)
    # A1=15*(m**2)
    
    #Inicializar modelo
    ret = Reticulado()
    
    #Nodos
    ret.agregar_nodo(0, 0, 0)       #0
    ret.agregar_nodo(5, 0, 0)      #1
    ret.agregar_nodo(10, 0, 0)      #2
    ret.agregar_nodo(15 ,0 ,0)      #3
    ret.agregar_nodo(2.5, 1, 3.5)   #4
    ret.agregar_nodo(7.5, 1, 3.5)  #5
    ret.agregar_nodo(12.5, 1, 3.5)  #6
    ret.agregar_nodo(0, 2, 0)       #7
    ret.agregar_nodo(5, 2, 0)      #8
    ret.agregar_nodo(10, 2, 0)      #9
    ret.agregar_nodo(15, 2, 0)      #10
    
    
    #Barras
    """
    PREGUNTAR, PARECIERA SER QUE ES UNA BARRA CUADRADA
    """
    # A = (8*cm)**2
    # r = sqrt(A/3.141593)
    r = 8.0*cm
    t = 5.0*mm 
    """
    REVISAR EN PROPS R,R DEBERIA SER R,T
    """
    props = [r, t, 200*GPa, 7600*kg/m**3, 420*MPa]
    
    ret.agregar_barra(Barra(0, 1, *props))      # 1
    ret.agregar_barra(Barra(1, 2, *props))      # 2
    ret.agregar_barra(Barra(2, 3, *props))      # 3
    ret.agregar_barra(Barra(3, 10, *props))     # 4
    ret.agregar_barra(Barra(9, 10, *props))     # 5
    ret.agregar_barra(Barra(8, 9, *props))      # 6
    ret.agregar_barra(Barra(7, 8, *props))      # 7
    ret.agregar_barra(Barra(0, 7, *props))      # 8
    ret.agregar_barra(Barra(1, 7, *props))      # 9
    ret.agregar_barra(Barra(0, 8, *props))      # 10
    ret.agregar_barra(Barra(1, 8, *props))      # 11
    ret.agregar_barra(Barra(2, 8, *props))      # 12
    ret.agregar_barra(Barra(1, 9, *props))      # 13
    ret.agregar_barra(Barra(2, 9, *props))      # 14
    ret.agregar_barra(Barra(3, 9, *props))      # 15
    ret.agregar_barra(Barra(2, 10, *props))     # 16
    ret.agregar_barra(Barra(4, 7, *props))      # 17
    ret.agregar_barra(Barra(0, 4, *props))      # 18
    ret.agregar_barra(Barra(4, 8, *props))      # 19
    ret.agregar_barra(Barra(1, 4, *props))      # 20
    ret.agregar_barra(Barra(5, 8, *props))      # 21
    ret.agregar_barra(Barra(1, 5, *props))      # 22
    ret.agregar_barra(Barra(5, 9, *props))      # 23
    ret.agregar_barra(Barra(2, 5, *props))      # 24
    ret.agregar_barra(Barra(6, 9, *props))      # 25
    ret.agregar_barra(Barra(2, 6, *props))      # 26
    ret.agregar_barra(Barra(6, 10, *props))     # 27
    ret.agregar_barra(Barra(3, 6, *props))      # 28
    ret.agregar_barra(Barra(4, 5, *props))      # 29
    ret.agregar_barra(Barra(5, 6, *props))      # 30
    
    
    # nodo 1
    ret.agregar_restriccion(0, 0, 0)
    ret.agregar_restriccion(0, 1, 0)
    ret.agregar_restriccion(0, 2, 0)
    # nodo 7 
    ret.agregar_restriccion(7, 0, 0)
    ret.agregar_restriccion(7, 1, 0)
    ret.agregar_restriccion(7, 2, 0)
    # nodo 3
    ret.agregar_restriccion(3, 1, 0)
    ret.agregar_restriccion(3, 2, 0)
    
    # nodo 10
    ret.agregar_restriccion(10, 1, 0)
    ret.agregar_restriccion(10, 2, 0)
    
    return ret

