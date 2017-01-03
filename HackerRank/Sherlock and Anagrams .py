#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com

numberOfProblems = input()
numberOfString = int(numberOfProblems)
x = 0

while (x < numberOfString) :

	#totalAna : number of Anagrams in the string
	#theString : the string we will research
	totalAna = 0
	theString = input()

	for subLength in range(1, len(theString)):
		#Use memoization, calculate all possible substrings
		#for each sublengths.(from 1 to len(theString) )
		subLengthLists = []

		for cha1stIndex in range(len(theString)-subLength+1) :
			suspectString = theString[cha1stIndex:cha1stIndex+subLength]
			suspectStringList = list(suspectString)
			#Sort the characters in the substring
			suspectStringList.sort()
			subLengthLists.append(suspectStringList)
		
		#Sort the substrings in the substring list
		subLengthLists.sort()

		#print(subLengthLists)

		startIndex = 0
		count = 0
		
		#count the same substrings from the index 0
		for index in range(len(subLengthLists)):
			#print(subLengthLists[startIndex])
			#print(subLengthLists[index])
			if subLengthLists[startIndex] == subLengthLists[index] :
				count += 1
			else :
				startIndex = index
				if count > 1 :
					totalAna += (count*(count-1))/2
				count = 1
		if count >1 :
			totalAna += (count*(count-1))/2
		#print(int(totalAna))	

	print(int(totalAna))
	x += 1
