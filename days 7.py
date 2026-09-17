import json

choice = 0
while choice != 3 :
    print("1. Add User \n"
          "2. Show Users \n"
          "3. Exit")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        with open("users.json", "r") as file:
            our_users = json.load(file)

        name = input("Enter your name: ")
        while True:
            try :
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Please enter a number")
        email = input("Enter your email: ")

        user = {
            "name": name,
            "age": age,
            "email": email
        }
        our_users.append(user)
        with open("users.json", "w") as file:
            json.dump(our_users, file)

    elif choice == 2:
        try:
            with open("users.json", "r") as file:
                our_users = json.load(file)
        except FileNotFoundError:
            print("file not found")
            continue
        except json.JSONDecodeError:
            print("Invalid JSON data")
            continue
        for user in our_users:
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"Email: {user['email']}")
            print("----------------")
    elif choice == 3:
        print("goodbye")

    else :
        print("your choice is invalid")








