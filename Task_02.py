import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int):
    if not (1 <= min_num <= max_num <= 1000 and
            quantity <= (max_num - min_num)): #перевірка валідності вхідних даних
       return []
    else:
        numbers = random.sample(range(min_num, max_num + 1), quantity) #генерація випадкових чисел

        return sorted(numbers) #повернення відсортованиго списку

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)
