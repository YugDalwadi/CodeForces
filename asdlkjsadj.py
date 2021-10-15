testCases = int(input())

# B is common in both of the sets AB and BC, so we can check if no. of B's is equal to half the length
# of the string and remainder of length of string is 0 when divided by 2.
# We have to check remainder as integer division rounds up or rounds down the number.
for i in range(testCases):
    string = list(input())
    bCount = string.count("B")

    if(bCount == len(string)//2 and len(string)%2 == 0):
        print("YES")

    else:
        print("NO")    

