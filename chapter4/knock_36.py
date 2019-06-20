import argparse
import knock_30
import collections

def main(my_morph):
	words = list()
	for line in my_morph:
		for morph in line:
			words.append(morph['base'])
	word_cnt = collections.Counter(words)
	for k,v in sorted(word_cnt.items(), key=lambda x:-x[1]):
		print(str(k)+": "+str(v))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default='../../data/knock/neko.mecab',help='input training data')
	args = parser.parse_args()
	my_morph = knock_30.get_morph(args.train)
	main(my_morph)
