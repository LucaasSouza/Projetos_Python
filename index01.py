from requests import get

class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f"Hi, my name is {self.name}, and I use '{self.username}' as username. My current email is {self.email}."

listUsers = []
reqUsers = get('https://jsonplaceholder.typicode.com/users')
if reqUsers.status_code != 200:
    print(f'Erro na requisição! ERROR {reqUsers.status_code}')
else:
    i = 0
    data = reqUsers.json()

    while i != 10:
        p1 = User(data[i]["name"], data[i]["username"], data[i]["email"])
        listUsers.append(p1)
        i += 1

    for i in listUsers:
        print(i)