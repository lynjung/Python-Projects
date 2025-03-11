def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").upper()
        if answer == question["answer"]:
            print("✅Correct!\n")
            score += 1
        else:
            print("❌Wrong! The correct answer was", question["answer"], "\n")
    print(f"🏆Your score: {score}/{len(questions)}")

questions = [
    {
        "prompt": "1) What is the capital of South Korea?",
        "options": ["A. Seoul", "B. Busan", "C. Incheon", "D. Jeju"],
        "answer": "A"
    },
    {
        "prompt": "2) Which river is the longest in the world?",
        "options": ["A. Amazon", "B. Mississippi", "C. Nile", "D. Yangtze"],
        "answer": "C"
    },
    {
        "prompt": "3) Who painted the Mona Lisa?",
        "options": ["A. Picasso", "B. Christopher Columbus", "C. Vincent Van Gogh", "D. Leonardo da Vinci"],
        "answer": "D"
    },
    {
        "prompt": "4) Which fruit is most consumed in the world?",
        "options": ["A. Apple", "B. Watermelon", "C. Banana", "D. Strawberry"],
        "answer": "C"
    }
]

print("📖Welcome to the general knowledge quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Hope to see you again, bye!")
    quit()
print("Okay! Let's play ☺️\n")
run_quiz(questions)