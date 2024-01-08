import json
import hashlib


def load_users():
    # Load existing users or initialize as empty list
    try:
        with open("data/users.json", mode='r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        users = []
    return users


def save_users(users):
    # Func for save users in JSON-file
    with open("data/users.json", mode='w', newline='') as file:
        json.dump(users, file, indent=4)


def registration_func():
    try:
        # Load users.
        users = load_users()

        # Input data for new user(name, password, email)
        name_ = input("Enter username: ")
        if name_.isdigit():
            raise ValueError(f'Enter your really name without nums!')
        password_ = input("Enter password: ")
        if len(password_) < 5:
            raise ValueError(f'Password need have more than 7 symbols. Try again!')
        hashed_password = hashlib.sha256(password_.encode()).hexdigest()
        email_ = input("Enter email: ")
        if "@" not in email_:
            raise ValueError(f'{email_} without "@". Try again')

        # Check if email is already registered

        for user in users:
            if user["email"] == email_:
                print("This email is already registered in the system.")
                return

        # Add new user
        new_user = {"name": name_, "password": hashed_password, "email": email_}
        users.append(new_user)

        save_users(users)

        print(f"User {name_} successfully registered.")
    except ValueError as e:
        print(e)


def auth_func(email, password):
    # Load users:
    users = load_users()

    # Check if email in JSON file and correct password.
    for user in users:
        if user["email"] == email and user["password"] == hashlib.sha256(password.encode()).hexdigest():
            print(f"Hello!")
            return True
    print("Invalid Password or email")
    return False


def login_func():
    # Func for login in system with correct email and password.
    try:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if auth_func(email, password):
            print("Login success! Welcome!")
            return True
        else:
            print("Login filed")
            return False
    except Exception as e:
        print(e)


def change_password(email):
    # Load users.
    users = load_users()

    # Func for change password. Key is email data.
    for user in users:
        if user["email"] == email:
            new_pass = input("Enter new password")
            user["password"] = hashlib.sha256(new_pass.encode()).hexdigest()
            save_users(users)
            print("Password changed!")
            return
    print("User not found!")


# If unique email in users
def is_email_unique(new_email, users):
    for user in users:
        if user["email"] == new_email:
            return False
    return True


# Func for change email.
def change_email(email):
    # Load users.
    users = load_users()

    for user in users:
        if user["email"] == email:
            new_email = input("Enter new email: ")

            if is_email_unique(new_email, users):
                user["email"] = new_email
                save_users(users)
                print("Email changed!")
            else:
                print("Email already exists. Choose a different one.")
            return
    print("User not found!")


# Function for delete account from JSON-file.
def delete_account(email):
    # Load users.
    users = load_users()

    for user in users:
        if user["email"] == email:
            users.remove(user)
            save_users(users)
            print("Account deleted!")
            return
    print("User not found!")


# Function with menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login in system")
        print("3. Change Password")
        print("4. Change Email")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            registration_func()
        elif choice == '2':
            login_func()
        elif choice == '3':
            email = input("Enter your email: ")
            change_password(email)
        elif choice == '4':
            email = input("Enter your email: ")
            change_email(email)
        elif choice == '5':
            email = input("Enter your email: ")
            delete_account(email)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

