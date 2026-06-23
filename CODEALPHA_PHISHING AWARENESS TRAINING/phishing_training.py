# Phishing Awareness Training Quiz

score = 0

print("===================================")
print(" PHISHING AWARENESS TRAINING ")
print("===================================\n")

questions = [
    {
        "question": "1. What is phishing?",
        "options": ["A. A fishing technique", "B. A cyberattack to steal information", "C. A computer game"],
        "answer": "B"
    },
    {
        "question": "2. Which email looks suspicious?",
        "options": ["A. support@amazon.com", "B. help@paypal.com", "C. security@amaz0n-login.com"],
        "answer": "C"
    },
    {
        "question": "3. Before clicking a link, you should:",
        "options": ["A. Click immediately", "B. Verify sender and URL", "C. Ignore the email"],
        "answer": "B"
    },
    {
        "question": "4. What does MFA stand for?",
        "options": ["A. Multi-Factor Authentication", "B. Main Firewall Access", "C. Multiple File Access"],
        "answer": "A"
    }
]

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer: ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect!\n")

print("===================================")
print(" TRAINING SUMMARY ")
print("===================================")
print(f"Score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent! You are highly aware of phishing threats.")
elif score >= 2:
    print("Good job! Keep improving your cybersecurity awareness.")
else:
    print("Please review phishing awareness best practices.")