import random


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

    questions = [
        {
            "question": "Which vulnerability involves injecting malicious SQL into a database?",
            "options": ["XSS", "SQL Injection", "CSRF", "SSRF"],
            "answer": "B"
        },
        {
            "question": "Which vulnerability can execute malicious JavaScript in a user's browser?",
            "options": ["XSS", "SQL Injection", "CSRF", "SSRF"],
            "answer": "A"
        },
        {
            "question": "What security feature adds an extra verification step during login?",
            "options": ["FTP", "MFA", "HTTP", "DNS"],
            "answer": "B"
        }
    ]

    random.shuffle(questions)

    score = 0

    for question in questions:
        print("\n" + question["question"])

        print("A.", question["options"][0])
        print("B.", question["options"][1])
        print("C.", question["options"][2])
        print("D.", question["options"][3])

        answer = input("Your answer: ")

        if answer.upper() == question["answer"]:
            print("✅ Correct!")
            score = score + 1
        else:
            print("❌ Wrong!")

    print("\n🎉 Quiz Complete!")
    print("Your score:", score, "/", len(questions))

    if score == 3:
        print("🏆 Excellent! You got everything right!")
    elif score == 2:
        print("👍 Good job! You have a solid understanding.")
    elif score == 1:
        print("📚 Keep practicing. You're getting there!")
    else:
        print("💪 Don't worry! Time to review the basics.")


def security_tip():
    tips = [
        "🔐 Use MFA whenever possible.",
        "🛡️ Keep your software and dependencies updated.",
        "🎣 Be careful with suspicious links and attachments.",
        "🔑 Never reuse passwords across important accounts.",
        "🌐 Avoid sending sensitive data over untrusted networks."
    ]

    print("\n💡 Security Tip:")
    print(random.choice(tips))


print("🛡️ Welcome to AI Security Assistant!")

name = input("What is your name? ")

history = []

print("\nHello", name, "👋")

while True:

    print("\n===================")
    print("1. SQL Injection")
    print("2. XSS")
    print("3. Password Tips")
    print("4. Security Quiz")
    print("5. Exit")
    print("6. Random Security Tip")

    choice = input(f"{name}, choose an option: ")

    if choice == "1":
        history.append("SQL Injection")
        show_sql()

    elif choice == "2":
        history.append("XSS")
        show_xss()

    elif choice == "3":
        history.append("Password Tips")
        show_password()

    elif choice == "4":
        history.append("Security Quiz")
        security_quiz()

    elif choice == "5":
        print("\n📝 Your session history:")

        for item in history:
            print("-", item)

        print("\nGoodbye!")
        break

    elif choice == "6":
        history.append("Random Security Tip")
        security_tip()

    else:
        print("Invalid option.")