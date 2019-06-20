import argparse
import knock_30

def main(my_morph):
	for line in my_morph:
		for morph in line:
			if morph['pos']=='動詞':
				print (morph['base'])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default='../../data/knock/neko.mecab',help='input training data')
	args = parser.parse_args()
	my_morph = knock_30.get_morph(args.train)
	main(my_morph)
