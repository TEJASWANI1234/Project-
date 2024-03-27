class User:
    def __init__(self, name, roll_no, email, password):
        self.name = name
        self.roll_no = roll_no
        self.email = email
        self.password = password

class RegistrationSystem:
    def __init__(self):
        self.registered_users = {}
        self.current_user = None

    def register(self):
        print("\nRegistration Form:")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll No: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        # Basic validation
        if not name or not roll_no or not email or not password:
            print("Please fill in all fields.")
            return

        confirm_password = input("Confirm Password: ")
        if password != confirm_password:
            print("Passwords do not match.")
            return

        # Store user information
        self.registered_users[roll_no] = User(name, roll_no, email, password)
        print("Registration successful for", name)

    def login(self):
        print("\nLogin Form:")
        roll_no = input("Enter Roll No: ")
        password = input("Enter Password: ")

        # Check if user exists and password matches
        if roll_no in self.registered_users and self.registered_users[roll_no].password == password:
            self.current_user = roll_no
            print("Login successful for", self.registered_users[roll_no].name)
            self.display_details()
        else:
            print("Invalid Roll No. or Password")

    def display_details(self):
        if self.current_user:
            user = self.registered_users[self.current_user]
            print("\nUser Details:")
            print("Name:", user.name)
            print("Roll No:", user.roll_no)
            print("Email:", user.email)
        else:
            print("No user logged in.")

    def logout(self):
        if self.current_user:
            print("\nLogging out user:", self.registered_users[self.current_user].name)
            self.current_user = None
        else:
            print("No user logged in.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Display Details")
            print("4. Logout")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.display_details()
            elif choice == '4':
                self.logout()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    registration_system = RegistrationSystem()
    registration_system.main_menu()
