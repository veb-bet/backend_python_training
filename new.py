class Car:
    pass  # Пустой класс
my_car = Car()  # Создаем объект класса Car

class Car:
    def __init__(self, make, model):
        self.make = make  # Атрибут
        self.model = model  # Атрибут

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):  # Наследует от Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Вызов конструктора родительского класса
        self.model = model

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0  # Закрытый атрибут
    def accelerate(self):
        self.__speed += 10

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Выводит: Woof, Meow

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __str__(self):
        return f"{self.make} {self.model}"
car = Car("Toyota", "Corolla")
print(car)  # Выведет: Toyota Corolla

class Car:
    def __init__(self, make, model):
        self.make = make  # Открытый атрибут
        self.model = model  # Открытый атрибут
        self.__speed = 0  # Закрытый атрибут, доступ к которому можно получить только через методы
    # Метод для увеличения скорости
    def accelerate(self):
        self.__speed += 10
        print(f"Speed is now {self.__speed} km/h")
    # Метод для получения текущей скорости
    def get_speed(self):
        return self.__speed
# Создаем объект Car
my_car = Car("Toyota", "Corolla")
# Используем методы для работы с закрытым атрибутом
my_car.accelerate()  # Увеличивает скорость на 10
my_car.accelerate()  # Увеличивает скорость на еще 10
# Получаем текущую скорость с помощью метода
print(f"Current speed: {my_car.get_speed()} km/h")

class Animal:
    def speak(self):
        pass  # Это пустой метод, его нужно переопределить в дочерних классах
class Dog(Animal):
    def speak(self):
        return "Woof"  # Реализация для собаки
class Cat(Animal):
    def speak(self):
        return "Meow"  # Реализация для кошки
# Создаем объекты разных классов
animals = [Dog(), Cat()]
# Используем метод speak() для разных объектов
for animal in animals:
    print(animal.speak())  # Выводит: Woof, Meow