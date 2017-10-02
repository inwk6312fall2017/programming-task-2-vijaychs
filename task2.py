import csv
with open("Crime.csv",'r') as my_file:
	reader = csv.reader(my_file)
# my_list = list(reader)
#print(my_list)
crime_type=[]
crime_id=[]
crime_count=[]
	for crime in my_file:
		if crime == "ASSAULT":
			print("s")
		else:
			print("f")
