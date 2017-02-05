#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com


import sys
from heapq import heappush, heappop
import time



probleminimumfo = input().strip()
N, E = probleminimumfo.split(" ")
N = int(N)
E = int(E)

#There is 3 Sets :
#'startSet set' : the nodes which are connected to the node 0
#'endSet set' : the node which are connected to the node N
#'middleSet set' : nodes which are connected to neither the node 0 nor the node N


#When we found the edge which is connected to the 
#'startSet set' or 'endSet set', 
#we attach the nodes in 'middleSet set' to the set as many as possible

def calculmiddleSet(addedNodeNumber, setToBeUpdated, middleSet):
	
	queue = []

	
	rest = list(middleSet[addedNodeNumber]-startSet)
	setToBeUpdated.update(middleSet[addedNodeNumber])
	
	queue += rest
	
	while queue != [] :
		rest = list(middleSet[queue[0]]-setToBeUpdated)
		setToBeUpdated.update(middleSet[queue[0]])
		queue += rest
		del queue[0]
		


def isThereRoute(startSet, endSet, middleSet, new) :
	#when one node of the edge is in startSet and other side of the edge is in endSet,
	#return True.  
	if new[1] in startSet and new[2] in endSet :
		return True
	elif new[2] in startSet and new[1] in endSet :
		return True
	#decide whether the node is connected to startSet, endSet, or middleSet.	
	if new[1] in startSet :
		startSet.add(new[2])
		if new[2] in middleSet :
			#startSet.update(middleSet[new[2]])
			calculmiddleSet(new[2], startSet, middleSet)
	elif new[2] in startSet :
		startSet.add(new[1])
		if new[1] in middleSet :
			#startSet.update(middleSet[new[1]])
			calculmiddleSet(new[1], startSet, middleSet)
	elif new[1] in endSet :
		endSet.add(new[2])
		if new[2] in middleSet :
			#endSet.update(middleSet[new[2]])
			calculmiddleSet(new[2], endSet, middleSet)
	elif new[2] in endSet :
		endSet.add(new[1])
		if new[1] in middleSet :
			#endSet.update(middleSet[new[1]])
			calculmiddleSet(new[1], endSet, middleSet)
	else :
		if new[1] in middleSet :
			middleSet[new[1]].add(new[2])
		else : 
			middleSet[new[1]] = set([new[2]])
		if new[2] in middleSet :
			middleSet[new[2]].add(new[1])
		else : 
			middleSet[new[2]] = set([new[1]])

	return False

#print(time.time())

costs = []

#sort the edges according to the costs
for x in range(E) :
	A, B, fee = input().strip().split(" ")
	A = int(A)
	B = int(B)
	fee = int(fee)
	heappush(costs, (fee, A-1, B-1 ))
#print(time.time())

efficient = 10000001


#print(time.time())
startSet = set([0])
endSet = set([N-1])
middleSet = {}

while costs != [] : 
	x = heappop(costs)
	if(isThereRoute(startSet, endSet, middleSet, x)):
		efficient = x[0]
		break

#print(time.time())

if efficient == 10000001:
	print("NO PATH EXISTS")
else : 
	print(efficient)