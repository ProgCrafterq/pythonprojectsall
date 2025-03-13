#Task1
# basketball_players = {
#     "Michael Jordan": 198,
#     "LeBron James": 206,
#     "Kobe Bryant": 198,
#     "Shaquille O'Neal": 216,
#     "Stephen Curry": 188
# }

# def show_all_players(players):
#     print("\nAll players:")
#     if not players:
#         print("Empty")
#     else:
#         for name, height in players.items():
#             print(f"{name} - {height} cm")

# def add_player(players):
#     name = input("Name: ")
#     if name in players:
#         print("Already exists")
#         return
#     try:
#         height = int(input("Height (cm): "))
#         players[name] = height
#         print("Added")
#     except ValueError:
#         print("Height must be number")

# def delete_player(players):
#     name = input("Name: ")
#     if name in players:
#         del players[name]
#         print("Deleted")
#     else:
#         print("Not found")

# def find_player(players):
#     name = input("Name: ")
#     if name in players:
#         print(f"{name} - {players[name]} cm")
#     else:
#         print("Not found")

# def update_player(players):
#     name = input("Name: ")
#     if name in players:
#         try:
#             height = int(input("New height (cm): "))
#             players[name] = height
#             print("Updated")
#         except ValueError:
#             print("Height must be number")
#     else:
#         print("Not found")

# def menu():
#     print("\nBasketball Players Info")
#     print("1. Show all")
#     print("2. Add player")
#     print("3. Delete player")
#     print("4. Find player")
#     print("5. Update player")
#     print("0. Exit")
    
#     choice = input("Choice: ")
    
#     if choice == "1":
#         show_all_players(basketball_players)
#         menu()
#     elif choice == "2":
#         add_player(basketball_players)
#         menu()
#     elif choice == "3":
#         delete_player(basketball_players)
#         menu()
#     elif choice == "4":
#         find_player(basketball_players)
#         menu()
#     elif choice == "5":
#         update_player(basketball_players)
#         menu()
#     elif choice == "0":
#         print("Bye")
#         return
#     else:
#         print("Wrong choice")
#         menu()

# menu()



#Task 2
# english_french = {
#     "hello": "bonjour",
#     "goodbye": "au revoir",
#     "thank you": "merci",
#     "please": "s'il vous plaît",
#     "sorry": "désolé"
# }

# def show_all(d):
#     print("\nDictionary:")
#     if not d:
#         print("Empty")
#     else:
#         for eng, fr in d.items():
#             print(f"{eng} - {fr}")

# def add_word(d):
#     eng = input("English word: ").lower()
#     if eng in d:
#         print("Already exists")
#         return
#     fr = input("French word: ")
#     d[eng] = fr
#     print("Added")

# def delete_word(d):
#     eng = input("English word: ").lower()
#     if eng in d:
#         del d[eng]
#         print("Deleted")
#     else:
#         print("Not found")

# def find_word(d):
#     eng = input("English word: ").lower()
#     if eng in d:
#         print(f"{eng} - {d[eng]}")
#     else:
#         print("Not found")

# def update_word(d):
#     eng = input("English word: ").lower()
#     if eng in d:
#         fr = input("New French word: ")
#         d[eng] = fr
#         print("Updated")
#     else:
#         print("Not found")

# def menu():
#     print("\nEnglish-French Dictionary")
#     print("1. Show all")
#     print("2. Add word")
#     print("3. Delete word")
#     print("4. Find word")
#     print("5. Update word")
    
#     choice = input("Choice: ")
    
#     if choice == "1":
#         show_all(english_french)
#         menu()
#     elif choice == "2":
#         add_word(english_french)
#         menu()
#     elif choice == "3":
#         delete_word(english_french)
#         menu()
#     elif choice == "4":
#         find_word(english_french)
#         menu()
#     elif choice == "5":
#         update_word(english_french)
#         menu()
#     else:
#         print("err")
#         menu()

# menu()


#Task3

