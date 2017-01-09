#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com

import sys
import math

numberOfProblem = int(input().strip())

for problem in range(numberOfProblem):
	theNumber = int(input().strip())
	gotPrime = False
	dividedNumber = theNumber
	

	#there is no more than 1 prime factor that is bigger than sqrt(theNumber)
	#So, we don't have to search all numbers from 1 to theNumber
	for divider in range(2, int(math.sqrt(theNumber)) + 1):
		while theNumber % divider == 0:
			theNumber //= divider
			#case 1 : we found biggest number in sqrt(number) by finishing prime factorization
			if (theNumber == 1) :
				print (x)
				gotPrime = True
	#case 2 : we didn't find biggest number in sqrt(number)
	if (gotPrime == False) :
		print(theNumber)
