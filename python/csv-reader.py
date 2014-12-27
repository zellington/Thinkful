import csv

def csv_reader(file_obj):

	reader = csv.reader(file_obj)
	for row in reader:
		print(" ".join(row))

if __name__ == "__main__":
	csv_path = "WHO_data.csv"
	with open(csv_path, "rb") as f_obj:
		csv_reader(f_obj)
		 