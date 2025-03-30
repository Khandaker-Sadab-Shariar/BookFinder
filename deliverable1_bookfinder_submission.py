
books = [
    {"title": "Pather Panchali", "author": "Bibhutibhushan Bandyopadhyay", "year": 1929, "genre": "Fiction"},
    {"title": "Chokher Bali", "author": "Rabindranath Tagore", "year": 1903, "genre": "Romance"},
    {"title": "Devi Chaudhurani", "author": "Bankim Chandra Chattopadhyay", "year": 1884, "genre": "Historical"},
    {"title": "Gitanjali", "author": "Rabindranath Tagore", "year": 1910, "genre": "Poetry"},
    {"title": "Karagar", "author": "Humayun Ahmed", "year": 2001, "genre": "Mystery"},
    {"title": "Shesher Kobita", "author": "Rabindranath Tagore", "year": 1929, "genre": "Romance"},
    {"title": "Lalon Fakir", "author": "Lalon", "year": "19th Century", "genre": "Spiritual"},
    {"title": "Aparajito", "author": "Bibhutibhushan Bandyopadhyay", "year": 1932, "genre": "Fiction"},
    {"title": "Parthib", "author": "Selina Hossain", "year": 1994, "genre": "Drama"},
    {"title": "Madhushala", "author": "Harivansh Rai Bachchan", "year": 1935, "genre": "Poetry"},
    {"title": "Ekattorer Dinguli", "author": "Jahanara Imam", "year": 1986, "genre": "Memoir"},
    {"title": "Oshomapto Attojiboni", "author": "Sheikh Mujibur Rahman", "year": 2012, "genre": "Autobiography"},
    {"title": "Aguner Poroshmoni", "author": "Humayun Ahmed", "year": 1994, "genre": "Historical"},
    {"title": "Dipu Number Two", "author": "Muhammed Zafar Iqbal", "year": 1984, "genre": "Children"},
    {"title": "Chander Pahar", "author": "Bibhutibhushan Bandyopadhyay", "year": 1937, "genre": "Adventure"}
]

print("Book Finder")
print("1 - Search by Book Name")
print("2 - Search by Author Name")
print("3 - Exit")

choice = input("Enter choice: ")

if choice == "1":
    title = input("Book name: ")
    found = False
    for b in books:
        if title.lower() in b["title"].lower():
            print("Found: " + b["title"] + " by " + b["author"])
            found = True
    if found == False:
        print("Not found")
elif choice == "2":
    author = input("Author name: ")
    found = False
    for b in books:
        if author.lower() in b["author"].lower():
            print("Found: " + b["title"] + " by " + b["author"])
            found = True
    if found == False:
        print("Not found")
elif choice == "3":
    print("Bye")
else:
    print("Wrong choice")