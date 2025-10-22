import json
import re


def load_users(path):
    """Load users from a JSON file."""
    with open(path, "r") as file:
        return json.load(file)


def is_valid_email(email):
    """Check if the email address has a valid format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def filter_users_by_name(users, name):
    """Return users whose name matches."""
    return [user for user in users if user.get("name", "").lower() == name.lower()]


def filter_users_by_age(users, age):
    """Return users whose age matches exactly."""
    return [user for user in users if user.get("age") == age]


def filter_users_by_email(users, email):
    """Return users whose email matches exactly."""
    return [user for user in users if user.get("email") == email]


def print_users(users):
    """Print all matching users or a message if none found."""
    if not users:
        print("No users found.")
        return
    for user in users:
        print(user)


def get_filter_option():
    """Ask the user which filter."""
    print("Filter options: name, age, email")
    option = input("What would you like to filter by? ").strip().lower()
    if option in {"name", "age", "email"}:
        return option
    return ""


def main():
    users = load_users("users.json")
    if not users:
        return

    option = get_filter_option()

    if option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        results = filter_users_by_name(users, name_to_search)
        print_users(results)

    elif option == "age":
        while True:
            value = input("Enter an age to filter users: ").strip()
            if not value:
                print("Please enter a value.")
                continue
            try:
                age_to_search = int(value)
                break
            except ValueError:
                print("Age must be an integer. Please try again.")
        results = filter_users_by_age(users, age_to_search)
        print_users(results)

    elif option == "email":
        while True:
            email_to_search = input("Enter an email to filter users: ").strip()
            if is_valid_email(email_to_search):
                results = filter_users_by_email(users, email_to_search)
                print_users(results)
                break
            else:
                print("Invalid email format. Please try again.")

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
