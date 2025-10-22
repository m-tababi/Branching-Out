import json
import re


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    for user in filtered_users:
        print(user)


def is_valid_email(email):
    """Check if the email address has a valid format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' is supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    if filter_option == "age":
        age_to_search = int(input("Enter an age to filter users: ").strip())
        filter_users_by_age(age_to_search)
    if filter_option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if is_valid_email(email_to_search):
                filter_users_by_email(email_to_search)
                break
            else:
                print("Invalid email format. Please try again.")

    else:
        print("Filtering by that option is not yet supported.")
