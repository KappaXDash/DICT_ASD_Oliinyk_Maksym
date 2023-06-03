import random
from typing import List, Union

class Spider:
    def __init__(self, name: str, species: str, category: str, areal: str, weight: float, color: str):

        self.name = name
        self.species = species
        self.category = category
        self.areal = areal
        self.weight = weight
        self.color = color

    def determine_category_areal(self) -> str:
        if self.category == "Аранеоморфні":
            if self.species in ["Комахоїдні", "Латродектиди", "Павуки-краби", "Лінькові павуки"]:
                return "Лінькові"
            else:
                return "невідомою"
        elif self.category == "Мігаломорфні":
            if self.species in ["Таргани", "Голіцинтові", "Бабки"]:
                return "важковозами"
            elif self.species in ["Тарантули", "Павуки-скакуни"]:
                return "Бабками"
            else:
                return "рисистими"

    def determine_areal_category(self) -> str:
        if self.areal == "Ліси та поля":
            return "Орбітальні павуки"
        elif self.areal == "Поля та луки":
           return "Полівкові"
        elif self.areal == "Пустелі":
            return "Тарганові"
        elif self.areal == "Поля":
            return "Вовківі"
        else:
            return "невідомим"

    def generate_message(self) -> str:
        category_areal = self.determine_category_areal()
        areal_category = self.determine_areal_category()
        message = f"Павук {self.name} виду {self.species}, що відноситься до {category_areal} {areal_category} , важить {self.weight} і має забарвлення {self.color}."
        return message

class Generator:
    @staticmethod
    def generate_spider() -> Spider:
        names = ["Бока", "Жока", "Боря", "Коля", "Міша", "Костя", "Дося", "Мася", "Куся", "Лопата"]
        species = ["Комахоїдні", "Латродектиди", "Павуки-краби", "Лінькові павуки", "Таргани", "Голіцинтові", "Бабки","Тарантули", "Павуки-скакуни"]
        categories = ["Аранеоморфні", "Мігаломорфні"]
        areals = ["Ліси та поля", "Поля та луки", "Пустелі", "Поля"]
        colors = ["чорний", "коричневий", "білий", "сірий", "рудий"]

        # Генерувати випадкові значення для кожної властивості павука
        name = random.choice(names)
        species = random.choice(species)
        category = random.choice(categories)
        areal = random.choice(areals)
        weight = round(random.uniform(150, 1000), 2)  # вага від 150 до 1000 грам
        color = random.choice(colors)

        # Створити об'єкт класу Spider з випадковими властивостями
        spider = Spider(name, species, category, areal, weight, color)
        return spider
# Створення випадкового павука
random_spider = Generator.generate_spider()

# Вивід повідомлення про випадкового павука
message = random_spider.generate_message()
print(message)


def generate_1000(self) -> list:

    plist = list()
    for i in range(1000):
        plist.append(self.generate_spider())
    return plist


def generate_10_000(self) -> list:
    plist = [self.generate_spider() for i in range(10000)]
    return plist