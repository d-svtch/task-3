from random import randint
class Address:

    def __init__(self, code, building, apartment):
        self.zip_code = code
        self.city = ["Москва", "Санкт-Петербург", "Омск", "Екатеринбург", "Владивосток", "Тверь", "Сочи", "Мурманск", "Великий Новгород", "Калининград", "Астрахань", "Псков", "Калуга", "Архангельск"]
        self.street = ["Ленина", "Главная", "Победы", "Центральная", "Молодёжная", "Школьная", "Советская", "Садовая ", "Гагарина", "Кирова", "Лесная", "Новая", "Набережная", "Зеленая"]
        self.building = building
        self.apartment = apartment

    def get_address(self):

        return (self.zip_code, self.city[randint(0,13)], self.street[randint(0,13)], self.building, self.apartment)
