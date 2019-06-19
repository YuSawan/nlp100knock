import argparse
import collections

def main(my_text):
	rows = open(my_text)
	s = []
	for row in list(rows):
		s.append(row.rstrip('\n').split('	')[0])
	for k,v in sorted(collections.Counter(s).items(),key=lambda x:-x[1]):
		print(k,v)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t','--train',dest='train',default='../data/hightemp.txt',help='input training data')

	args = parser.parse_args(args=[])
	
	main(args.train)
