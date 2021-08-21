numbers = [4, 5, 12, 6, 20, 1, 6]

bigNum = numbers[0]

for number in numbers:
    if number > bigNum:
        bigNum = number

print(bigNum)