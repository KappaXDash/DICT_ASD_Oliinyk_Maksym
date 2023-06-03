import random
from main_modul import Spider


class Generator:
    @staticmethod
    def generate_spider() -> Spider:
        names = ["Бока", "Жока", "Боря", "Коля", "Міша", "Костя", "Дося", "Мася", "Куся", "Лопата"]
        breeds = ["Комахоїдні", "Латродектиди", "Павуки-краби", "Лінькові павуки", "Таргани", "Голіцинтові", "Бабки", "Тарантули", "Павуки-скакуни"]
        categories = ["Аранеоморфні", "Мігаломорфні"]
        areals = ["Ліси та поля", "Поля та луки", "Пустелі", "Поля"]
        colors = ["чорний", "коричневий", "білий", "сірий", "рудий"]

        # Генерувати випадкові значення для кожної властивості павука
        name = random.choice(names)
        species = random.choice(breeds)
        category = random.choice(categories)
        areal = random.choice(areals)
        weight = round(random.uniform(150, 1000), 2)  # вага від 150 до 1000 кг
        color = random.choice(colors)

        # Створити об'єкт класу Spider з випадковими властивостями
        spider = Spider(name, species, category, areal, weight, color)
        return spider


# Створення випадкового павука
random_spider = Generator.generate_spider()

# Вивід повідомлення про випадкового павука
message = random_spider.generate_message()
print(message)


def generate_1000() -> list:
    generator = Generator()
    plist = []
    for _ in range(1000):
        plist.append(generator.generate_spider())
    return plist


def generate_10_000() -> list:
    generator = Generator()
    plist = [generator.generate_spider() for _ in range(10000)]
    return plist


def abstract_object():
    return None
