from .library import Library


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. View All Books")
        print("7. Save & Exit")
        print("0. Exit Without Saving")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            success, msg = library.add_book(title, author, isbn)
            print(msg)

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            success, msg = library.register_member(name, member_id)
            print(msg)

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            success, msg = library.borrow_book(member_id, isbn)
            print(msg)

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            success, msg = library.return_book(member_id, isbn)
            print(msg)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            results = library.search_books(keyword)
            for book in results:
                print(book)

        elif choice == "6":
            for book in library.books.values():
                print(book)

        elif choice == "7":
            library.save_data()
            print("Data saved successfully.")
            break

        elif choice == "0":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
