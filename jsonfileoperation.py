
import json
file_name = "shopping_list.json"
try:
    with open(file_name, "r") as file:
        shopping_list = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    shopping_list = []
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Display Items")
    print("4. Show Raw JSON Data")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found.")

    elif choice == "3":
        if shopping_list:
            print("Shopping List:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Shopping list is empty.")

    elif choice == "4":
        print(shopping_list)

    elif choice == "5":
        with open(file_name, "w") as file:
            json.dump(shopping_list, file, indent=4)
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice.")










