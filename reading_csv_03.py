#reading_csv_03.py
import csv
with open('books.csv', newline='') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list=[]
  for books in books_reader:
    isbn_list.append(books['ISBN'])

print(isbn_list)