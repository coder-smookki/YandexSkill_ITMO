import csv
from typing import List, Tuple


def read_questions(filename: str) -> List[Tuple[str, str]]:
    questions = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            question, answer = row
            questions.append((question, answer))
    return questions


def answer_question():
    global score
    answer = input().lower()
    correct_answer = questions[score][1].lower()
    if answer == correct_answer:
        score += 1
        if score == len(questions):
            print(f'Правильно! Вы набрали {score} баллов!')
        else:
            print(f'Правильно! Следующий вопрос: {questions[score][0]}')
            answer_question()
    else:
        print(f'Неправильно! Попробуйте еще раз: {questions[score][0]}')
        answer_question()


questions = read_questions("questions.csv")
score = 0
