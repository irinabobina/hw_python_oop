import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)

    def get_today_stats(self):
        day_sum = 0
        date_today = dt.date.today()
        for i in self.records:
            if i.date == date_today:
                day_sum += i.amount
        return day_sum

    def get_week_stats(self):
        week_cash = 0
        now = dt.date.today()
        week_ago = now - dt.timedelta(days=6)
        now = dt.date.today()
        for i in self.records:
            if week_ago <= i.date <= now:
                week_cash += i.amount
        return week_cash

    def today_remained(self):
        today_sum = self.get_today_stats()
        lim = self.limit
        today_rem = lim - today_sum
        return today_rem


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        cals_remained = self.today_remained()

        if cals_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но'
                    f' с общей калорийностью не более {cals_remained} кКал')

        return 'Хватит есть!'


class CashCalculator(Calculator):
    EURO_RATE = 81.41
    USD_RATE = 71.21

    def get_today_cash_remained(self, currency):
        cash_remained = self.today_remained()

        currencies = {
            'rub': ['руб', 1],
            'eur': ['Euro', CashCalculator.EURO_RATE],
            'usd': ['USD', CashCalculator.USD_RATE]
        }

        if cash_remained == 0:
            return 'Денег нет, держись'

        if currency not in currencies:
            return 'Незнакомая валюта'

        if currency in currencies:
            now_cash = cash_remained/currencies[currency][1]

        cur_name = currencies[currency][0]

        if cash_remained > 0:
            return f'На сегодня осталось {now_cash:.2f} {cur_name}'

        minus_n = abs(now_cash)
        return ('Денег нет, держись:'
                f' твой долг - {minus_n:.2f} {cur_name}')


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    calories_calculator = CaloriesCalculator(2500)

    r1 = Record(amount=145, comment='Безудержный шопинг', date='27.07.2020')
    r2 = Record(amount=1545, comment='Корзина', date='27.07.2020')
    r3 = Record(amount=791, comment='Катание на такси', date='27.07.2020')

    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    r4 = Record(amount=1500, comment='Тортик', date='27.07.2020')
    r5 = Record(amount=84, comment='Йогурт.')
    r6 = Record(amount=1140, comment='Баночка чипсов.', date='27.07.2020')

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    print(cash_calculator.get_today_stats())
    print(cash_calculator.get_week_stats())
    print(cash_calculator.get_today_cash_remained('eur'))
    print(cash_calculator.get_today_cash_remained('gdg'))
    print(calories_calculator.get_calories_remained())
    print(calories_calculator.get_week_stats())
    print(calories_calculator.get_today_stats())
    print(calories_calculator.get_calories_remained())
