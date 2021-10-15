no_soldiers = int(input())
soldier_sequence = list(map(int, input().split()))

yeah=0
yeah2 = 0
a= max(soldier_sequence)
b = min(soldier_sequence)
turns= 0
x= 0

while(soldier_sequence[0]!=a):
    x=x+1
    soldier_sequence[0], soldier_sequence[x] = soldier_sequence[x], soldier_sequence[0]
    turns = turns+1
    print(soldier_sequence)

 
while(soldier_sequence[-1]!=b):
    x=x+1
    soldier_sequence[-1], soldier_sequence[-x-1] = soldier_sequence[-x-1], soldier_sequence[-1]
    turns = turns+1 
    
    print(soldier_sequence)

print(turns)


        

