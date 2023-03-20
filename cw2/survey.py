name = input("Jak masz na imię? ")
questions = [
    "Jak często ćwiczysz?",
    "Jaka jest Twoja ulubiona potrawa?",
    "Co robisz w wolnym czasie?",
    "Jaką muzykę preferujesz?",
    "Gdzie najchętniej spędzasz wakacje?",
    "Która pora roku jest Twoja ulubiona?",
    "Jakie jest Twoje ulubione zwierzę?"
]

answers = [
    ["codziennie", "raz w tygodniu", "raz w miesiącu"],
    ["pizza", "sushi", "pierogi"],
    ["czytam książki", "gram w gry", "uprawiam sport"],
    ["rock", "pop", "klasyczna"],
    ["nad morzem", "w górach", "w mieście"],
    ["wiosna", "lato", "jesień"],
    ["kot", "pies", "ptak"]
]

user_answers = []

def ask_question(question, answers):
    print(question)
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    user_input = input("Twoja odpowiedź (podaj numer): ")
    while not user_input.isdigit() or int(user_input) not in range(1, len(answers)+1):
        print("Nieprawidłowa odpowiedź. Podaj numer z zakresu 1 -", len(answers))
        user_input = input("Twoja odpowiedź (podaj numer): ")
    return int(user_input)

for i, question in enumerate(questions):
    print(f"Pytanie {i+1}/{len(questions)}")
    answer_index = ask_question(question, answers[i])
    user_answer = answers[i][answer_index-1]
    user_answers.append(user_answer)

print(f"Cześć {name}! \nOto Twoje odpowiedzi:")
for i, question in enumerate(questions):
    print(f"{question}: {user_answers[i]}")
