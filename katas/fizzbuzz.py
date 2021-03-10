def main():
	n,m=map(int,input().split())

	for i in range(n,m+1):
		if i%3==0 and i%5!=0:
			print("Fizz")
		elif i%5==0 and i%3!=0:
			print("Buzz")
		elif i%3==0 and i%5==0:
			print("FizzBuzz")
		elif i%3!=0 and i%5!=0:
			print(i)

if __name__=='__main__':
	main()
