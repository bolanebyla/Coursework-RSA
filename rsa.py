import random
from pprint import pprint


table = {1: 997, 14: 991, 27: 983, 40: 977, 53: 971, 66: 967, 79: 953, 92: 947, 105: 941, 118: 937, 131: 929,
         2: 919, 15: 911, 28: 907, 41: 887, 54: 883, 67: 881, 80: 877, 93: 863, 106: 859, 119: 857, 132: 853,
         3: 839, 16: 829, 29: 827, 42: 823, 55: 821, 68: 811, 81: 809, 94: 797, 107: 787, 120: 773, 133: 769,
         4: 761, 17: 757, 30: 751, 43: 743, 56: 739, 69: 733, 82: 727, 95: 719, 108: 709, 121: 701, 134: 691,
         5: 683, 18: 677, 31: 673, 44: 661, 57: 659, 70: 653, 83: 647, 96: 643, 109: 641, 122: 631, 135: 619,
         6: 617, 19: 613, 32: 607, 45: 601, 58: 599, 71: 593, 84: 587, 97: 577, 110: 571, 123: 569, 136: 563,
         7: 557, 20: 547, 33: 541, 46: 523, 59: 521, 72: 509, 85: 503, 98: 499, 111: 491, 124: 487, 137: 479,
         8: 467, 21: 463, 34: 461, 47: 457, 60: 449, 73: 443, 86: 439, 99: 433, 112: 431, 125: 421, 138: 419,
         9: 409, 22: 401, 35: 397, 48: 389, 61: 383, 74: 379, 87: 373, 100: 367, 113: 359, 126: 353, 139: 349,
         10: 347, 23: 337, 36: 331, 49: 317, 62: 313, 75: 311, 88: 307, 101: 293, 114: 283, 127: 281, 140: 277,
         11: 271, 24: 269, 37: 263, 50: 257, 63: 251, 76: 241, 89: 239, 102: 233, 115: 229, 128: 227, 141: 223,
         12: 211, 25: 199, 38: 197, 51: 193, 64: 191, 77: 181, 90: 179, 103: 173, 116: 167, 129: 163, 142: 157,
         13: 151, 26: 149, 39: 139, 52: 137, 65: 131, 78: 127, 91: 113, 104: 109, 117: 107, 130: 103, 143: 101}

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
