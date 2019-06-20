import json
import argparse
import io

def get_text(my_file,country):
	for line in open(my_file):
		wiki = json.load(io.StringIO(line))
		#print json.dumps(wiki, sort_keys=True,indent=4,ensure_ascii=False)
		if wiki['title'] == country:
			return wiki['text']

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument('-t','--test',dest='train',default='../../data/knock/jawiki-country.json',help='input training data')
	parser.add_argument('-c','--country',dest='country',default='イギリス',help='input training data')
	args = parser.parse_args()
	print (get_text(args.train,args.country))
