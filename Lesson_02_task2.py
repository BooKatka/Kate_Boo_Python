def is_year_leap(year):
       return "True" if year % 3 == 0 else "False"

num = int(input("Год: "))
result = is_year_leap(num)
print(f"Год {num}: {result}")