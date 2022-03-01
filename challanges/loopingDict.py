fruitcompanies= [{"name":"Zesty","employees":["Bryan", "Colin", "Erik", "Greg", "John"]},
                 {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Chad"]},
                 {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                 {"name":"JuiceGrove","employees":["Tim", "Travis", "Trung"]}]
#Write a for loop that returns all the employees from the company you "work" for!

for x in fruitcompanies[1]["employees"]:
    print(x)
#• Ask a user to choose a company. Return the employees that belong to that group.

#input("please enter a company")
#for x in fruitcompanies:
choice=input("Choose a company:Zesty, Ripe.ly, FruitBee, JuiceGrove\n>")
for company in fruitcompanies:
    if choice == company["name"]:
        print(company["employees"])
#Ask a user to choose a company (Zesty, Ripe.ly, FruitBee, or JuiceGrove) and return the employees... but DO NOT return "Chad" He got fired this morning.
#make a menu of companies to choose from
fruitcompanies[1][employees"].remove("Chad")
x=0
for company in fruitcompanies:
    x += 1
    print(f"{x}.{company['name']}")

    choice =input("Choose your company!\n>"))
    print(fruitcompanies[choice-1]["employees"]):
            if x != "Chad":
            print(x)
