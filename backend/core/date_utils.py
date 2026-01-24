from datetime import date, datetime
from typing import Optional, Union

from backend.core.exceptions import InvalidDate


class DateUtils:
    @staticmethod
    def parse_date(input_date: Union[str, date, datetime]) -> Optional[date]:
        if input_date is None:
            return None

        if isinstance(input_date, date) and not isinstance(input_date, datetime):
            return input_date

        if isinstance(input_date, datetime):
            return input_date.date()

        if isinstance(input_date, str):
            try:
                return datetime.strptime(input_date, "%Y-%m-%d").date()
            except ValueError:
                pass

            try:
                return datetime.strptime(input_date, "%Y-%m").date()
            except ValueError:
                pass

        raise InvalidDate(f"Impossible to parse this date : {input_date}")
