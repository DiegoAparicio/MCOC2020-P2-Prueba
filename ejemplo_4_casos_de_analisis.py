from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d
import itertools
from operator import itemgetter
from numpy import *
ret_D = caso_D()
ret_L = caso_L()
#Casos optimizados
ret_D_muerto = caso_D()
ret_D_vivo_muerto = caso_D()
ret_D_5_barras = caso_D()
factor_a=30.0

ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=180.,
    deshabilitar_ejes=True)


#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
ret_D_muerto.ensamblar_sistema()
ret_D_muerto.resolver_sistema()
ret_D_vivo_muerto.ensamblar_sistema()
ret_D_vivo_muerto.resolver_sistema()
ret_D_5_barras.ensamblar_sistema()
ret_D_5_barras.resolver_sistema()

f_D = ret_D.recuperar_fuerzas()
f_D_muerto = ret_D_muerto.recuperar_fuerzas()
f_D_vivo_muerto = ret_D_vivo_muerto.recuperar_fuerzas()
f_D_5_barras = ret_D_5_barras.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()
#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2
f_3_D_muerto = 1.4*f_D_muerto
f_4_D_vivo_muerto = 1.2*f_D_vivo_muerto + 1.6*f_L
f_5_D_5_barras = 1.2*f_D_5_barras + 1.6*f_L

# Calcular factores 
FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)



import matplotlib.pyplot as plt

# CASO 1
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 1: 1.4 D ")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.4),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# print(array(ret_D.desplazamientos_verticales)[:,0])
# ret_D.desplazamientos_verticales=[]
# plt.legend()
plt.show()


# CASO 2
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.2+ret_L.u*1.6),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]

plt.show()



# CASO 3
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 1: 1.4 D ")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.4),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]
plt.show()


# CASO 4
ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 2: 1.2 D + 1.6 L")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D.u*1.2+ret_L.u*1.6),3)} [mm]")
# ret_D_desplazamientos_max=sorted(ret_D.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_desplazamientos_max[0]}: {round(ret_D_desplazamientos_max[1]*1000,3)}[mm] ')
# ret_D.desplazamientos_verticales=[]
plt.show()


peso = ret_D.calcular_peso_total()

print(f"peso original = {peso}")



barras_a_rediseñar = [i for i in range(30)]
# barras_a_rediseñar = [8,9,12,14,15]

#                   CASO DE CARGA MUERTA OPTIMIZADA
barras_muerto = ret_D_muerto.obtener_barras()
barras_vivas=ret_L.obtener_barras()
for i in barras_a_rediseñar:
    barras_muerto[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
    barras_vivas[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
        

ret_D_muerto.ensamblar_sistema()
ret_D_muerto.resolver_sistema()        

ret_L.ensamblar_sistema()
ret_L.resolver_sistema()

f_L = ret_L.recuperar_fuerzas()

FU_caso_muerto = ret_D_muerto.recuperar_factores_de_utilizacion(f_3_D_muerto)
f_D_muerto = ret_D_muerto.recuperar_fuerzas()
f_3_D_muerto = 1.4*f_D_muerto  




ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_muerto.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_3_D_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 3: 1.4 D  OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_muerto.u*1.4),3)} [mm]")
# ret_D_muerto_desplazamientos_max=sorted(ret_D_muerto.desplazamientos_verticales, key=itemgetter(1))[0]
# plt.title(f'Desplazamiento maximo en el nodo {ret_D_muerto_desplazamientos_max[0]}: {round(ret_D_muerto_desplazamientos_max[1]*1000,3)}[mm] ')
plt.show()

peso = ret_D_muerto.calcular_peso_total()
print(f"peso optimizado 1.4 D = {peso}")

ver_reticulado_3d(ret_D_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_muerto.u*1.4,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 3: 1.4 D OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_muerto.u*1.4),3)} [mm]")
plt.show()

#                            CASO DE COMBINACION DE CARGA 2 OPTIMIZADA (1.2*D + 1.6*L)
barras_vivo_muerto= ret_D_vivo_muerto.obtener_barras()
barras_vivas=ret_L.obtener_barras()
for i in barras_a_rediseñar:
    barras_vivo_muerto[i].rediseñar(f_4_D_vivo_muerto[i],ret_D_vivo_muerto)
    barras_vivas[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)
        

ret_D_vivo_muerto.ensamblar_sistema()
ret_D_vivo_muerto.resolver_sistema()        

ret_L.ensamblar_sistema()
ret_L.resolver_sistema()

f_L = ret_L.recuperar_fuerzas()

FU_caso_vivo_muerto = ret_D_vivo_muerto.recuperar_factores_de_utilizacion(f_4_D_vivo_muerto)
f_D_vivo_muerto = ret_D_vivo_muerto.recuperar_fuerzas()
f_4_D_vivo_muerto = 1.2*f_D_vivo_muerto + 1.6*f_L  




ver_reticulado_3d(ret_D_vivo_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_vivo_muerto.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_4_D_vivo_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 4: 1.2 D + 1.6 L  OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_vivo_muerto.u*1.2+ret_L.u*1.6),3)} [mm]")
plt.show()

peso = ret_D_vivo_muerto.calcular_peso_total()
print(f"peso optimizado 1.2 D + 1.6 L = {peso}")

ver_reticulado_3d(ret_D_vivo_muerto, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_vivo_muerto.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_vivo_muerto,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 4: 1.2 D + 1.6 L OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_vivo_muerto.u*1.2+ret_L.u*1.6),3)} [mm]")
plt.show()




#                            CASO DE 5 BARRAS PARA COMBINACION DE CARGA 2 OPTIMIZADA (1.2*D + 1.6*L)

barras_a_rediseñar = [8,9,12,14,15]

barras_5_barras= ret_D_5_barras.obtener_barras()
barras_vivas=ret_L.obtener_barras()
for i in barras_a_rediseñar:
    barras_5_barras[i].rediseñar(f_5_D_5_barras[i],ret_D_5_barras)
    barras_vivas[i].rediseñar(f_3_D_muerto[i],ret_D_muerto)

ret_D_5_barras.ensamblar_sistema()
ret_D_5_barras.resolver_sistema()        

ret_L.ensamblar_sistema()
ret_L.resolver_sistema()

f_L = ret_L.recuperar_fuerzas()
        
FU_caso_5_barras = ret_D_5_barras.recuperar_factores_de_utilizacion(f_5_D_5_barras)
f_D_5_barras = ret_D_5_barras.recuperar_fuerzas()
f_5_D_5_barras = 1.2*f_D_5_barras + 1.6*f_L 




ver_reticulado_3d(ret_D_5_barras, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_5_barras.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_5_D_5_barras,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("Tensiones en caso 5 BARRAS: 1.2 D + 1.6 L  OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_5_barras.u*1.2+ret_L.u*1.6),3)} [mm]")
plt.show()

peso = ret_D_5_barras.calcular_peso_total()
print(f"peso optimizado 5 barras = {peso}")

ver_reticulado_3d(ret_D_5_barras, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": factor_a,
        "datos_desplazamientos_nodales":ret_D_5_barras.u*1.2 + ret_L.u*1.6,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso_5_barras,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.suptitle("FU caso 5 BARRAS: 1.2 D + 1.6 L OPTIMIZADO")
plt.title(f"El desplazamiento máximo es: {round(1000*min(ret_D_5_barras.u*1.2+ret_L.u*1.6),3)} [mm]")
plt.show()