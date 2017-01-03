#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com

import sys

trip = int(input().strip())
#read problems as many as skeleton trips

for eachTrip in range(trip):
	#read lines
	n = input().strip()
	
	#parameters of the problem
	parameters = n.split()
	
	#numberOfSticksToBuy = n in problem
	#sales = k in problem
	#numberOfBoxesToBuy = b in problem
	numberOfSticksToBuy = int(parameters[0])
	sales = int(parameters[1])
	numberOfBoxesToBuy = int(parameters[2])

	#Lists that contains box numbers
	#ans string for answer output
	answerList = []
	answerString = ""	
	
	#stickLimit = the number of sticks in the most biggest boxes
	#for example, if k = 10 and b = 3 , stickLimit is 10+9+8 = 27
	stickLimit = int((sales*(sales+1)//2) - ((sales - numberOfBoxesToBuy)*(sales - numberOfBoxesToBuy +1) //2))
	
	#case 1 : if numberOfSticksToBuy is smaller than the smallest boxes,
	#it can not be solved
	#for example, if you want 3 boxes, you must requ
	if numberOfSticksToBuy < ((numberOfBoxesToBuy+1)*numberOfBoxesToBuy)//2:
		#print("case1")
		print(-1)

	#case 2 : if numberOfSticksToBuy is bigger than the sum of biggest boxes,
	#It can not be solved.
	elif numberOfSticksToBuy > stickLimit:
		#print("case2")
		print(-1)


	#case 3 : if numberOfSticksToBuy is equal to the sum of smallest boxes,
	#answer is just the list of them.
	elif numberOfSticksToBuy == ((numberOfBoxesToBuy+1)*numberOfBoxesToBuy//2) :
		#print("case 3")
		for x in range(1, numberOfBoxesToBuy+1):
			answerString += str(x) + " "
		print (answerString[:-1])

	
	#default case : from [1, 2, ... , theNumberOfBoxes],
	#increase the number of each number as equally as we can
	#and print the list
	else :
		increment = int(((numberOfSticksToBuy-((numberOfBoxesToBuy+1)*numberOfBoxesToBuy//2))//numberOfBoxesToBuy))
		moduloParameter = int((numberOfSticksToBuy-(numberOfBoxesToBuy+1)*numberOfBoxesToBuy//2) % numberOfBoxesToBuy)
		for x in range(1, numberOfBoxesToBuy + 1):
			answerList.append(x+increment)
		
		#the residues are added from the last element of the answerLists.
		for x in range(1, moduloParameter+1):
			answerList[-x] += 1
		
		for x in answerList:
			answerString += str(x) + " "
		print(answerString[:-1])