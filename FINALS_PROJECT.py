import sys
import os
import json
import random
from datetime import datetime
DATA_DIR = 'school_data'
os.makedirs(DATA_DIR, exist_ok=True)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def wait_enter(msg='Press Enter to continue...'):
    input(msg)
def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
def timestamp():
    return datetime.now().isoformat()
STUDENTS_FILE = os.path.join(DATA_DIR, 'students.json')
students = load_json(STUDENTS_FILE, []) or []
def save_students():
    save_json(STUDENTS_FILE, students)
def list_students():
    if not students:
        print('No students found.')
        return
    for s in students:
        print(f"ID:{s['id']} Name:{s['name']} Grade:{s['grade']} Enrolled:{s.get('enrolled', True)}")
def add_student():
    sid = input('Student ID: ').strip()
    name = input('Name: ').strip()
    grade = input('Grade: ').strip()
    student = {'id': sid, 'name': name, 'grade': grade, 'created': timestamp(), 'enrolled': True}
    students.append(student)
    save_students()
    print('Student added.')
def find_student_index(sid):
    for i, s in enumerate(students):
        if s['id'] == sid:
            return i
    return -1
def update_student():
    sid = input('Enter Student ID to update: ').strip()
    idx = find_student_index(sid)
    if idx == -1:
        print('Student not found.')
        return
    s = students[idx]
    print('Leave blank to keep current value.')
    name = input(f"Name [{s['name']}]: ").strip()
    grade = input(f"Grade [{s['grade']}]: ").strip()
    if name:
        s['name'] = name
    if grade:
        s['grade'] = grade
    s['modified'] = timestamp()
    save_students()
    print('Student updated.')
def remove_student():
    sid = input('Enter Student ID to remove: ').strip()
    idx = find_student_index(sid)
    if idx == -1:
        print('Student not found.')
        return
    students.pop(idx)
    save_students()
    print('Student removed.')
def student_submenu():
    while True:
        print('\n-- Student Management --')
        print('1. List students')
        print('2. Add student')
        print('3. Update student')
        print('4. Remove student')
        print('5. Back to main menu')
        choice = input('Choose: ').strip()
        if choice == '1':
            list_students()
            wait_enter()
        elif choice == '2':
            add_student()
            wait_enter()
        elif choice == '3':
            update_student()
            wait_enter()
        elif choice == '4':
            remove_student()
            wait_enter()
        elif choice == '5':
            break
        else:
            print('Invalid choice.')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')
books = load_json(BOOKS_FILE, []) or []
def save_books():
    save_json(BOOKS_FILE, books)
def list_books(show_all=True):
    if not books:
        print('No books in the library.')
        return
    for b in books:
        status = 'Available' if b.get('available', True) else f"Borrowed by {b.get('borrower')}"
        if show_all or b.get('available', True):
            print(f"ID:{b['id']} Title:{b['title']} Author:{b['author']} Status:{status}")
def add_book():
    bid = input('Book ID: ').strip()
    title = input('Title: ').strip()
    author = input('Author: ').strip()
    book = {'id': bid, 'title': title, 'author': author, 'available': True, 'added': timestamp()}
    books.append(book)
    save_books()
    print('Book added.')
def find_book_index(bid):
    for i, b in enumerate(books):
        if b['id'] == bid:
            return i
    return -1
def borrow_book():
    bid = input('Enter Book ID to borrow: ').strip()
    idx = find_book_index(bid)
    if idx == -1:
        print('Book not found.')
        return
    b = books[idx]
    if not b.get('available', True):
        print('Book is currently borrowed.')
        return
    borrower = input('Borrower name: ').strip()
    b['available'] = False
    b['borrower'] = borrower
    b['borrowed_at'] = timestamp()
    save_books()
    print('Book borrowed.')
def return_book():
    bid = input('Enter Book ID to return: ').strip()
    idx = find_book_index(bid)
    if idx == -1:
        print('Book not found.')
        return
    b = books[idx]
    if b.get('available', True):
        print('This book is not marked as borrowed.')
        return
    b['available'] = True
    b.pop('borrower', None)
    b.pop('borrowed_at', None)
    save_books()
    print('Book returned.')
def library_submenu():
    while True:
        print('\n-- Library System --')
        print('1. List all books')
        print('2. List available books')
        print('3. Add book')
        print('4. Borrow book')
        print('5. Return book')
        print('6. Back to main menu')
        choice = input('Choose: ').strip()
        if choice == '1':
            list_books(show_all=True)
            wait_enter()
        elif choice == '2':
            list_books(show_all=False)
            wait_enter()
        elif choice == '3':
            add_book()
            wait_enter()
        elif choice == '4':
            borrow_book()
            wait_enter()
        elif choice == '5':
            return_book()
            wait_enter()
        elif choice == '6':
            break
        else:
            print('Invalid choice.')
ITEMS_FILE = os.path.join(DATA_DIR, 'items.json')
items = load_json(ITEMS_FILE, []) or []
def save_items():
    save_json(ITEMS_FILE, items)
def list_items():
    if not items:
        print('No items in inventory.')
        return
    for it in items:
        print(f"ID:{it['id']} Name:{it['name']} Qty:{it['qty']} Price:{it.get('price', 'N/A')}")
def add_item():
    iid = input('Item ID: ').strip()
    name = input('Name: ').strip()
    qty = input('Quantity: ').strip()
    try:
        qty = int(qty)
    except ValueError:
        print('Quantity must be an integer.')
        return
    price = input('Price (optional): ').strip()
    try:
        price = float(price) if price else None
    except ValueError:
        print('Price must be a number.')
        return
    item = {'id': iid, 'name': name, 'qty': qty, 'price': price, 'added': timestamp()}
    items.append(item)
    save_items()
    print('Item added.')
