#reading_csv_02.py
import csv
with open('cool_csv.csv',newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for dict in cool_csv_dict:
    print(dict)