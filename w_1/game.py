import random

number = random.randint(0, 101)

print("Вгадайте число від 0 до 100")
print("Для того, щоб вийти, введіть: q")

while True:
    answer = input("Введіть число: ")
    if not answer or answer == "q":
        break

    if not answer.isdigit():
        print("Введіть правильне число")
        continue

    user_answer: int = int(answer)

    if user_answer > number:
        print("Загадане число — менше")
    elif user_answer < number:
        print("Загадане число — більше")
    else:
        print("Правильно!")
