from datetime import datetime


def Date(date_string):
    date = datetime.strptime(date_string, "%d/%m/%Y")

    day = {
        '1': 'Понедельник: ',
        '2': 'Вторник: ',
        '3': 'Среда: ',
        '4': 'Четверг: ',
        '5': 'Пятница: ',
        '6': 'Суббота: ',
        '7': 'Воскресенье: '
    }

    return day[str(datetime.isoweekday(date))]
    