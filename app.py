def security_quiz():
    print("\n🧠 Security Quiz")

    score = 0

    print("\nQuestion 1:")
    print("Which vulnerability involves injecting malicious SQL into a database?")
    print("A. XSS")
    print("B. SQL Injection")
    print("C. CSRF")
    print("D. SSRF")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong! The answer is SQL Injection.")

    print("\nQuestion 2:")
    print("Which vulnerability can execute malicious JavaScript in a user's browser?")
    print("A. XSS")
    print("B. SQL Injection")
    print("C. CSRF")
    print("D. SSRF")

    answer = input("Your answer: ")

    if answer.upper() == "A":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong! The answer is XSS.")

    print("\nQuestion 3:")
    print("What security feature adds an extra verification step during login?")
    print("A. FTP")
    print("B. MFA")
    print("C. HTTP")
    print("D. DNS")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("✅ Correct!")
        score = score + 1
    else:
        print("❌ Wrong! The answer is MFA.")

    print("\n🎉 Quiz Complete!")
    print("Your score:", score, "/ 3")