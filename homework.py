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
            if i.date == dt.datetime.now().date():
                daysum = daysum + i.amount
        return daysum 
        
    def get_week_stats(self):
        week_cash = 0
        week_ago = dt.datetime.now().date() - dt.timedelta(days=7)
        now = dt.datetime.now().date()
        for i in self.records:
            if week_ago <= i.date <= now:
                week_cash = week_cash + i.amount 
        return week_cash
        
    
                
    
class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        todaysum = self.get_today_stats()
        lim2 = self.limit
        calories_remained = lim2 - todaysum
        
        if calories_remained > 0:
            return(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал')
        else:
            return(f'Хватит есть!')

class CashCalculator(Calculator):
    EURO_RATE = 81.41
    USD_RATE = 71.21

    def get_today_cash_remained(self, currency):
        sumfortoday = self.get_today_stats() 
        lim = self.limit
        cash_remained = lim - sumfortoday
        
        if currency == 'rub':
            cur = 'руб'
            N = cash_remained
        elif currency == 'usd':
            cur = 'USD'
            N = cash_remained/CashCalculator.USD_RATE
        elif currency == 'eur':
            cur = 'Euro'
            N = cash_remained/CashCalculator.EURO_RATE
        else:
            return ('Незнакомая валюта')
            
        if cash_remained > 0: 
            return (f'На сегодня осталось {N:.2f} {cur}') 
        elif cash_remained == 0:
            return ('Денег нет, держись')
        else: 
            return (f'Денег нет, держись: твой долг - {abs(N):.2f} {cur}')

if __name__ == "__main__":
    cash_calculator = CashCalculator(1000)
    calories_calculator = CaloriesCalculator(2500)
 
    r1 = Record(amount=145, comment="Безудержный шопинг", date="16.07.2020")
    r2 = Record(amount=1545, comment="Наполнение потребительской корзины", date="16.07.2020")
    r3 = Record(amount=791, comment="Катание на такси", date="15.07.2020")
 
    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    r4 = Record(amount=1500, comment="Кусок тортика. И ещё один.", date="16.07.2020")
    r5 = Record(amount=84, comment="Йогурт.")
    r6 = Record(amount=1140, comment="Баночка чипсов.", date="16.07.2020")

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

 
    print(cash_calculator.get_today_stats())
    print(cash_calculator.get_week_stats())
    print(cash_calculator.get_today_cash_remained('eur'))
    print(calories_calculator.get_calories_remained())
    print(calories_calculator.get_week_stats())
    print(calories_calculator.get_today_stats())