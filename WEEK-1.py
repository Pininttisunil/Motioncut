class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of India?", "options": ['A) Delhi', 'B) Benguluru', 'C) Hydrabad', 'D) Tamil nadu'], "answer": "A"},
            {"question": "Who is the PM of India?", "options": ['A) Modi', 'B) Amit Sha', 'C) Naveen', 'D) Pawan Kalyan'], "answer": "A"},
            {"question": "What does CPU stand for?", "options": ['A) Central Process Unit', 'B) Computer Personal Unit', 'C) Central Processor Unit', 'D) Central Processing Unit'], "answer": "D"}
        ]
        self.score = 0

    def start_quiz(self):
        for question in self.questions:
            print(question["question"])
            for option in question["options"]:
                print(option)
            user_answer = input("Enter your answer (A, B, C, or D): ").upper()
            if user_answer == question["answer"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is {question['answer']}.")
        self.show_final_score()

    def show_final_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")
def customize_quiz(quiz):
    pass

def main():
    quiz_game = QuizGame()
    customize_quiz(quiz_game)
    quiz_game.start_quiz()

if __name__ == "__main__":
    main()
