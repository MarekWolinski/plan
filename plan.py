import csv


def is_part_to_replace(row):
	if (row[4] != '') & (row[44] == 'SCRAP'):
		return row
	elif (row[4] != '') & (row[44] == 'OVERHAUL'):
		return row
	elif row[3].find('OVERHAUL') != -1:
		return row
	elif row[3].find('REPLACE') != -1:
		return row
	elif row[3].find('FUEL MANIFOLD ADAPTER AND NOZZLE ASSEMBLIES') != -1:
		return row
	elif row[3].find('FIRST AID KIT') != -1:
		return None


def main():
	source_file_name = 'DUE MXH.csv'
	save_file_name = 'parts.csv'
	read_file = open(source_file_name, 'r')
	reader = csv.reader(read_file, delimiter = ';', skipinitialspace = True)
	save_file = open(save_file_name, 'w')
	writer = csv.writer(save_file, delimiter = ';', skipinitialspace = True)
	for row in reader:
		part = is_part_to_replace(row)
		if part != None:
			writer.writerow(part)
	read_file.close()
	save_file.close()


main()
