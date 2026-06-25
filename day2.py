import json
with open("data1.json", "r") as file:
    data = json.load(file)
new_item = input("Enter item to add: ")
data["shopping_list"].append(new_item)
with open("data1.json", "w") as file:
    json.dump(data, file, indent=4)
print("Item added!")

import json
with open("data1.json", "r") as file:
    data = json.load(file)
for item in data["shopping_list"]:
    print(item)

import json
with open("data1.json", "r") as file:
    data = json.load(file)
item_name = input("Enter item name to remove: ")
for item in data["shopping_list"]:
    if item["item"] == item_name:
        data["shopping_list"].remove(item)
        print("Item removed ")
        break
else:
    print("Item not found")
with open("data1.json", "w") as file:
    json.dump(data, file, indent=4)




import json
with open("data1.json","r") as file:
    data=json.load(file)
for item in data["shopping_list"]:
    print(item)


import json
with open ("data1.json") as file:
    data=json.load(file)
new_item=input()
data["shopping_list"].append(new_item)
with open("data1.json","w") as file:
    json.dump(data,file ,indent=4)
print("item added!")


