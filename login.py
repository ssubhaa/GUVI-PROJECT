# login.py

# Sample user credentials
valid_username = "admin"
valid_password = "password123"

def login(username, password):
    if username == valid_username and password == valid_password:
        return "Login successful!"
    else:
        return "Invalid credentials."

# Simulate user input (for demonstration purposes)
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(login(username, password))
