testCases = int(input())

for i in range(testCases):
    parts = int(input())
    myList = list(map(int,input().split()))
    middleTerm = parts//2+1

    if(parts%2!=0 and myList[0]==myList[parts-1] and myList[parts//2]== middleTerm):
        print("yes")
 
    else:
        print("no")    




            

