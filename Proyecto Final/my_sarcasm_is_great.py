#!/usr/bin/env python

import csv
with open('data.csv', 'r') as my_file:
	my_csv = csv.reader(my_file)
	for row in my_csv:
		print(row)