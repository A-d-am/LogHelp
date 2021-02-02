class Oil:
    def __init__(self):
        self.__fuel_money = 0  # счетчик потраченных на топливо денег

    def oil_cost(self):
        flag = True
        while flag:
            try:
                fuel_quantity = float(input('Сколько литров топлива 1 вида было потрачено: '))
                cost_per_liter = float(input('Сколько стоил 1 литр этого топлива: '))
            except:
                print('Ошибка ввода, повторите попытку')
                continue
            if_sales = input('Была ли использована скидка на топливо (д = да,все остальное - нет)? ').lower()
            if if_sales == 'д':
                try:
                    discount = float(input('Сколько процентов скидки (вводить без знака %)? '))
                    intermediate_result = fuel_quantity * cost_per_liter
                    self.__fuel_money += intermediate_result - intermediate_result * (discount / 100)
                except():
                    print('Ошибка ввода скидки, пожалуйста, проверьте ввод и повторите попытку')

            else:
                self.__fuel_money += fuel_quantity * cost_per_liter
            choice = input('Вы желаете записать еще (д = да,все остальное - нет)?  ').lower()
            if choice != 'д':
                flag = False

    def read_oil(self):  # для чтения из файла (для работы вне фукнции oil)
        try:
            file = open('oil.txt', 'r')
            value = file.readline()
            file.close()
            return value
        except:
            return 0


    def increase_money(self, val):  # отвечает за увеличения суммы заатрат на топливо
        self.__fuel_money += val

    def write(self):  # запись для дальнешего обращения к этому файлу
        file = open('oil.txt', 'w')
        file.write(str(self.__fuel_money))
        file.close()

    def reduce_money(self, val):  # для уменьшения значения перменной __fuel_money
        if self.__fuel_money < val:
            print('Стоимость топлива меньше, чем вы хотите вычесть')
        else:
            self.__fuel_money -= val

    def get_fuel_money(self):  # для вывода __fuel_money
        return self.__fuel_money