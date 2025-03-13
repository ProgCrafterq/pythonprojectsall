countries = {"Ukraine", "Poland", "Turkey", "Germany", "France"}

def add_country(countries: set, country: str):
    countries.add(country)
    print(f"{country} added")

def remove_country(countries: set, country: str):
    if country in countries:
        countries.remove(country)
        print(f"{country} has been deleted.")
    else:
        print("сountry isn't there")

def search_countries(countries: set, query: str):
    found = [c for c in countries if query in c]
    if found:
        print("Found countries:", ", ".join(found))
    else:
        print("no countries found.")

def check_country(countries: set, country: str):
    if country in countries:
        print(f"{country} is in the set.")
    else:
        print(f"{country} is not in the set.")

print("\nM")
print("+")
print("-")
print("search")
print("is")
choice = input("Select=== ")

if choice == "1":
    add_country(countries, input("Enter name: "))
elif choice == "2":
    remove_country(countries, input("Enter name for deleting: "))
elif choice == "3":
    search_countries(countries, input("Enter characters to search: "))
elif choice == "4":
    check_country(countries, input("Enter country name to check: "))
else:
    print("Error")




    
