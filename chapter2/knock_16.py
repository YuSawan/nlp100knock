import argparse
import sys

arg = sys.argv

def main(my_text,N):
	rows = open(my_text)
	for cnt,s in enumerate(list(rows)):
		if cnt%(N+1)==0:
			print ('\n----------\n')
		else:
			print(s)
			cnt += 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-t','--train',dest='train',default=    '../data/hightemp.txt', help='input training data')
	args = parser.parse_args(args=[])
	main(args.train,int(arg[1]))
