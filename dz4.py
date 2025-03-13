basketball_players = {
    "ЛеБрон Джеймс": 206,
    "Майкл Джордан": 198,
    "Стефен Каррі": 188,
    "Шакіл О'Ніл": 216,
    "Святослав Михайлюк": 203
}

def add_player():
    name = input("Введіть ПІБ баскетболіста: ")
    if name in basketball_players:
        print("Такий гравець вже існує!")
        return
    try:
        height = int(input("Введіть зріст у см: "))
        if height <= 0:
            print("Зріст має бути більше 0!")
            return
        basketball_players[name] = height
        print(f"{name} додано до списку!")
    except ValueError:
        print("Невірний формат зросту!")

def remove_player():
    name = input("Введіть ПІБ для видалення: ").strip()
    if name in basketball_players:
        del basketball_players[name]
        print(f"{name} видалено зі списку!")
    else:
        print("Гравця не знайдено!")

def find_player():
    name = input("Введіть ПІБ для пошуку: ").strip()
    height = basketball_players.get(name)
    print(f"Зріст гравця {name}: {height} см" if height else "Гравця не знайдено!")

def edit_player():
    name = input("Введіть ПІБ для зміни зросту: ").strip()
    if name not in basketball_players:
        print("Гравця не знайдено!")
        return
    try:
        new_height = int(input("Введіть новий зріст (см): "))
        if new_height <= 0:
            print("Зріст має бути більше 0!")
            return
        basketball_players[name] = new_height
        print(f"Зріст для {name} оновлено!")
    except ValueError:
        print("Невірний формат зросту!")

def list_players():
    if not basketball_players:
        print("Список гравців порожній!")
        return
    print("\nСписок баскетболістів:")
    for name, height in basketball_players.items():
        print(f"{name}: {height} см")

print("Вітаємо в системі керування баскетболістами!")
print("команди для введення : add, remove, find, edit, list, exit")

while True:
    command = input("\nВведіть команду: ").strip().lower()
    
    if command == "exit":
        print("гудбай")
        break
    elif command == "add":
        add_player()
    elif command == "remove":
        remove_player()
    elif command == "find":
        find_player()
    elif command == "edit":
        edit_player()
    elif command == "list":
        list_players()
    else:
        print("err")