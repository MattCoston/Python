shopping_list = []

print ("What do you need to get at the store?")
print ("Enter 'DONE' to end the program")

while True:
	new_item = input("> ")

	shopping_list.append(new_item)
	if new_item == 'DONE':
		break

print("Here's the list:")

for item in shopping_list:
	print(item)

