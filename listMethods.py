numbers = [4, 1, 2, 5, 8, 3]

numbers.insert(3, 412) # index, value

print(numbers)

numbers.remove(4) # remove item called 4

print(numbers)

print(412 in numbers) # returns boolean (True, in this case)

numbers.clear() # removes all items

print(numbers)

#remove duplicates

moreNumbers = [1, 1, 4, 3, 5, 4, 7]

numList = []

for number in moreNumbers:
    if number not in numList:
        numList.append(number)

print(numList)