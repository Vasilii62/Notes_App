import json
import datetime
import os
import sys

FILENAME = "notes.json"


def load_notes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
        return data
    else:
        return []


def save_notes(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file)


def add_note():
    notes = load_notes()
    note = {}

    note["id"] = len(notes) + 1
    note["title"] = input("Enter note title: ")
    note["body"] = input("Enter note body: ")
    note["created_at"] = str(datetime.datetime.now())
    note["updated_at"] = str(datetime.datetime.now())

    notes.append(note)
    save_notes(notes)
    print("Note added successfully.")


def view_notes():
    notes = load_notes()

    if len(notes) == 0:
        print("No notes found.")
    else:
        print("ID\tTitle")
        for note in notes:
            print(f"{note['id']}\t{note['title']}")


def view_note():
    notes = load_notes()

    if len(notes) == 0:
        print("No notes found.")
    else:
        try:
            note_id = int(input("Enter note ID: "))
            note = next((note for note in notes if note["id"] == note_id), None)
            if note is None:
                print("Note not found.")
            else:
                print(f"Title: {note['title']}")
                print(f"Body: {note['body']}")
                print(f"Created at: {note['created_at']}")
                print(f"Updated at: {note['updated_at']}")
        except ValueError:
            print("Invalid input. Please enter a valid note ID.")


def edit_note():
    notes = load_notes()

    if len(notes) == 0:
        print("No notes found.")
    else:
        try:
            note_id = int(input("Enter note ID: "))
        except ValueError:
            print("Invalid note ID.")
            return

        note = next((note for note in notes if note["id"] == note_id), None)
        if note is None:
            print("Note not found.")
        else:
            note["title"] = input("Enter note title: ")
            note["body"] = input("Enter note body: ")
            note["updated_at"] = str(datetime.datetime.now())

            save_notes(notes)
            print("Note updated successfully.")


def delete_note():
    notes = load_notes()  # Получаем список заметок
    note_id = input("Введите ID заметки, которую нужно удалить: ")

    try:
        note_id = int(note_id)
    except ValueError:
        print("Ошибка: ID должен быть целым числом")
        return

    note_found = False

    # Проходимся по всем заметкам и удаляем заметку с заданным ID
    for i, note in enumerate(notes):
        if note["id"] == note_id:
            notes.pop(i)
            note_found = True
            break

    if not note_found:
        print("Заметка не найдена")
    else:
        # Обновляем ID всех оставшихся заметок, начиная с 1
        for i, note in enumerate(notes):
            note["id"] = i + 1

        save_notes(notes)  # Сохраняем обновленный список заметок в файл
        print("Заметка успешно удалена")

def search_note_by_title():
    notes = load_notes()
    search_term = input("Enter search term: ")
    matching_notes = [note for note in notes if search_term.lower() in note["title"].lower()]
    if len(matching_notes) == 0:
        print("No matching notes found.")
    else:
        print("ID\tTitle")
        for note in matching_notes:
            print(f"{note['id']}\t{note['title']}")

def search_notes_by_time():
    notes = load_notes()
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return

    filtered_notes = []

    for note in notes:
        created_at = datetime.datetime.strptime(note["created_at"], "%Y-%m-%d %H:%M:%S.%f")
        if start_date <= created_at <= end_date:
            filtered_notes.append(note)

    if len(filtered_notes) == 0:
        print("No notes found for the given date range.")
    else:
        print(f"Notes found for the date range {start_date.date()} to {end_date.date()}:")
        print("ID\tTitle\tCreated At\tUpdated At")
        for note in filtered_notes:
            print(f"{note['id']}\t{note['title']}\t{note['created_at']}\t{note['updated_at']}")


def exit():
    sys.exit(0)

def sort_notes_by_titles():
    notes = load_notes()
    sorted_notes = sorted(notes, key=lambda x: x['title'])
    if len(sorted_notes) == 0:
        print("No notes found.")
    else:
        print("ID\tTitle")
        for note in sorted_notes:
            print(f"{note['id']}\t{note['title']}")

def sort_notes_by_date():
    notes = load_notes()
    sorted_notes = sorted(notes, key=lambda x: x['created_at'])
    if len(sorted_notes) == 0:
        print("No notes found.")
    else:
        print("ID\tTitle\tCreated At\tUpdated At")
        for note in sorted_notes:
            print(f"{note['id']}\t{note['title']}\t{note['created_at']}\t{note['updated_at']}")

def main():
    while True:
        print("\nNote App\n")
        print("1. Add Note")
        print("2. View Notes")
        print("3. View Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Search Note by Title")
        print("7. Search Note by Time")
        print("8. Sort Notes by Titles")
        print("9. Sort Notes by Date")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            search_note_by_title()
        elif choice == "7":
            search_notes_by_time()
        elif choice == "8":
            sort_notes_by_titles()
        elif choice == "9":
            sort_notes_by_date()
        elif choice == "10":
            exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
