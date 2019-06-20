import argparse
import knock_20
import re

category = re.compile('\[\[Category\:(((?P<cat1>.*)\|+.*)|(?P<cat2>.*))\]\]')

def main(my_country):
	item = my_country.strip().split('\n')
	for row in item:
		result = category.search(row)
		if result is not None:
			print(result.group('cat1') if result.group('cat2') is None else result.group('cat2'))

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument('-t','--test',dest='train',default='../../data/knock/jawiki-country.json',help='input training data')
	parser.add_argument('-c','--country',dest='country',default='イギリス',help='input training data')
	args = parser.parse_args()
	uk = knock_20.get_text(args.train,args.country)

	main(uk)