# emps = {
#     "Shevchenko Volodymyr Olexandrovych": {
#         "ph": "+380993344556",
#         "em": "shevchenko@company.com",
#         "pos": "Developer",
#         "rm": "303",
#         "sk": "volodymyr.shevchenko"
#     },
#     "Zheleikin Sasha Sergiyovych": {
#         "ph": "+380994455667",
#         "em": "zheleikin@company.com",
#         "pos": "Analyst",
#         "rm": "404",
#         "sk": "sasha.zheleikin"
#     }
# }

# def show_all(e):
#     print("\nAll employees:")
#     if not e: print("Empty"); return
#     for n, i in e.items():
#         print(f"\nName: {n}\nPhone: {i['ph']}\nEmail: {i['em']}\nPos: {i['pos']}\nRoom: {i['rm']}\nSkype: {i['sk']}")

# def add(e):
#     n = input("Name: ")
#     if n in e: print("Exists"); return
#     e[n] = {
#         "ph": input("Phone: "),
#         "em": input("Email: "),
#         "pos": input("Pos: "),
#         "rm": input("Room: "),
#         "sk": input("Skype: ")
#     }
#     print("Added")

# def delete(e):
#     n = input("Name: ")
#     print("Deleted" if e.pop(n, None) else "Not found")

# def find(e):
#     n = input("Name: ")
#     if n in e:
#         i = e[n]
#         print(f"\nName: {n}\nPhone: {i['ph']}\nEmail: {i['em']}\nPos: {i['pos']}\nRoom: {i['rm']}\nSkype: {i['sk']}")
#     else:
#         print("Not found")

# def update(e):
#     n = input("Name: ")
#     if n not in e: print("Not found"); return
#     print("1.Phone 2.Email 3.Pos 4.Room 5.Skype")
#     c = input("Choice: ")
#     if c in "12345":
#         k = ["ph", "em", "pos", "rm", "sk"][int(c) - 1]
#         e[n][k] = input(f"New {k}: ")
#         print("Updated")
#     else:
#         print("Err")

# def menu():
#     print("\n1.Show 2.Add 3.Del 4.Find 5.Upd 0.Exit")
#     choice = input("->")
#     if choice == "1":
#         show_all(emps)
#         menu()
#     elif choice == "2":
#         add(emps)
#         menu()
#     elif choice == "3":
#         delete(emps)
#         menu()
#     elif choice == "4":
#         find(emps)
#         menu()
#     elif choice == "5":
#         update(emps)
#         menu()
#     elif choice == "0":
#         print("Bye")
#     else:
#         print("Err")
#         menu()

# menu()


# Task 4

books = {
    "The Stars Beyond": {
        "author": "Alaric Raynor",
        "genre": "Space Opera",
        "year": 2045,
        "pages": 412,
        "publisher": "Galactic Press"
    },
    "Shadows of the Network": {
        "author": "Ava Sterling",
        "genre": "Cyberpunk",
        "year": 2030,
        "pages": 376,
        "publisher": "Neon Horizons"
    }
}


def show_books(books_dict):
    print("\nBook Collection:")
    if not books_dict:
        print("Empty collection")
    else:
        for title, info in books_dict.items():
            print(f"\nTitle: {title}")
            print(f"Author: {info['author']}")
            print(f"Genre: {info['genre']}")
            print(f"Year: {info['year']}")
            print(f"Pages: {info['pages']}")
            print(f"Publisher: {info['publisher']}")

def add_book(books_dict):
    title = input("Enter book title: ")
    if title in books_dict:
        print(f"'{title}' already exists!")
        return
    
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    
    try:
        year = int(input("Enter year: "))
        pages = int(input("Enter number of pages: "))
    except ValueError:
        print("Err")
        return
    
    publisher = input("Enter publisher: ")
    
    books_dict[title] = {
        "author": author,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher
    }
    
    print(f"'{title}' added successfully!")

def delete_book(books_dict):
    title = input("Enter book title to delete: ")
    if title in books_dict:
        del books_dict[title]
        print(f"'{title}' deleted successfully.")
    else:
        print(f"'{title}' not found.")

