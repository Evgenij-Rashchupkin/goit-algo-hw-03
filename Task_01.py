from datetime import datetime


def get_days_from_today():
    given_date = input("Введіть дату у форматі YYYY-MM-DD: ")  # введення дати користувачем

    try:
        given_date = datetime.strptime(given_date, "%Y-%m-%d").date()  # введений рядок на об'єкт datetime
    except ValueError:
        return "Неправильний формат дати. Введіть дату у форматі YYYY-MM-DD."  # коли формат дати невірний

    today_day = datetime.now().date()  # отримання поточної дати
    print(f"Задана дата: {given_date}")
    print(f"Поточна дата: {today_day}")

    diff_day = given_date - today_day  # обчислення різниці між датами
    print("Різниця в днях між заданою та поточною датою:")

    return diff_day.days


result = get_days_from_today()
print(result)
