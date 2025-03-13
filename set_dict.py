from random import randint as rand
from tabnanny import check


# try:
#     for i in range(5):
#         a = rand(1,10)
#         b = rand(0,10)
#         print(f"{a} / {b} = {a/b:0.2f}")
#     raise Exception("End of program")
# except ZeroDivisionError as ex:
#     print(f"Error: {ex}")
# except Exception as ex:
#     print(f"{ex}")
# finally:
#     print("!!!")

#~~~~~~~~~~~~~~~ set ~~~~~~~~~~~~~~~~~~~
# lst = [rand(0,10) for i in range(10)]
# print(lst)
# #s = {1,2,3,2,4,3,5,4,6,7}
# s = set(lst)
# print(s)

# s = set()
#
# for i in range(10):
#     tmp = rand(0,10)
#     print(tmp, end=" ")
#     s.add(tmp)
# print()
# print(s)
#s.update({2,5,6,15})
# try:
#     s.remove(15)
# except Exception as ex:
#     print(f"Error: {ex}")
# key = 5
# if key in s:
#     s.remove(key)
#copy = s.copy()
#s.clear()
#s.discard(15)
# print(s.pop())
# print(s)
# for i in s:
#     print(i, end=" ")
# a = {1,2,3,4,5}
# b = {4,5,6,7}

#c = a.difference(b)
# c = a - b
#c = a.intersection(b)
# c = a & b
#c = a.union(b)
# c = a | b
#c = a.symmetric_difference(b)
# c = a ^ b
# print(c)

#d = {1:"one", 5:"five", 3:"three", 2:"two", 4:"four"}
#d = dict()

# print(d.get(5))

#print(3 in d)
#
# print(d.items())
# print(d.keys())
# print(d.values())
# for key in d:
#     print(f"{key} => {d[key]}")

# for key, value in d.items():
#     print(f"{key} => {value}")
#print(d)
#print(d.popitem())
#d.pop(3)
#print(d)


# task 1
def add_country(countries:set, country:str):
    countries.add(country)

def remove_country(countries:set, country:str):
    countries.discard(country)

def contains_country(countries:set, country:str)->bool:
    return country in countries

def find_countries(countries:set, pattern:str)->list[str]:
    # res = []
    # for country in countries:
    #     if pattern in country:
    #         res.append(country)
    # return res
    return [country for country in countries if pattern in country]

def menu(countries: set):
    while True:
        choice = input("show -> print all countries\n"
                       "add -> add new country\n"
                       "del -> remove country\n"
                       "find -> search countries\n"
                       "check -> check if exists\n"
                       "exit -> end program\n"
                       "make your choice: ")
        if choice == "add":
            country = input("enter the name of the country to add ->")
            add_country(countries, country)
        elif choice == "show":
            for country in countries:
                print(country)
        elif choice == "del":
            country = input("enter the name of the country to delete ->")
            remove_country(countries, country)
        elif choice == "find":
            pattern = input("enter the part of the name of country->")
            print(find_countries(countries, pattern))
        elif choice == "check":
            country = input("enter the name of the country to check ->")
            print(contains_country(countries, country))
        elif choice == "exit":
            break
        else:
            print("wrong command")

countries = {
    "Ukraine",
    "France",
    "Poland",
    "China",
    "Finland"
}
menu(countries)
# print(countries)
# #add_country(countries,"Poland")
# #remove_country(countries,"Poland")
# #print(contains_country(countries, "Poland"))
# print(find_countries(countries, "an"))
# print(countries)


