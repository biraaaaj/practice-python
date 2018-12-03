#!/usr/bin/env python3
import csv
csv_file=open('darkhumor.csv')
csv_reader=csv.csv_reader(csv_file)
print(csv_reader)
csv_file.close()