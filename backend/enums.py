from enum import Enum
import pandas as pd
from datetime import datetime, timedelta
from typing import Tuple

class RecentPeriod(Enum):

    TODAY = timedelta(days=1)
    THIS_WEEK = timedelta(days=7)
    THIS_MONTH = timedelta(days=31)
    THIS_YEAR = timedelta(days=365)

    def get_date_range(self) -> Tuple[datetime, datetime]:
        """ Returns the start and end date for the given time period"""
        return (datetime.today() - self.value, datetime.today())
