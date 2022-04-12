import csv
import json

book_dict = {}
books_list = []

user_dict = {}
user_list = []

BOOK_HEADER = ('title', 'author', 'pages', 'genre')
JSON_HEADER = ('name', 'gender', 'address', 'age', 'books')

with open('../examples/data/books.csv', newline='') as f1, open('../examples/data/users.json', newline='') as f2:
    reader1 = csv.DictReader(f1)
    header = next(reader1)

    for row in reader1:
        book_dict_row = (row['Title'], row['Author'], row['Pages'], row['Genre'])
        book_dict = dict(zip(BOOK_HEADER, book_dict_row))
        books_list.append(book_dict)

    users = json.loads(f2.read())
    for user in users:
        user_dict_row = (user['name'], user['gender'], user['address'], user['age'], [])
        user_dict = dict(zip(JSON_HEADER, user_dict_row))
        user_list.append(user_dict)

    number_of_users = len(user_list)
    usr_count = 0

    for book in books_list:
        user_list[usr_count]["books"] = book
        usr_count += 1
        if usr_count >= number_of_users:
            usr_count = 0

print(user_list)

with open("data_reference.json", 'w') as f:
    s = json.dumps(user_list, indent=4)
    f.write(s)
