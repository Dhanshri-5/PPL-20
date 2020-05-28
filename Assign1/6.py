#question 6
#pair of amicable numbers

def SumDivisors(number):
	sum = 1
	for i in range(2,number):
		if number % i == 0 :
			sum += i
	return sum

list_=[]
if __name__ == "__main__":
	count = 0
	for i in range(1,75000):
		if i in list_:
			continue
		sum = SumDivisors(i)
		if SumDivisors(sum) == i and i < sum:
			list_.append(sum)
			print("{0:<4} and {1:<4}".format(i,sum))
			count += 1
		if count == 10:
			break
  	                    
