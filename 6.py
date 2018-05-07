def chkDupNum(s):
    result = [ ]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10


number1 = input("숫자을 입력하세요: ")
number2 = input("숫자을 입력하세요: ")
number3 = input("숫자을 입력하세요: ")
number4 = input("숫자을 입력하세요: ")
number5 = input("숫자을 입력하세요: ")


print(chkDupNum(number1))
print(chkDupNum(number2))
print(chkDupNum(number3))
print(chkDupNum(number4))
print(chkDupNum(number5))