def update_item():
    iid = input('Enter Item ID to update: ').strip()
    for it in items:
        if it['id'] == iid:
            name = input("Name [{0}]: ".format(it['name'])).strip()
            qty = input("Qty [{0}]: ".format(it['qty'])).strip()
            if name: it['name'] = name
            if qty:
                try:
                    it['qty'] = int(qty)
                except ValueError:
                    print('Quantity must be integer.')
            save_items()
            print('Item updated.')
            return
    print('Item not found.')
def remove_item():
    iid = input('Enter Item ID to remove: ').strip()
    for i, it in enumerate(items):
        if it['id'] == iid:
            items.pop(i)
            save_items()
            print('Item removed.')
            return
    print('Item not found.')
def inventory_submenu():
    while True:
        print('\n-- Inventory System --')
        print('1. List items')
        print('2. Add item')
        print('3. Update item')
        print('4. Remove item')
        print('5. Back to main menu')
        choice = input('Choose: ').strip()
        if choice == '1':
            list_items()
            wait_enter()
        elif choice == '2':
            add_item()
            wait_enter()
        elif choice == '3':
            update_item()
            wait_enter()
        elif choice == '4':
            remove_item()
            wait_enter()
        elif choice == '5':
            break
        else:
            print('Invalid choice.')
def notepad_tool():
    print('\n-- Simple Notepad --')
    fname = input('Filename to create/read (inside school_data): ').strip()
    if not fname:
        print('No filename provided.')
        return
    path = os.path.join(DATA_DIR, fname)
    if os.path.exists(path):
        print('File exists. Contents:')
        with open(path, 'r', encoding='utf-8') as f:
            print(f.read())
    else:
        print('File does not exist. Creating new file.')
    text = input('Enter text to append (single line): ')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    print('Saved.')
def converter_tool():
    print('\n-- Simple Converter --')
    print('1. Celsius to Fahrenheit')
    print('2. Kilograms to Pounds')
    choice = input('Choose: ').strip()
    if choice == '1':
        c = input('Celsius: ').strip()
        try:
            c = float(c)
            f = (c * 9/5) + 32
            print("{}C = {}F".format(c, f))
        except ValueError:
            print('Invalid number.')
    elif choice == '2':
        kg = input('Kilograms: ').strip()
        try:
            kg = float(kg)
            lb = kg * 2.20462
            print("{} kg = {} lb".format(kg, lb))
        except ValueError:
            print('Invalid number.')
    else:
        print('Invalid choice.')
def tools_submenu():
    while True:
        print('\n-- Tools --')
        print('1. Notepad')
        print('2. Converter')
        print('3. Back to main menu')
        ch = input('Choose: ').strip()
        if ch == '1':
            notepad_tool()
            wait_enter()
        elif ch == '2':
            converter_tool()
            wait_enter()
        elif ch == '3':
            break
        else:
            print('Invalid choice.')
def rps_game():
    choices = ['rock', 'paper', 'scissors']
    print('\n-- Rock Paper Scissors --')
    while True:
        u = input('Choose (rock/paper/scissors) or q to quit: ').strip().lower()
        if u == 'q':
            break
        if u not in choices:
            print('Invalid choice.')
            continue
        c = random.choice(choices)
        print('Computer chose:', c)
        if u == c:
            print('Tie!')
        elif (u == 'rock' and c == 'scissors') or (u == 'paper' and c == 'rock') or (u == 'scissors' and c == 'paper'):
            print('You win!')
        else:
            print('You lose!')
def guessing_game():
    print('\n-- Number Guessing --')
    secret = random.randint(1, 50)
    attempts = 0
    while True:
        g = input('Guess (1-50) or q to quit: ').strip().lower()
        if g == 'q':
            break
        try:
            g = int(g)
        except ValueError:
            print('Enter a number.')
            continue
        attempts += 1
        if g < secret:
            print('Too low')
        elif g > secret:
            print('Too high')
        else:
            print('Correct! Attempts: {}'.format(attempts))
            break
def dice_game():
    print('\n-- Dice Roll --')
    while True:
        inp = input('Press Enter to roll or type q to quit: ').strip().lower()
        if inp == 'q':
            break
        roll = random.randint(1, 6)
        print('You rolled:', roll)
        if input('Roll again? (y/n): ').strip().lower() != 'y':
            break
def games_submenu():
    while True:
        print('\n-- Games --')
        print('1. Rock Paper Scissors')
        print('2. Guessing Game')
        print('3. Dice Roll')
        print('4. Back to main menu')
        ch = input('Choose: ').strip()
        if ch == '1':
            rps_game()
            wait_enter()
        elif ch == '2':
            guessing_game()
            wait_enter()
        elif ch == '3':
            dice_game()
            wait_enter()
        elif ch == '4':
            break
        else:
            print('Invalid choice.')
def main_menu():
    while True:
        clear_screen()
        print('=== SCHOOL PROJECT MENU ===')
        print('1. Student Management')
        print('2. Library System')
        print('3. Inventory System')
        print('4. Tools')
        print('5. Games')
        print('6. Exit')
        choice = input('Choose: ').strip()
        if choice == '1':
            student_submenu()
        elif choice == '2':
            library_submenu()
        elif choice == '3':
            inventory_submenu()
        elif choice == '4':
            tools_submenu()
        elif choice == '5':
            games_submenu()
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')
            wait_enter()
if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print('\nExiting...')
