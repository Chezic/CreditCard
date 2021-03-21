def check_brand(card_num):
    """
    Функция определеяет платежную систему введеной карты
    :param card_num: Номер карты
    :return: Название платежной системы
    """
    if card_num[0] == "4":
        brand = "Visa"
    elif card_num[0] == "5":
        brand = "MasterCard"
    elif card_num[0] == "3" and card_num[1] == "7":
        brand = "American Express"
    elif card_num[0] == "6":
        brand = "Discover"
    elif card_num[0] == "2":
        brand = "Мир"
    else:
        brand = "Неизвестно"
    return brand


def sum_of_digits(number):
    """
    Сумма цифр числа
    :param number: Число
    :return: Сумма цифр числа
    """
    # Сумма элементов строки, преобразованных в тип int функцией map
    return sum(list(map(int, str(number))))


def check_sum(card_num):
    """
    Алгоритм проверки номера кредитной карты Ганса Луна
    :param card_num: Номер карты
    :return: Результат проверки
    """
    # Строка для редактирования
    temp_card_num = ""
    card_num = card_num[::-1]
    for index in range(len(card_num)):
        if index % 2 != 0:
            if int(card_num[index]) * 2 > 9:
                temp_card_num += str(sum_of_digits(int(card_num[index]) * 2))
            else:
                temp_card_num += str(int(card_num[index]) * 2)
        else:
            temp_card_num += card_num[index]
    if sum_of_digits(int(temp_card_num)) % 10 == 0:
        return "Номер картый верный"
    else:
        return "Номер картый неверный"


def main():
    card_num = input("Введите номер карты:")
    if 13 <= len(card_num) <= 16:
        print("Тип Вашей карты:", check_brand(card_num))
        print(check_sum(card_num))
    else:
        print("Некорректный номер карты, попробуйте еще раз.")
        main()


main()
