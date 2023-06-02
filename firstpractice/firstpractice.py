class Spider:
    def init(self, name, size, category, areal, weight, color):
        self.name = name
        self.size = size
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

    def generate_message(self):
        category_areal = self.determine_category_areal()
        areal_category = self.determine_areal_category()
        message = f"Павук {self.name} розміру {self.size}, що відноситься до {category_areal} {areal_category} категорії, важить {self.weight} і має забарвлення {self.color}."
        return message

# Запит даних у користувача
name = input("Введіть ім'я павука: ")
size = input("Введіть розмір павука: ")
category = input("Введіть категорію павука (Аранеоморфні/Мігаломорфні): ")
areal = input("Введіть ареал павука (Ліси та поля/Поля та луки/Пустелі/Поля): ")
weight = input("Введіть вагу павука: ")
color = input("Введіть забарвлення павука: ")

# Створення об'єкту класу Spider
spider = Spider(name, size, category, areal, weight, color)

# Вивід повідомлення про павука
message = spider.generate_message()
print(message)