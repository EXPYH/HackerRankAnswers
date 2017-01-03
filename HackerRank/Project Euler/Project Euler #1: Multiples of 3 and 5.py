#Written by EXPYH(or DublinerYH)
#dublineryh@gmail.com
#YounghwanShin.com


import sys


numberOfProblems = int(input().strip())
for eachProblem in range(numberOfProblems):
    problem = int(input().strip())
    
    #We need to find numbers BELOW the problem 
    problem -= 1

    div3 = n // 3
    div5 = n // 5
    div15 = n // 15

    sum3 = ((div3 * (div3+1))// 2) * 3
    sum5 = ((div5 * (div5+1)) // 2) * 5

    #Substract joint sets of each sums
    sum15 = (div15 * (div15+1) // 2) *15
    totalSum = sum3 + sum5 - sum15
    print(totalSum)
