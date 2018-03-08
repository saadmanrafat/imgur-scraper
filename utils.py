from datetime import datetime, date, timedelta

date_format = "%d/%m/%y"


class Convert:

    def __init__(self, date):
        self.input_time = date

    def time_now(self):
        return datetime.utcnow() - timedelta(hours=-5)

    def user_given_time(self):
        return datetime.strptime(self.input_time, date_format)

    def to_days_ago(self):
        if self.time_now() < self.user_given_time():
            raise ValueError('Invalid Date')
        return (self.time_now() - self.user_given_time()).days
