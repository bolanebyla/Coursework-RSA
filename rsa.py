import random
from pprint import pprint

table = {1: 97, 2: 89, 3: 83, 4: 79, 5: 73, 6: 71, 7: 67, 8: 61, 9: 59, 10: 53,
         11: 47, 12: 43, 13: 41, 14: 37, 15: 31, 16: 29, 17: 23, 18: 19, 19: 17,
         20: 13, 21: 11, 22: 7, 23: 5, 24: 3, 25: 2}

letters = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8,
           'З': 9, 'И': 10, 'Й': 11, 'К': 12, 'Л': 13, 'М': 14, 'Н': 15, 'О': 16,
           'П': 17, 'Р': 18, 'С': 19, 'Т': 20, 'У': 21, 'Ф': 22, 'Х': 23, 'Ц': 24,
           'Ч': 25, 'Ш': 26, 'Щ': 27, 'Ъ': 28, 'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32,
           'Я': 33}


def get_key(my_dict, val):
    """возвращает ключ словаря по значению"""
    for key, value in my_dict.items():
        if val == value:
            return key
    raise ('Key does not exist')


def get_gcd(a: int, b: int) -> int:
    """Возвращает наибольший общий делитель"""
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    return gcd


class RSA:
    def __init__(self, number: int, last_name: str):
        self.p = table[int(number)]
        self.last_name = last_name
        self._set_last_name_in_numeric_form()
        self._set_q()
        self._set_n()
        self._set_e()
        self.set_d()

    def _set_last_name_in_numeric_form(self) -> list:
        """возвращает список номеров букв фамилии"""
        self.last_name_in_numeric_form = [letters[letter.upper()] for letter in self.last_name]

    def _set_q(self) -> int:
        """устанавливает значение q"""
        self.sum_numeric_form = sum(self.last_name_in_numeric_form)  # сумма фамилии в цифровой форме

        # находим число меньше 100
        while True:
            if self.sum_numeric_form < 100:
                break
            self.sum_numeric_form -= 100

        # выбираем наиболее близкое значение q из таблицы простых чисел (table)
        min_diff = 500
        for value in table.values():
            if abs(value - self.sum_numeric_form) < min_diff:
                min_diff = value - self.sum_numeric_form
                self.q = value

    def _set_n(self):
        """устанавливает n"""
        self.n = self.p * self.q

    def _find_function_of_Euler(self) -> int:
        """Функция эйлера"""
        self.function_of_Euler = (self.p - 1) * (self.q - 1)
        return self.function_of_Euler

    def _set_e(self) -> int:
        """устанавливает число e для открытого ключа"""
        values = [value for value in range(2, self._find_function_of_Euler()) if
                  get_gcd(value, self._find_function_of_Euler()) == 1]
        self.e = random.choice(values)

    def set_d(self):
        d = 1
        while True:
            if (d * self.e) % (self._find_function_of_Euler()) == 1:
                self.d = d
                return
            d += 1

    @staticmethod
    def encrypt(data, e, n):
        """шифруем данные"""
        encrypted_data = [(letters[letter.upper()] ** e) % n for letter in data]
        return encrypted_data

    @staticmethod
    def decrypt(data, d, n):
        decrypted_data = ''.join([get_key(letters, (value ** d) % n) for value in data])
        return decrypted_data


if __name__ == '__main__':
    number = input('Введите номер в списке ')
    last_name = input('Введите фамилию ')
    coder = RSA(number=number, last_name=last_name)
    print('Сгенерированные данные:')
    pprint(coder.__dict__)

    data = input('Введите слово для шифрования ')
    e = input('Введите значение e: ')
    n = input('Введите значение n: ')
    encrypted_data = coder.encrypt(data, int(e), int(n))
    print('Результат шифрования:')
    print(encrypted_data)

    d = input('Введите значение d: ')
    n = input('Введите значение n: ')
    decrypted_data = coder.decrypt(encrypted_data, int(d), int(n))
    print('Результат дешифрования:')
    print(decrypted_data)
