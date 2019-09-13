from datetime import datetime

date_format = "%Y-%m-%d"


class Convert:
    """Subtracts the given time from the current UTC time
    and returns the number of days.

    :param:start_date, where date is a string
    :param:end_date, where date is a string
    """

    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def _user_given_time(self):
        return (
            datetime.strptime(self.start_date, date_format),
            datetime.strptime(self.end_date, date_format),
        )

    def to_days_ago(self):
        start_time, end_time = self._user_given_time()
        time_now = datetime.utcnow()
        if time_now < start_time or time_now < end_time:
            raise ValueError("Invalid Date")
        start_time = (datetime.utcnow() - start_time).days
        end_time = (datetime.utcnow() - end_time).days
        if start_time < end_time:
            raise ValueError("Invalid Date Range")
        return start_time, end_time
