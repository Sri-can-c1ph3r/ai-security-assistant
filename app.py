print("🛡️ Welcome to AI Security Assistant!")

name = input("What is your name? ")

print("Hello", name)

print("\nChoose a topic:")

print("1. SQL Injection")
print("2. XSS")
print("3. Password Security")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    print("SQL Injection lets attackers manipulate database queries.")

elif choice == "2":
    print("XSS allows attackers to run JavaScript in another user's browser.")

elif choice == "3":
    print("Use long, unique passwords and enable MFA.")

else:
    print("Sorry, I don't know that topic yet.")