#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com



import sys


numberOfProblems= int(input().strip())
for eachProblem in range(numberOfProblems):
	problem = int(input().strip())
	numberBeforeBefore = 0
	numberBefore = 1
	nthNumb = 0
	totalSum = 0
	while (numberBeforeBefore + numberBefore  <= problem):
		nthNumb =numberBeforeBefore + numberBefore
		numberBeforeBefore = numberBefore
		numberBefore = nthNumb

		if nthNumb %2 == 0 :
			totalSum += nthNumb
	print(totalSum)

