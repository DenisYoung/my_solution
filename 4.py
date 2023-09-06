import sys
import json

def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    for questions in data["game"]["rounds"]:
        count += len(questions["questions"])

    print(f"Кол-во вопросов: {count}")


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    print("\nПравильные ответы:")
    for questions in data["game"]["rounds"]:
        for question in questions["questions"]:
            print(f"    {question['correct_answer']}")


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time = 0
    for questions in data["game"]["rounds"]:
        for question in questions["questions"]:
            if "time_to_answer" in question and max_time<question["time_to_answer"]:
                max_time = question["time_to_answer"]

    print(f"\nМаксимальное время ответа: {max_time}")


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    filename = sys.argv[1]
    main(filename)
