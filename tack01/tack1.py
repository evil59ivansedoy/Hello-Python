#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def week_day():
    num_day = int(input('введите номер дня'))
    if num_day >= 1 and num_day <= 5 : return ('no')
    elif num_day == 6 or 7  : return('yes')
print(week_day())

