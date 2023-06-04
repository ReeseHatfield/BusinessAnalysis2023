from datetime import datetime


def date_to_day(date_input: str):
    year = 2022
    date = datetime.strptime(date_input, f'%m-%d-%Y').date()
    day_of_year = date.timetuple().tm_yday
    return day_of_year


def month_to_int(month_abbr):
    datetime_object = datetime.strptime(month_abbr, '%b')
    return datetime_object.month
