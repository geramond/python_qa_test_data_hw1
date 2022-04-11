import csv
import json

book_dict = {}
books_list = []

user_dict = {}
user_list = []

data = []

with open('../examples/data/books.csv', newline='') as f1, open('../examples/data/users.json', newline='') as f2:
    reader1 = csv.reader(f1)
    header = next(reader1)

    for row in reader1:
        book_dict['title'] = row[0]
        book_dict['author'] = row[1]
        book_dict['pages'] = row[3]
        book_dict['genre'] = row[2]
        books_list.append(book_dict)

    users = json.loads(f2.read())
    for user in users:
        user_dict['name'] = user['name']
        user_dict['gender'] = user['gender']
        user_dict['address'] = user['address']
        user_dict['age'] = user['age']
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
