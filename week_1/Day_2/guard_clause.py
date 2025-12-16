# Task 1: The Guard Clause

user = None

if user is not None and user == "admin":
    print("User has admin access")
else:
    print("No access")