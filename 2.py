sum1 = 0
sum2 = 0

for i in range(1, 100+1):
    sum1 += i
    sum2 += i**2  # 제곱의 합

sum1 = sum1 ** 2  # 합의 제곱

print(sum1 - sum2)