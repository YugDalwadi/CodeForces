totalCoins= int(input())
coinValues = list(map(int, input().split()))
coinValues.sort(reverse=True)
print(coinValues)
Value= sum(coinValues) 
coins = 0
sum = 0

for i in coinValues:
    sum = sum+i
    Value = Value-i
    coins+= 1

    if(sum>Value):
        break

print(coins)
