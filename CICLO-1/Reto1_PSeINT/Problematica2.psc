Algoritmo Problematica2
	Escribir "Este programa genera medias en metros y el costo de importación"
	Escribir "Ingrese las pulgadas del material para el pedido"
	Leer pulgadas
	metros = (pulgadas*2.54)/100
	v_pedido = metros*1280
	v_imp = v_pedido*1.25
	Escribir "La cantidad de material en metros es: ", metros, " [m]"
	Escribir "El costo del pedido es: $", v_pedido, " pesos"
	Escribir "El costo del pedido con importación del 25% es: $", v_imp, " pesos"
FinAlgoritmo