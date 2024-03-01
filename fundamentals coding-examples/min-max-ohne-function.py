transactions = [10.1, 22.0, 32.2, 17.8, 55.0]

min_value = transactions[0]

for transaction in transactions:
    if transaction < min_value:
        min_value = transaction

print(min_value)

max_value = transactions[0]
for transaction in transactions:
    if transaction > max_value:
        max_value = transaction

print (max_value)

summed = 0
for transaction in transactions:
    summed += transaction

print(summed)
