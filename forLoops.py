for item in "Python":
    print(item)

for index in [4, 1, 2]:
    print(index)

for num in range(1, 100, 2):  # for one num, 0-num; for 2 nums, num1-num2; for 3 nums, num1-num2, by num3
    print(num)

prices = [10, 20, 30]
total_price = 0

for price in prices:
    total_price += price

print(f"Total: {total_price}")
