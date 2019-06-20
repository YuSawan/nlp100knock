import argparse
import knock_20
import knock_25

def main(info):
	infobox = dict([(key,value.replace("'''''","").replace("'''","")) for key,value in info.items()])
	print ("\n".join([key+": "+infobox[key] for key in infobox.keys()]))

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument('-t','--test',dest='train',default='../../data/knock/jawiki-country.json',help='input training data')
	parser.add_argument('-c','--country',dest='country',default='イギリス',help='input training data')
	args = parser.parse_args()
	uk = knock_20.get_text(args.train,args.country)
	info = knock_25.get_info(uk)
	main(info)
