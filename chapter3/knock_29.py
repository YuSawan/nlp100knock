import argparse
import knock_20
import knock_25
import re
import json
import requests

def main(info):
	infobox = dict([(key,value.replace("'''''","").replace("'''","")) for key,value in info.items()])
	infobox = dict([(key,re.sub(r"\[\[.*\]\]", lambda x:x.group().replace("[[","").replace("]]","").split("|")[0].split("#")[0],value)) for key, value in infobox.items()])
	infobox = dict([(key,re.sub(r"{{.*}}", lambda x: x.group().replace("{{","").replace("}}",""),value)) for key,value in infobox.items()])
	infobox = dict([(key,re.sub(r"<.*>","",value)) for key,value in infobox.items()])
	url = "http://ja.wikipedia.org/w/api.php?format=json&action=query&titles=Image:%s&prop=imageinfo&iiprop=url" % infobox["国旗画像"]
	response = requests.get(url).json()
	print (response['query']['pages']['-1']["imageinfo"][0]["url"])

if __name__ == '__main__':
	parser =  argparse.ArgumentParser()
	parser.add_argument('-t','--test',dest='train',default='../../data/knock/jawiki-country.json',help='input training data')
	parser.add_argument('-c','--country',dest='country',default='イギリス',help='input training data')
	args = parser.parse_args()
	uk = knock_20.get_text(args.train,args.country)
	info = knock_25.get_info(uk)
	main(info)
