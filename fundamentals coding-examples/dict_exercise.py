fruits = {}
list_fruits = []
run_program = True
while run_program == True:
    input_text = input("Enter an item (or 'done' to finish): ")
    if input_text == 'done':
        run_program = False
    else:
        list_fruits.append(input_text)


for fruit in list_fruits:
    if fruit in fruits:
        fruits[fruit] += 1
    else:
        fruits.update({fruit: 1})


print("Item counts:")
for fruit in fruits:
    print(f"{fruit}: {fruits[fruit]} ")
