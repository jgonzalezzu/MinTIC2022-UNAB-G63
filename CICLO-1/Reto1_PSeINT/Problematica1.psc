Algoritmo Problematica1
	Escribir "Este programa calcula el valor presupuestal para UNAB seg�n sus rubros y los ajsuta para el siguiente a�o seg�n el aumento"
	Escribir "Los rubros est�n clasificados de la siguiente manera:"
	Escribir "Investigaci�n     | 20%"
	Escribir "Gastos Operaci�n  | 40%"
	Escribir "Tecnolog�a        | 20%"
	Escribir "Extensi�n         | 20%"
	Escribir "Ingrese el valor de inversi�n"
	Leer inversion
	P_investigacion = inversion*0.2
	P_gastosOperacion = inversion*0.4
	P_tecnologia = inversion*0.2
	P_extension = inversion*0.2
	Escribir "El valor de inversion de investigaci�n es de: ", P_investigacion
	Escribir "El valor de inversion de Gastos Operaci�n es de: ", P_gastosOperacion
	Escribir "El valor de inversion de Tecnolog�a es de: ", P_tecnologia
	Escribir "El valor de inversion de Extensi�n es de: ", P_extension
	Escribir "Ingrese el porcentaje de aumento para el siguiente a�o (Para digitar decimales use el punto . )"
	Leer aumento
	P_aumento=(aumento+100)/100
	Incremento_investigacion = P_investigacion*P_aumento
	Incremento_gastosOperation = P_gastosOperacion*P_aumento
	Incremento_tectonologia = P_tecnologia*P_aumento
	Incremento_extension = P_extension*P_aumento
	Escribir "El valor con aumento de: ", aumento, "% para inversi�n es: "
	Escribir "Investigaci�n     | 20% |", Incremento_investigacion, " |"
	Escribir "Gastos Operaci�n  | 40% |", Incremento_gastosOperation, " |"
	Escribir "Tecnolog�a        | 20% |", Incremento_tectonologia, " |"
	Escribir "Extensi�n         | 20% |", Incremento_extension, " |"
FinAlgoritmo
