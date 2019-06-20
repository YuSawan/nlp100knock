import argparse
import knock_30

def main(my_morph):
	for line in my_morph:
		for i in range(1,len(line)-1):
			if line[i-1]['pos']=='名詞' and line[i]['surface'] == 'の' and line[i+1]['pos']=='名詞':
				print (line[i-1]['surface']+line[i]['surface']+line[i+1]['surface'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default='../../data/knock/neko.mecab',help='input training data')
	args = parser.parse_args()
	my_morph = knock_30.get_morph(args.train)
	main(my_morph)
