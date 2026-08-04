print("🛡️ Welcome to AI Security Assistant")

while True:

    print("\n==========================")
    print("1. Learn SQL Injection")
    print("2. Learn XSS")
    print("3. Password Tips")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nSQL Injection attacks databases by manipulating queries.")

    elif choice == "2":
        print("\nXSS executes malicious JavaScript in another user's browser.")

    elif choice == "3":
        print("\nUse a password manager and enable MFA.")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option.")