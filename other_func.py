monthes = ('январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')
days = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
def by_shift(worker):
    return len(worker.shift)

def month_in_year(month):
    start_day = 1
    for i in monthes:
        if i != month:
            start_day += days_in_month(i)
        else:
            print((start_day, start_day + days_in_month(i) - 1))
            return (start_day, start_day + days_in_month(i) - 1)


def days_in_month(month):
    if month in ('январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь'):
        return 31
    elif month in ('апрель', 'июнь', 'сентябрь', 'ноябрь'):
        return 30
    else:
        return 28

