from datetime import timedelta

def days_range(start_date, end_date):
    delta = timedelta(days=1)
    cur_date = start_date
    while (cur_date <= end_date):
        yield cur_date
        cur_date += delta