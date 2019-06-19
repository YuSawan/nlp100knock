def main(my_text1,my_text2):
	rows1 = open(my_text1)
	rows2 = open(my_text2)
	pref = [_.rstrip('\n') for _ in rows1]
	city = [_.rstrip('\n') for _ in rows2]
	for i in range(len(pref)):
		print (pref[i],city[i])

if __name__ == '__main__':
	main('col1.txt','col2.txt')
