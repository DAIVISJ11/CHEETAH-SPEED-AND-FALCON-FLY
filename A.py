# quiz_result_checker.py

def check_quiz(questions, correct_answers):
    print("=== QUIZ START ===")
    user_answers = []
    
    # Ask questions
    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question}")
        answer = input("Your answer: ").strip().upper()
        user_answers.append(answer)

    # Check answers
    score = 0
    print("\n=== RESULTS ===")
    for i, (user_ans, correct_ans) in enumerate(zip(user_answers, correct_answers)):
        result = "✅ Correct" if user_ans == correct_ans else "❌ Wrong"
        print(f"Q{i + 1}: Your answer: {user_ans} | Correct: {correct_ans} -> {result}")
        if user_ans == correct_ans:
            score += 1

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n=== SUMMARY ===")
    print(f"Score: {score} / {total_questions}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Status: PASS 🎉")
    else:
        print("Status: FAIL 😔")


if __name__ == "__main__":
    # You can change these questions and answers
    questions = [
        "What is the capital of France? (A) Paris (B) London (C) Rome",
        "Which number is even? (A) 3 (B) 7 (C) 8",
        "What is 2 + 2? (A) 3 (B) 4 (C) 5",
        "Which is a programming language? (A) Python (B) Snake (C) Lizard",
        "What color is the sky on a clear day? (A) Blue (B) Green (C) Red"
    ]

    # Correct answers (match A/B/C etc.)
    correct_answers = ["A", "C", "B", "A", "A"]

    check_quiz(questions, correct_answers)
