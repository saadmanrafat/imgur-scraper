from datetime import datetime

date_format = "%d/%m/%Y"


class Convert:
    """Subtracts the given time from the current UTC time
    and returns the number of days.

    :param:date, where date is a string
    """
    def __init__(self, date):
        self.input_time = date

    def user_given_time(self):
        return datetime.strptime(self.input_time, date_format)

    def to_days_ago(self):
        if datetime.utcnow() <= self.user_given_time():
            raise ValueError('Invalid Date')
        return (datetime.utcnow() - self.user_given_time()).days



