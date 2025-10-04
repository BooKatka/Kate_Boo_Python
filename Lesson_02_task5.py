def month_to_season(n):
    if n in(12,1,2):
        print("Зима")
    elif n in(3,4,5):
        print("Весна")
    elif n in(6,7,8):
        print("Лето")
    elif n in(9,10,11):
        print ("Осень")
    else: return(print("Месяц не найден"))
month_to_season(int(input("Укажите номер месяца:")))