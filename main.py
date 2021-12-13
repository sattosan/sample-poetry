from dateutil.relativedelta import relativedelta
import datetime
def main():
    for i in range(10):
        today=datetime.date.today()
        print(today)
        next_month_date=today + relativedelta(months=+i)
        print(next_month_date)
if __name__=='__main__':
    main()
