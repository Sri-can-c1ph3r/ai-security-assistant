def show_sql():
    print("\n📚 SQL Injection")
    print("SQL Injection allows attackers to manipulate database queries.")


def show_xss():
    print("\n📚 XSS")
    print("Cross-Site Scripting can execute malicious JavaScript in a user's browser.")


def show_password():
    print("\n🔐 Password Tips")
    print("Use long, unique passwords, a password manager, and enable MFA.")


def security_quiz():
    print("\n🧠 Security Quiz")
    print("Which vulnerability involves injecting malicious SQL into a database?")
    print("A. XSS")
    print("B. SQL Injection")
    print("C. CSRF")
    print("D. SSRF")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("✅ Correct! Nice one.")
    else:
        print("❌ Not quite. The answer is SQL Injection.")


print("🛡️ Welcome to AI Security Assistant")

while True:

    print("\n===================")
    print("1. SQL Injection")
    print("2. XSS")
    print("3. Password Tips")
    print("4. Security Quiz")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_sql()

    elif choice == "2":
        show_xss()

    elif choice == "3":
        show_password()

    elif choice == "4":
        security_quiz()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")