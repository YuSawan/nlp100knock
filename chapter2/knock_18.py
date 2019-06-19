import argparse

def main(my_text):
	rows = open(my_text)
	s = []
	for row in list(rows):
		s.append(row.rstrip('\n').split('	'))
	s.sort(key=lambda x:float(x[2]))
	for i in s:
		print(' '.join(i))
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t','--train',dest='train',default='../data/hightemp.txt',help='input training data')

	args = parser.parse_args(args=[])
	
	main(args.train)
