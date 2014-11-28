#!/usr/bin/env python

import csv
with open('data.csv', 'r') as my_file:
	my_csv = csv.reader(my_file)

	# En el data set el target esta en la columna 2 y el resto
	# de los atributos en las columnas > 2
	target = []
	data = []

	# Saltamos el header
	next(my_csv)

	# Llenamos las tuplas de target (Valores esperados)
	# y las de data (Valores que tenemos)
	for row in my_csv:
		target.append(row[1])
		data.append(row[2:])

	# Transformamos la entrada a enteros

	for i in range(len(target)):
		target[i] = int(target[i])
		for j in range(len(data[i])):
			data[i][j] = int(data[i][j])