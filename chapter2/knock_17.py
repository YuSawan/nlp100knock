import argparse

def main(my_text):
	rows = open(my_text)
	vocab = set()
	for s in rows:
		row = s.split('	')
		vocab.add(row[0])
	print(vocab)
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t','--train',dest='train',default='../data/hightemp.txt',help='input training data')

	args = parser.parse_args(args=[])
	
	main(args.train)
