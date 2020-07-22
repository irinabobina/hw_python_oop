import datetime as dt
 
 
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, rec):
        self.records.append(rec)
 
    def get_today_stats(self): 
        daysum = 0 
        for i in self.records: 
            if i.date == dt.date.today(): 
                daysum = daysum + i.amount 
        return daysum  

    def get_week_stats(self):
        week_cash = 0
        week_ago = dt.date.today() - dt.timedelta(days=6)
        now = dt.date.today()
        for i in self.records:
            if week_ago <= i.date <= now:
                week_cash = week_cash + i.amount 
        return week_cash

    def today_remained(self):
        todaysum = self.get_today_stats()
        lim = self.limit
        todayremained = lim - todaysum
        return todayremained


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
        calories_remained = self.today_remained()

        if calories_remained > 0:
            a = ('Сегодня можно съесть что-нибудь ещё, но' 
                f' с общей калорийностью не более {calories_remained} кКал')
        else:
            a = 'Хватит есть!'
        return a


class CashCalculator(Calculator):
    EURO_RATE = 81.41
    USD_RATE = 71.21

    currencies = {
        'rub': 'руб',
        'eur': 'Euro',
        'usd': 'USD'
    }

    def get_today_cash_remained(self, currency):
        cash_remained = self.today_remained()

        if currency not in CashCalculator.currencies:
            M = 'Незнакомая валюта'
            return M

        today_currency = CashCalculator.currencies[currency]

        if currency == 'rub':
            N = cash_remained
        elif currency == 'usd':
            N = cash_remained/CashCalculator.USD_RATE
        elif currency == 'eur':
            N = cash_remained/CashCalculator.EURO_RATE

        if cash_remained > 0: 
            return (f'На сегодня осталось {N:.2f} {today_currency}') 
        elif cash_remained == 0:
            return ('Денег нет, держись')
        else: 
            K = abs(N)
            return (f'Денег нет, держись:'
            f' твой долг - {K:.2f} {today_currency}')

if __name__ == "__main__":
    cash_calculator = CashCalculator(1000)
    calories_calculator = CaloriesCalculator(2500)
 
    r1 = Record(amount=145, comment="Безудержный шопинг", date="23.07.2020")
    r2 = Record(amount=1545, comment="Корзина", date="23.07.2020")
    r3 = Record(amount=791, comment="Катание на такси", date="22.07.2020")
 
    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    r4 = Record(amount=1500, comment="Тортик", date="23.07.2020")
    r5 = Record(amount=84, comment="Йогурт.")
    r6 = Record(amount=1140, comment="Баночка чипсов.", date="23.07.2020")

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