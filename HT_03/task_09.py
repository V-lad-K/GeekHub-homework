# Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку
# (границі включно). P.S. Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.

start_year = int(input("input start year "))
end_year = int(input("input end year "))

for year in range(start_year, end_year+1):
    if year % 100 and not year % 4 or not year % 400:
        print(year)