def search_book(books_dict):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    print("3. Genre")
    print("4. Year")
    print("5. Publisher")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        title = input("Enter title: ")
        if title in books_dict:
            info = books_dict[title]
            print(f"\nTitle: {title}")
            print(f"Author: {info['author']}")
            print(f"Genre: {info['genre']}")
            print(f"Year: {info['year']}")
            print(f"Pages: {info['pages']}")
            print(f"Publisher: {info['publisher']}")
        else:
            print(f"'{title}' not foundЖ")
    
    elif choice == "2":
        author = input("Enter author: ")
        found = False
        for title, info in books_dict.items():
            if info["author"] == author:
                if not found:
                    print(f"\nBooks by '{author}':")
                    found = True
                print(f"\nTitle: {title}")
                print(f"Genre: {info['genre']}")
                print(f"Year: {info['year']}")
                print(f"Pages: {info['pages']}")
                print(f"Publisher: {info['publisher']}")
        if not found:
            print(f"No books found by '{author}'.")
    
    elif choice == "3":
        genre = input("Enter genre: ")
        found = False
        for title, info in books_dict.items():
            if info["genre"] == genre:
                if not found:
                    print(f"\nBooks of genre '{genre}':")
                    found = True
                print(f"\nTitle: {title}")
                print(f"Author: {info['author']}")
                print(f"Year: {info['year']}")
                print(f"Pages: {info['pages']}")
                print(f"Publisher: {info['publisher']}")
        if not found:
            print(f"No books in '{genre}' genre.")
    
    elif choice == "4":
        try:
            year = int(input("Enter year: "))
            found = False
            for title, info in books_dict.items():
                if info["year"] == year:
                    if not found:
                        print(f"\nBooks from {year}:")
                        found = True
                    print(f"\nTitle: {title}")
                    print(f"Author: {info['author']}")
                    print(f"Genre: {info['genre']}")
                    print(f"Pages: {info['pages']}")
                    print(f"Publisher: {info['publisher']}")
            if not found:
                print(f"No books from {year}.")
        except ValueError:
            print("Err")
    
    elif choice == "5":
        publisher = input("Enter publisher: ")
        found = False
        for title, info in books_dict.items():
            if info["publisher"] == publisher:
                if not found:
                    print(f"\nBooks from publisher '{publisher}':")
                    found = True
                print(f"\nTitle: {title}")
                print(f"Author: {info['author']}")
                print(f"Genre: {info['genre']}")
                print(f"Year: {info['year']}")
                print(f"Pages: {info['pages']}")
            if not found:
                print(f"No books from '{publisher}' publisher.")
    
    else:
        print("Invalid choice. Try again.")

def update_book(books_dict):
    title = input("Enter title to update: ")
    if title in books_dict:
        print("Select what to update:")
        print("1. Author")
        print("2. Genre")
        print("3. Year")
        print("4. Pages")
        print("5. Publisher")
        
        choice = input("нour choice: ")
        
        if choice == "1":
            books_dict[title]["author"] = input("Enter new author: ")
        elif choice == "2":
            books_dict[title]["genre"] = input("Enter new genre: ")
        elif choice == "3":
            try:
                books_dict[title]["year"] = int(input("Enter new year: "))
            except ValueError:
                print("Err")
                return
        elif choice == "4":
            try:
                books_dict[title]["pages"] = int(input("Enter new number of pages: "))
            except ValueError:
                print("Error! Pages must be a number.")
                return
        elif choice == "5":
            books_dict[title]["publisher"] = input("Enter new publisher: ")
        else:
            print("Invalid choice.")
            return
        
        print(f"'{title}' updated success.")
    else:
        print(f"'{title}' not found.")

def menu():
    print("\n'Book Collection' Program")
    print("1. Show all books")
    print("2. Add new book")
    print("3. Delete book")
    print("4. Search book")
    print("5. Update book info")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        show_books(books)
        menu()
    elif choice == "2":
        add_book(books)
        menu()
    elif choice == "3":
        delete_book(books)
        menu()
    elif choice == "4":
        search_book(books)
        menu()
    elif choice == "5":
        update_book(books)
        menu()
    else:
        print("incorect choice")
        menu()

menu()


