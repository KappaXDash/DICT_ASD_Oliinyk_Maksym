class Spider:
    def __repr__(self) -> str:
        return f"Spider(name={self.name}, breed={self.species}, category={self.category}, areal={self.areal}, weight={self.weight},color={self.color})"


    def __init__(self, name: str, species: str, category: str, areal: str, weight: float, color: str):
        self.name = name
        self.species = species
        self.category = category
        self.areal = areal
        self.weight = weight
        self.color = color

    def determine_category_areal(self):
        if self.category == "Аранеоморфні":
            if self.size in ["Комахоїдні", "Латродектиди", "Павуки-краби", "Лінькові павуки"]:
                return "Лінькові"
            else:
                return "невідомою"
        elif self.category == "Мігаломорфні":
            if self.size in ["Таргани", "Голіцинтові", "Бабки"]:
                return "Бабками"
            elif self.size in ["Тарантули", "Павуки-скакуни"]:
                return "рисистими"
            else:
                return "невідомою"

    def determine_areal_category(self):
        if self.areal == "Ліси та поля":
            return "Орбітальні павуки"
        elif self.areal == "Поля та луки":
            return "Полівкові"
        elif self.areal == "Пустелі":
            return "Тарганові"
        elif self.areal == "Поля":
            return "Вовківі"
        else:
            return "невідомо"

    def generate_message(self) -> str:
        category_areal = self.determine_category_areal()
        areal_category = self.determine_areal_category()
        message = f"Павук {self.name} виду {self.breed}, що відноситься до {category_areal} {areal_category} видів, важить {self.weight} і має забарвлення {self.color}."
        return message

# Запрос данных у пользователя
name = input("Введіть ім'я павука: ")
spices = input("Введіть вид павука: ")
category = input("Введіть категорію павука (Аранеоморфні/Мігаломорфні): ")
areal = input("Введіть ареал павука (Ліси та поля/Поля та луки/Пустелі/Поля): ")
weight = float(input("Введіть вагу павука: "))
color = input("Введіть забарвлення павука: ")

# Створення об'єкту класу Spider
spider = Spider(name, spices, category, areal, weight, color)

# Вивід повідомлення про павука
message = spider.generate_message()
print(message)
#  вага не є числом
spider1 = Spider("Павло", "Тарганові", "Аранеоморфні", "Пустелі", "1000", "червоне")

#  порода невідома
spider1 = Spider("Микола", "невідомий вид", "Аранеоморфні", "Поля", 500, "біле")