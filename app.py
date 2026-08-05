def show_sql():
    print("\n📚 SQL Injection")
    print("SQL Injection allows attackers to manipulate database queries.")


def show_xss():
    print("\n📚 XSS")
    print("Cross-Site Scripting executes malicious JavaScript in another user's browser.")


def show_password():
    print("\n🔐 Password Tips")
    print("Use long passwords, enable MFA, and use a password manager.")


print("🛡️ Welcome to AI Security Assistant")

while True:

    print("\n===================")
    print("1. SQL Injection")
    print("2. XSS")
    print("3. Password Tips")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_sql()

    elif choice == "2":
        show_xss()

    elif choice == "3":
        show_password()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")