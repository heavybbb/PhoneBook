# Это ДЗ ( если сверх обязательной части) можно разделить на 2 этапа, в этом ДЗ сдаете первый этап. 
# В качестве итогового ДЗ по этому курсу сдаете доделанный проект.

# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, 
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
# для отлично в группах (до 2человек включительно) надо выполнить или ТГ бот или ГУИ 
# (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
# для отлично в группах (до 3 человек включительно) надо выполнить или ТГ бот + БД или ГУИ+ БД.
# ГУИ можно сделать просто на EasyGUI или Tkinter
# Формат сдачи: ссылка на свой репозиторий в гитхаб. Грамотно оформляем Readme.md, 
# это по сути рекламное описание вашего приложения.


import sqlite3 as sl
import easygui as eg

with sl.connect('phonebook.db') as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone
            (
                id INTEGER PRIMARY KEY,
           name TEXT,
           famele TEXT,
           number TEXT,
           email TEXT
            );
            """)


def view_contacts():
    conn = sl.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM phone')
    contacts = cur.fetchall()
    conn.commit()
    conn.close()
    if contacts:
        contact_info = '\n'.join([f"ID: {contact[0]}, Имя: {contact[1]}, Фамилия: {contact[2]}, Номер телефона: {contact[3]}, E-mail: {contact[4]}" for contact in contacts])
        eg.msgbox(msg=contact_info, title='Список контактов')
    else:
        eg.msgbox(msg='пусто', title='Список контактов')

def add_contact(name, famele, number, email):
    conn = sl.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO phone (name, famele, number, email) VALUES (?, ?, ?, ?)', (name, famele, number, email))
    conn.commit()
    conn.close()
    eg.msgbox(msg=f"Контакт {name} добавлен.", title='Добавление контакта')

def import_contacts(file_path):
    try:
        conn.execute('pragma encoding="UTF-8"')
        cur = conn.cursor()
        with open(file_path, 'r') as file:
            imported_contacts = [tuple(line.strip().split(',')) for line in file.readlines()]
            cur.executemany('INSERT INTO phone (name, famele, number, email) VALUES (?, ?, ?, ?)', imported_contacts)
            conn.commit()
            conn.close()
        eg.msgbox(msg='Контакты импортированы.', title='Импорт контактов')
    except FileNotFoundError:
        eg.msgbox(msg='Файл не найден.', title='Ошибка')
    except Exception as e:
        eg.msgbox(msg=f'Ошибка при импорте: {e}', title='Ошибка')

def search_contacts(keyword):
    conn = sl.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM phone WHERE name LIKE ? OR famele LIKE ? OR number LIKE ? OR email LIKE ?', ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))
    found_contacts = cur.fetchall()
    conn.close()
    if found_contacts:
        contact_info = '\n'.join([f"ID: {contact[0]}, Имя: {contact[1]}, Фамилия: {contact[2]}, Номер телефона: {contact[3]}, E-mail: {contact[4]}" for contact in found_contacts])
        eg.msgbox(msg=contact_info, title=f'Результаты поиска : {keyword}')
    else:
        eg.msgbox(msg='Контакты не найдены.', title='Результаты поиска')

def delete_contact(id):
    conn = sl.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM phone WHERE id=?', (id,))
    conn.commit()
    conn.close()
    eg.msgbox(msg="Контакт удален.", title='Удаление контакта')

def edit_contact(id, name, famele, number, email):
    conn = sl.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('UPDATE phone SET name=?, famele=?, number=?, email=? WHERE id=?', (name, famele, number, email, id))
    conn.commit()
    conn.close()
    eg.msgbox(msg="Контакт изменен.", title='Изменение контакта')

def main():
    while True:
        choice = eg.buttonbox(msg='Выберите действие:', title='Телефонный справочник', choices=['Просмотр контактов', 'Добавление контакта', 'Импорт контактов', 'Поиск контактов', 'Удаление контакта', 'Изменение контакта', 'Выход'])
        if choice == 'Просмотр контактов':
            view_contacts()
        elif choice == 'Добавление контакта':
           input_data = eg.multenterbox(msg='Введите данные контакта:', title='Добавление контакта', fields=['Имя', 'Фамилия', 'Номер телефона', 'E-mail'])
           if input_data:
                name, famele, number, email = input_data
                add_contact(name, famele, number, email)
                    
        elif choice == 'Импорт контактов':
            file_path = eg.fileopenbox(msg='Выберите файл для импорта:', title='Импорт контактов', filetypes=['*.txt'])
            if file_path:
                import_contacts(file_path)
        elif choice == 'Поиск контактов':
            keyword = eg.enterbox(msg='Введите ключевое слово для поиска:', title='Поиск контактов')
            if keyword:
                search_contacts(keyword)
        elif choice == 'Удаление контакта':
            id = eg.enterbox(msg='Введите ID контакта для удаления:', title='Удаление контакта')
            if id:
                delete_contact(int(id))
        elif choice == 'Изменение контакта':
            id = eg.enterbox(msg='Введите ID контакта для изменения:', title='Изменение контакта')
            if id:
                name, famele, number, email = eg.multenterbox(msg='Введите новые данные контакта:', title='Изменение контакта', fields=['Имя', 'Фамилия', 'Номер телефона', 'E-mail'])
                if name and famele and number and email:
                    edit_contact(int(id), name, famele, number, email)
        elif choice == 'Выход':
            break
main()