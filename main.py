import OIL
import workers


def menu_bar():
    print("""
    Главное меню
    1 - Рассчет стоимости топлива
    2 - Рассчет зарплаты сотрудникам
    3 - Вывести инструкцию
    4 - Конец сеанса 
    """)


def instructions():
    print("""
    Инструкция 
    1)Для ввода дробных чисел использовать точку (.) !
    2)Для ввода процентов не использовать % (пример ввода 65% = 65)
    """)


def oil_menu_bar():
    print("""
    1 - Рассчет затрат на топливо
    2 - Вывести на экран сумму затрат на топливо  
    3 - Сохранить сумму затрат для использования после выхода из программы
    4 - Увеличить сумму затрат на топливо 
    5 - Уменьшить сумму затрат на топливо
    6 - Выйти в главное меню
    """)


def oil():  # часть программы для работы с топливом
    my_oil = OIL.Oil()
    flag = True
    while flag:
        oil_menu_bar()
        choice = input('Введите ваш выбор: ')
        if choice == '1':
            my_oil.oil_cost()
            print(f'Теперь сумма затрат на топливо составляет {my_oil.get_fuel_money()} р.')
        elif choice == '2':
            print(f'Сумма затрат на топливо составляет{my_oil.get_fuel_money()} р.')
            print()
        elif choice == '3':
            print('На данный момент сумма затрат на топливо ')
            print(f'составляет {my_oil.get_fuel_money()} р.')
            decision = input('Вы уверены, что хотите сохранить (да - 1 , нет  - 2) ? ')
            if decision == '1':
                my_oil.write()
                print('Данные успешно сохранены')
        elif choice == '4':
            try:
                value = float(input('На сколько хотите увеличить сумму затрат на топливо? '))
                my_oil.increase_money(value)
                print(f'Сумма затрат составляет {my_oil.get_fuel_money()} р.')
            except:
                print('Ошибка ввода, повторите еще раз')
        elif choice == '5':
            try:
                value = float(input('На сколько хотите уменьшить сумму затрат на топливо? '))
                my_oil.reduce_money(value)
                print(f'Теперь сумма затрат на топливо составляет {my_oil.get_fuel_money()} р.')
            except:
                print('Ошибка ввода,повторите попытку')
        elif choice == '6':
            flag = False
            print('Возвращение в главное меню')

        else:
            print('Ошибка, повторите еще раз ')
            print()


def salary_menu_bar():
    print("""
    1 - Заработная плата водителей (имя - зарплата за рейс) 
    2 - Удалить водителя из списка (пункт 1)
    3 - Добавить водителя в список (пункт 1)
    4 - Сохранить список в файл 
    5 - Вывести на экран сумму всех зарплат водителей 
    6 - Выйти в главное меню
    """)


def salary():  # часть программы для работы с зарплатами сотрудников
    flag = True
    my_workers = workers.Workers()
    while flag:
        salary_menu_bar()
        choice = input('Введите ваш выбор: ')
        if choice == '1':
            my_workers.add_workers()  # вызывает метод, который добавляет в список сотрудника и его зарплату
            print('Теперь список зарплат водителей выглядит так:')
            my_workers.get_workers_list()
        elif choice == '2':
            worker_name = input('Фамилия сотрудника, которого хотите удалить: ')
            print(my_workers.del_workers_list(worker_name))
            print('Теперь список зарплат водителей выглядит так:')
            my_workers.get_workers_list()
        elif choice == '3':
            worker_name = input('Фамилия сотрудника, которого хотите добавить: ')
            try:
                worker_salary = float(input('Зарплата сотрудника, которого хотите добавить: '))
                my_workers.supp_workers_list(worker_name, worker_salary)
                print('Теперь список зарплат водителей выглядит так:')
                my_workers.get_workers_list()
            except():
                print('Ошибка ввода, повторите еще раз')
        elif choice == '4':
            print(my_workers.save_workers_list())
        elif choice == '5':
            print(f'Общая сумма зарплат составляет {my_workers.sum_salary()} р.')
        elif choice == '6':
            flag = False
            print('Возвращение в главное меню')
        else:
            print('Ошибка, повторите еще раз')


def main():
    flag = True
    while flag:
        menu_bar()
        choice = input('Введите ваш выбор: ')
        if choice == '1':
            oil()
        elif choice == '2':
            salary()
        elif choice == '3':
            instructions()
        elif choice == '4':
            print('Завершение работы.')
            flag = False
        else:
            print('Ошибка, повторите еще раз ')
            print()


main()
