import math


groupmates = [
    {"name": "Анна", "surname": "Соколова",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [5, 5, 5]},
    {"name": "Иван", "surname": "Петров",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [4, 4, 4]},
    {"name": "Мария", "surname": "Орлова",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [5, 4, 5]},
    {"name": "Артём", "surname": "Волков",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [3, 3, 4]},
    {"name": "Елена", "surname": "Морозова",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [4, 5, 4]},
    {"name": "Денис", "surname": "Лебедев",
     "exams": ["ПИС", "Математика", "Информатика"], "marks": [3, 3, 3]},
]


def average_mark(student):
    return sum(student["marks"]) / len(student["marks"])


def filter_students(students, threshold):
    return [student for student in students
            if average_mark(student) > threshold]


def print_students(students):
    print(f'{"Имя":<9} {"Фамилия":<10} {"Экзамены":<29} '
          f'{"Оценки":<9} Средний балл')
    for student in students:
        exams = ", ".join(student["exams"])
        marks = " ".join(map(str, student["marks"]))
        print(f'{student["name"]:<9} {student["surname"]:<10} '
              f'{exams:<29} {marks:<9} {average_mark(student):.2f}')
    if not students:
        print("Студентов с таким средним баллом нет.")


def main():
    print("Все студенты:")
    print_students(groupmates)
    while True:
        try:
            threshold = float(input("\nВведите порог среднего балла: ").replace(",", "."))
            if not math.isfinite(threshold):
                raise ValueError
            break
        except ValueError:
            print("Введите конечное число, например 4 или 4,5.")
    print(f"\nСтуденты со средним баллом строго выше {threshold:g}:")
    print_students(filter_students(groupmates, threshold))


if __name__ == "__main__":
    main()
