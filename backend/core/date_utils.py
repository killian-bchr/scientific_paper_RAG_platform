from datetime import date, datetime
from typing import Optional, Tuple, Union

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

    @staticmethod
    def compute_start_and_end_date(
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
    ) -> Tuple[date, date]:
        start_date, end_date = None, None

        if start_year:
            start_date = date(start_year, 1, 1)

        if end_year:
            end_date = date(end_year, 12, 31)

        if start_date and end_date and start_date > end_date:
            raise ValueError("Start year must be before end year")

        return start_date, end_date
