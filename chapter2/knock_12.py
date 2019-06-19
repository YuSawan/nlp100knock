import argparse

def main(my_text):
	file1 = 'col1.txt'
	file2 = 'col2.txt'
	rows = open(my_text)
	for s in rows:
		row = s.split('	')
		file1.write(row[0]+'\n')
		file2.write(row[1])+'\n')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t','--train',dest='train',default='../data/hightemp.txt',help='input training data')

	args = parser.parse_args(args=[])
	
	main(args.train)
