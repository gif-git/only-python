import csv
def csv_reader(file_obj):
  reader = csv.reader(file_obj)
  for row in reader:
    print(" | ".join(row))
#path = "/home/subashini/Documents/PythonLearning/"
path = "/home/gif/git/only-python/exp/"
file = open(path + 'data2023.csv')
csv_reader(file)
