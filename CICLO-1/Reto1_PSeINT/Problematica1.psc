Algoritmo Problematica1
	Escribir "Este programa calcula el valor presupuestal para UNAB según sus rubros y los ajsuta para el siguiente año según el aumento"
	Escribir "Los rubros están clasificados de la siguiente manera:"
	Escribir "Investigación     | 20%"
	Escribir "Gastos Operación  | 40%"
	Escribir "Tecnología        | 20%"
	Escribir "Extensión         | 20%"
	Escribir "Ingrese el valor de inversión"
	Leer inversion
	P_investigacion = inversion*0.2
	P_gastosOperacion = inversion*0.4
	P_tecnologia = inversion*0.2
	P_extension = inversion*0.2
	Escribir "El valor de inversion de investigación es de: ", P_investigacion
	Escribir "El valor de inversion de Gastos Operación es de: ", P_gastosOperacion
	Escribir "El valor de inversion de Tecnología es de: ", P_tecnologia
	Escribir "El valor de inversion de Extensión es de: ", P_extension
	Escribir "Ingrese el porcentaje de aumento para el siguiente año (Para digitar decimales use el punto . )"
	Leer aumento
	P_aumento=(aumento+100)/100
	Incremento_investigacion = P_investigacion*P_aumento
	Incremento_gastosOperation = P_gastosOperacion*P_aumento
	Incremento_tectonologia = P_tecnologia*P_aumento
	Incremento_extension = P_extension*P_aumento
	Escribir "El valor con aumento de: ", aumento, "% para inversión es: "
	Escribir "Investigación     | 20% |", Incremento_investigacion, " |"
	Escribir "Gastos Operación  | 40% |", Incremento_gastosOperation, " |"
	Escribir "Tecnología        | 20% |", Incremento_tectonologia, " |"
	Escribir "Extensión         | 20% |", Incremento_extension, " |"
FinAlgoritmo
