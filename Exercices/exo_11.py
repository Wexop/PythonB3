import json

import requests



class Personne:
    def __init__(self, genre, nom, age, city, country):
        self.gender = genre
        self.name = nom
        self.age: int = age
        self.city = city
        self.country = country

    def register(self):
        f = open('personne.txt', 'a')
        json.dump({"age": self.age, "genre": self.gender, "nom": self.name, "ville": self.city, "pays": self.country}, f)
        f.write('\n')
        f.close()

result = requests.get('https://randomuser.me/api').json()['results']
p = Personne(result[0]['gender'], result[0]['name']['first'], result[0]['dob']['age'], result[0]['location']['city'], result[0]['location']['country'])
p.register()