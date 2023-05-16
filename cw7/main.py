import mysql.connector
import tkinter as tk
from tkinter import ttk


def connection():
    f = open("./account.txt", "r")
    lines = f.readlines()
    host = lines[0]
    user = lines[1]
    password = lines[2]
    database = lines[3]
    f.close()
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password.rstrip(),
        database=database,
    )
    return conn


def fetch_data():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    cursor.close()
    return result


root = tk.Tk()
root.title("Book Store")
treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("title", text="Tytuł")
treeview.heading("author", text="Autor")
treeview.heading("price", text="Cena")
treeview.heading("category", text="Kategoria")
treeview.pack()


def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")

    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()
    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()
    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()
    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def add_new():
        new_title = title_entry.get()
        new_author = author_entry.get()
        new_price = price_entry.get()
        new_category = category_entry.get()

        try:
            conn = connection()
            cursor = conn.cursor()
            sql = 'INSERT INTO books (title, author, price, category) VALUES (%s,%s,%s,%s)'
            params = (new_title, new_author, new_price, new_category)
            cursor.execute(sql, params)
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        load_data()
        new_window.destroy()

    add_button = tk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


add_new_book_button = tk.Button(root, text="Dodaj nową książkę", command=open_new_window)
add_new_book_button.pack(side="left")


def open_details_window(event):
    selected_item = treeview.focus()

    if selected_item:
        item_data = treeview.item(selected_item)
        item_values = item_data["values"]

        details_window = tk.Toplevel(root)
        details_window.title("Szczegóły")

        id_label = ttk.Label(details_window, text="ID:")
        id_label.pack()
        id_entry = ttk.Entry(details_window)
        id_entry.insert(0, item_values[0])
        id_entry.config(state="disabled")
        id_entry.pack()

        title_label = ttk.Label(details_window, text="Tytuł:")
        title_label.pack()
        title_entry = ttk.Entry(details_window)
        title_entry.insert(0, item_values[1])
        title_entry.pack()

        author_label = ttk.Label(details_window, text="Autor:")
        author_label.pack()
        author_entry = ttk.Entry(details_window)
        author_entry.insert(0, item_values[2])
        author_entry.pack()

        price_label = ttk.Label(details_window, text="Cena:")
        price_label.pack()
        price_entry = ttk.Entry(details_window)
        price_entry.insert(0, item_values[3])
        price_entry.pack()

        category_label = ttk.Label(details_window, text="Kategoria:")
        category_label.pack()
        category_entry = ttk.Entry(details_window)
        category_entry.insert(0, item_values[4])
        category_entry.pack()

        def delete():
            try:
                conn = connection()
                cursor = conn.cursor()
                sql = 'DELETE FROM books WHERE id = %s'
                params = (id_entry.get(),)
                cursor.execute(sql, params)
                conn.commit()

            except mysql.connector.Error as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details_window.destroy()
        def update():
            try:
                conn = connection()
                cursor = conn.cursor()
                sql = 'UPDATE books SET title = %s, author = %s, category = %s, price = %s WHERE id = %s'
                params = (title_entry.get(), author_entry.get(), category_entry.get(), price_entry.get(), id_entry.get())
                cursor.execute(sql, params)
                conn.commit()
            except mysql.connector.Error as e:
                print(f"Error: {e}")
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            load_data()
            details_window.destroy()


    updateBtn = tk.Button(details_window, text="Edytuj", command=update)
    updateBtn.pack()
    deleteBtn = tk.Button(details_window, text="Usuń", command=delete)
    deleteBtn.pack()



treeview.bind("<Double-1>", open_details_window)

load_data()
root.mainloop()