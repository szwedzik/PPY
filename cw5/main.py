import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
os.environ['SENDGRID_API_KEY'] = 'SG.XXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def load_data():
    data = {}
    try:
        with open("students.txt", 'r') as file:
            for line in file:
                email, name, surname, points = line.strip().split(",")
                data[email] = {
                    "imie": name,
                    "nazwisko": surname,
                    "punkty": points,
                    "ocena": "",
                    "status": ""
                }
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open("students.txt", 'w') as file:
        for email, student in data.items():
            line = f"{email},{student['imie']},{student['nazwisko']},{student['punkty']},{student['ocena']},{student['status']}\n"
            file.write(line)

def add_student(data):
    email = input("Podaj adres email studenta: ")
    if email in data:
        print("Student o podanym adresie email już istnieje")
        return
    name = input("Podaj imię studenta: ")
    surname = input("Podaj nazwisko studenta: ")
    points = input("Podaj punkty studenta: ")
    data[email] = {
        "imie": name,
        "nazwisko": surname,
        "punkty": points,
        "ocena": "",
        "status": ""
    }
    save_data(data)
    print("Student został dodany")

def remove_student(data):
    email = input("Podaj adres email studenta: ")
    if email not in data:
        print("Student o podanym adresie email nie istnieje")
        return
    del data[email]
    save_data(data)
    print("Student został usunięty")

def assign_grade(data):
    for email, student in data.items():
        if student["status"] not in ["GRADED", "MAILED"]:
            points = int(student["punkty"])
            if points > 90:
                grade = "5"
            elif points > 80:
                grade = "4"
            elif points > 70:
                grade = "3"
            elif points > 60:
                grade = "2"
            else:
                grade = "1"
            student["ocena"] = grade
            student["status"] = "GRADED"
    save_data(data)
    print("Oceny zostały przypisane")

def send_emails(data):
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("example@sendgrid.com")
    subject = "Wyniki z egzaminu"
    for email, student in data.items():
        if student["status"] != "MAILED":
            to_email = To(email)
            content = Content("text/plain", f"Witaj {student['imie']}!\nTwoja ocena z egzaminu to {student['ocena']}")
            mail = Mail(from_email, to_email, subject, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            if response.status_code == 202:
                student["status"] = "MAILED"
            else:
                print(f"Nie udało się wysłać wiadomości do {email}")
    save_data(data)
    print("Wysłano wiadomości")

if __name__ == '__main__':
    student = load_data()
    while True:
        print("1. Dodaj studenta")
        print("2. Usuń studenta")
        print("3. Przypisz oceny")
        print("4. Wyślij wiadomości")
        print("5. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            add_student(student)
        elif choice == "2":
            remove_student(student)
        elif choice == "3":
            assign_grade(student)
        elif choice == "4":
            send_emails(student)
        elif choice == "5":
            break
        else:
            print("Nie ma takiej opcji")
