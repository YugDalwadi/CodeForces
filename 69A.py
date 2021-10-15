# Young Physicist
# Warning- The axes are written in order. So, the first line has the x1, y1, z1 axes and the second line
# has the x2,y2,z2 axes and so on.
lines = int(input())

a,b,c = 0,0,0

for i in range(lines):
    
    coordinates = list(map(int, input().split()))

    # Adding values to each element to see if the final result is 0.
    a= a+coordinates[0]
    b= b+coordinates[0]
    c= c+coordinates[0]     

if(a==b==c==0):
    print("YES")
else:
    print("NO")           

