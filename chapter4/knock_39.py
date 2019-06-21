import argparse
import knock_30
from collections import Counter
import matplotlib.pyplot as plt

def main(my_morph):
	words = list()
	for line in my_morph:
		for morph in line:
			words.append(morph['base'])
	names,cnts = zip(*Counter(words).most_common())

	plt.bar(range1(1,len(names)+1),cnts)
	plt.xscale('log')
	plt.yscale('log')
	plt.show()

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default='../../data/knock/neko.mecab',help='input training data')
	args = parser.parse_args()
	my_morph = knock_30.get_morph(args.train)
	main(my_morph)
