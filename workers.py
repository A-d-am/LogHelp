class Workers:
    def __init__(self):
        self.__workers_list = dict()

    def add_workers(self):
        flag = True
        while flag:
            name = input('Введите имя и фамилию работника: ')
            try:
                cost_per_kilo = float(input('Введите стоимость 1 км для этого водителя: '))
                kilo = float(input('Сколько км проехал водитель: '))
                salary = kilo * cost_per_kilo
                self.__workers_list[name] = salary
            except:
                print('Ошибка ввода, повторите попытку')
                continue

            choice = input('Вы желаете записать еще (да - 1 , нет  - 2)?  ')
            if choice != '1':
                flag = False

    def del_workers_list(self, name):
        ex = 'Такого сотрудника нет в списке, проверьте ввод'
        val = self.__workers_list.pop(name, ex)
        if val == ex:
            return ex
        else:
            # ans = f'Вы удалили запись  {val}'
            return f'Вы удалили запись  {val}'

    def supp_workers_list(self, name, salary):  # дописать рабочего в словарь
        if name in self.__workers_list.keys():
            pass
        else:
            self.__workers_list[name] = salary

    def save_workers_list(self):
        if len(self.__workers_list) != 0:
            file = open('workers.txt', 'w')
            count = 1
            for i in self.__workers_list.keys():
                note = f'{count}) {i} -- {self.__workers_list[i]} р. за рейс'
                file.write(str(note) + '\n')
            summary = str(self.sum_salary())
            note = f'Сумма всех зарплат составляет {summary} р.'
            file.write(note)
            file.close()
            return 'Сохранение в файл workers.txt прошло успешно'
        else:
            print('Вы пытаетесь сохранить пустой список')

    def sum_salary(self):
        if len(self.__workers_list) != 0:
            total = 0
            for i in self.__workers_list.values():
                total += i
            return total
        else:
            return 0

    def get_workers_list(self):
        if len(self.__workers_list) == 0:
            print('В списке нет записей')
        else:
            count = 1
            for i in self.__workers_list.keys():
                print(f'{count}) {i} -- {self.__workers_list[i]} р. за рейс')
                count += 1
