fruits = ['apple', 'banana', 'cherry', 'date']
fruits.append('elderberry')
fruits.remove('banana')
print(fruits)

student = {"name": "John Doe", "age": 25, "major": "computer scinece"}
print(student)
student['major'] = "Electrical Engineering"
student.update({"year":"Senior"})
print(student.keys())
print(student.values())

books = [
    {"title":"Friedhof der Kuscheltiere", "author":"Stehphen King", "year": "1993"},
    {"title":"Edda", "author":"Skalden", "year":"400"},
    {"title":"Jackie hat Hirn erbrochen", "author":"Jörg Nießen", "year": "2021"}]

print(books[1]["title"])
print(books[2]["year"])

for book in books:
    print(f'{book["title"]} von {book["author"]}')

courses = {"courses": [{"math":["Andreas"]}, {"physics":[]}, {"history":[]}]}

courses["courses":["math"].append("Elisabeth", "Torben", "Dennis", "Fabienne", "Andre")]
print(courses["courses"]["math"])



