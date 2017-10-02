import csv
with open("Crime.csv",'r') as my_file:
 reader = csv.reader(my_file)
 my_list = list(reader)
print(my_list)
