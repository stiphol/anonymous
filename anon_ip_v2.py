import pandas as pd 
import re
import sys


counter = n = 0
ip_list = []

CONST = int(sys.argv[1]) #number of strings


#Adding IP-column without a subnetwork
df = pd.read_csv('GeoIP2-Anonymous-IP-Blocks-IPv4.csv')
df['ip'] = df['network']
for i in df['ip']:
	ip = re.search(r'^[0-9.]+', i.split(",")[0])
	df.at[counter, 'ip'] = ip.group(0)
	counter+=1


#Creating a list of found anonymous IP-addresses
with open('imp.csv', "r") as f_obj: 
	f_obj.readline()
	for ip in f_obj:
		result = ip.split(",")[1]
		current_ip = result[1:-1].strip("\n")
		if n<CONST:
			try:
				df[df['ip']==current_ip].index[0]
				ip_list.append(current_ip)
				n+=1
			except IndexError: 
				continue
		else:
			break

df = df.loc[df['ip'].isin(ip_list)]
del df['ip']
df.to_csv('result.csv')
