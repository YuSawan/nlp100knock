import argparse
import sys

arg = sys.argv

def main(my_text,N):
	rows = open(my_text)
	count = 0
	for s in reversed(list(rows)):
		if count == int(N):
			break
		else:
			print(s)
		count += 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default=    '../data/hightemp.txt', help='input training data')
	args = parser.parse_args(args=[])
	main(args.train,arg[1])
