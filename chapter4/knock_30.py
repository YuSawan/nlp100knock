import argparse

#mecab neko.txt -o neko.txt.mecab
def get_morph(my_file):
	doc = list()
	sent = list()
	for line in open(my_file):
		if line.startswith('EOS') or line=="":
			doc.append(sent)
			sent = list()
			continue
		surface,items = line.split("\t")
		item_list = items.split(",")
		morph = {
			'surface': surface,
			'base': item_list[6],
			'pos': item_list[0],
			'pos1': item_list[1]
		}
		sent.append(morph)
		#print(morph['surface'],morph['base'],morph['pos'],morph['pos1'])
	return doc

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default='../../data/knock/neko.mecab',help='input training data')
	args = parser.parse_args()
	my_morph = get_morph(args.train)
