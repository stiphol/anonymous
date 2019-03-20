import csv


# Make a dictionary of anonymous IP {ip: other values from row}
database_set = dict()
with open('GeoIP2-Anonymous-IP-Blocks-IPv4.csv', 'r') as db:
	db.readline()
	database = csv.reader(db, delimiter = ',')
	for row in database:
		row = ['0' if x == '' else x for x in row] # fill empty row with 0
		result = row[0]
		x = result[:-3].strip("\n")
		database_set[x] = (row[0],row[1],row[2],row[3],row[4],row[5])

# Result file with column names.
out = open('result_2.csv','w')
result = csv.writer(out, delimiter = ',')
result.writerow((
	'exchange', 
	'remote_ip', 
	'imps', 
	'clicks', 
	'convs', 
	'CTR', 
	'CR', 
	'spend', 
	'eCPM', 
	'eCPC', 
	'CPI',
	'network',  
	'is_anonymous',  
	'is_anonymous_vpn',  
	'is_hosting_provider',
	'is_public_proxy',  
	'is_tor_exit_node'
	))

# Line by line reading IP-addresses. 
# If the IP-address is in the dictionary - make an entry in the file with all columns.
with open('imp.csv', 'r') as db:
	db.readline()
	database = csv.reader(db, delimiter = ',')
	for row in database:
		if row[1] in database_set:
			result.writerow((
				row[0],
				row[1],
				row[2],
				row[3],
				row[4],
				row[5],
				row[6],
				row[7],
				row[8],
				row[9],
				row[10],
				database_set[row[1]][0],
				database_set[row[1]][1],
				database_set[row[1]][2],
				database_set[row[1]][3],
				database_set[row[1]][4],
				database_set[row[1]][5]
				))
out.close()
