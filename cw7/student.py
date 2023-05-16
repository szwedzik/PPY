import sqlite3
import tkinter as tk
from tkinter import ttk


def connection():
    return sqlite3.connect('students.db')


def fetch_data():
    try:
        cursor = connection().cursor()
        cursor.execute('SELECT * FROM Student')
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f'Error: {e}')
    finally:
        if cursor:
            cursor.close()
        if connection():
            connection().close()


root = tk.Tk()
root.title('Students')
treeview = ttk.Treeview(root)
treeview['columns'] = ('id', 'name', 'surname', 'points', 'grade')
treeview.column('#0', width=0)
treeview.heading('id', text='ID')
treeview.heading('name', text='Imię')
treeview.heading('surname', text='Nazwisko')
treeview.heading('points', text='Punkty')
treeview.heading('grade', text='Ocena')
treeview.pack()


def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert('', 'end', values=row)


def open_add_student_window():
    add_student_window = tk.Toplevel(root)
    add_student_window.title('Dodaj studenta')
    add_student_window.geometry('400x250')
    name_label = tk.Label(add_student_window, text='Imię')
    name_label.pack()
    name_entry = tk.Entry(add_student_window)
    name_entry.pack()
    surname_label = tk.Label(add_student_window, text='Nazwisko')
    surname_label.pack()
    surname_entry = tk.Entry(add_student_window)
    surname_entry.pack()
    points_label = tk.Label(add_student_window, text='Punkty')
    points_label.pack()
    points_entry = tk.Entry(add_student_window)
    points_entry.pack()
    grade_label = tk.Label(add_student_window, text='Ocena')
    grade_label.pack()
    grade_entry = tk.Entry(add_student_window)
    grade_entry.pack()

    def add_student():
        try:
            conn = connection()
            cursor = conn.cursor()
            sql = 'INSERT INTO Student (name, surname, points, grade) VALUES (?, ?, ?, ?)'
            params = (name_entry.get(), surname_entry.get(), points_entry.get(), grade_entry.get())
            cursor.execute(sql, params)
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error: {e}')
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        load_data()
        add_student_window.destroy()

    add_student_btn = tk.Button(add_student_window, text='Dodaj', command=add_student)
    add_student_btn.pack()


def open_student_details_window(event):
    selected = treeview.focus()

    if selected:
        data = treeview.item(selected)
        values = data['values']

        details = tk.Toplevel(root)
        details.geometry('400x250')
        details.title('Szczegóły studenta: ' + values[1] + ' ' + values[2])

        id_label = tk.Label(details, text='ID')
        id_label.pack()
        id_entry = tk.Entry(details)
        id_entry.insert(0, values[0])
        id_entry.config(state='disabled')
        id_entry.pack()

        name_label = tk.Label(details, text='Imię')
        name_label.pack()
        name_entry = tk.Entry(details)
        name_entry.insert(0, values[1])
        name_entry.pack()

        surname_label = tk.Label(details, text='Nazwisko')
        surname_label.pack()
        surname_entry = tk.Entry(details)
        surname_entry.insert(0, values[2])
        surname_entry.pack()

        points_label = tk.Label(details, text='Punkty')
        points_label.pack()
        points_entry = tk.Entry(details)
        points_entry.insert(0, values[3])
        points_entry.pack()

        grade_label = tk.Label(details, text='Ocena')
        grade_label.pack()
        grade_entry = tk.Entry(details)
        grade_entry.insert(0, values[4])
        grade_entry.pack()

        def delete():
            try:
                conn = connection()
                cursor = conn.cursor()
                sql = 'DELETE FROM Student WHERE id=?'
                params = (id_entry.get(),)
                cursor.execute(sql, params)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error: {e}')
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details.destroy()

        def update():
            try:
                conn = connection()
                cursor = conn.cursor()
                sql = 'UPDATE Student SET name=?, surname=?, points=?, grade=? WHERE id=?'
                params = (name_entry.get(), surname_entry.get(), points_entry.get(), grade_entry.get(), id_entry.get())
                cursor.execute(sql, params)
                conn.commit()
            except sqlite3.Error as e:
                print(f'Error: {e}')
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details.destroy()


    updateBtn = tk.Button(details, text='Edytuj', command=update)
    updateBtn.pack()
    deleteBtn = tk.Button(details, text='Usuń', command=delete)
    deleteBtn.pack()




addStudentBtn = tk.Button(root, text="Dodaj studenta", command=open_add_student_window)
addStudentBtn.pack(side="left")

treeview.bind("<Double-1>", open_student_details_window)

load_data()
root.mainloop()

if __name__ == '__main__':
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            points REAL,
            grade REAL
            )''')
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error: {e}')
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()