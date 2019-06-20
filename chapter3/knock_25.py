import argparse
import knock_20

def get_info(my_country):
	item = my_country.strip().split('\n}}\n')[0].split('\n')
	info = [row.strip() for row in item if row.startswith('|')]
	return dict([tuple(line.split("<ref>")[0].replace("|","").split(" = ")) for line in info])

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument('-t','--test',dest='train',default='../../data/knock/jawiki-country.json',help='input training data')
	parser.add_argument('-c','--country',dest='country',default='イギリス',help='input training data')
	args = parser.parse_args()
	uk = knock_20.get_text(args.train,args.country)
	info = get_info(uk)
	print("\n".join([k+": "+info[k] for k in info.keys()]))
