# MCOC2020 - Proyecto 2
# ==========================================================
# ver_reticulado_2d
#
# Funciones sencillas para visualizar reticulados en 2d. 
#
# 2020 - www.joseabell.com 
# Facultad de Ingeniería y Ciencias Aplicadas
# Universidad de los Andes
# ==========================================================

import matplotlib.pyplot as plt

def ver_reticulado_2d(ret, fig=0, 
	#Opciones para nodos
	ver_nodos=True,
	marcador_nodos="o", 
	ver_numeros_de_nodos=True,
	color_nodos="k",
	color_borde_nodos=[0.7,0.7,0.7],
	#Opciones para barras
	ver_barras=True,
	estilo_barras="-",
	color_barras=[138/255,89/255,0/255],#8F652F
	grosor_barras=2,
	ver_numeros_de_barras=True,
	llamar_show=True,
	#Otras opciones
	ver_grilla=True,
	
	):

	xy = ret.obtener_nodos()

	if fig == 0:
		fig = 1
		llamar_show = True
	elif llamar_show:
		llamar_show = False
	
	plt.figure(fig)

	# Nodos

	plt.plot(xy[:,0], xy[:,1], 
		marker=marcador_nodos,
		markerfacecolor=color_nodos,
		markeredgecolor=color_borde_nodos,
		linestyle="",
		)

	if ver_numeros_de_nodos:
		for n in range(xy.shape[0]):
			plt.text(xy[n,0], xy[n,1], f"{n}", color=color_nodos)

	# Barras

	if ver_barras:
		x = []
		y = []
		for i,b in enumerate(ret.obtener_barras()):
			nodos = b.obtener_conectividad()
			x =  xy[nodos,0]
			y =  xy[nodos,1]
			plt.plot(x,y,
				linestyle=estilo_barras,
				color=color_barras,
				linewidth=grosor_barras,
				)
			if ver_numeros_de_barras:
				x0 = x.mean()
				y0 = y.mean()
				plt.text(x0, y0, f"{i}", color=color_barras)

	
	plt.grid(ver_grilla)

	if llamar_show:
		plt.show()