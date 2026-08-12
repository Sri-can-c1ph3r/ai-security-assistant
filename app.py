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