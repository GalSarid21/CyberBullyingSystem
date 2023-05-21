from DAL.social_media_dto import HateMonitor
from typing import Iterable

class HateTableScanBL():

    def __init__(self,
                 user_name: str, 
                 alert_email: str, 
                 max_hate_per_hour: int,
                 max_hate_per_day: int,
                 max_hate_per_week: int,
                 max_hate_per_month: int) -> None:
        
        self.__user_name = user_name
        self.__alert_email = alert_email
        self.__max_hate_per_hour = max_hate_per_hour
        self.__max_hate_per_day = max_hate_per_day
        self.__max_hate_per_week = max_hate_per_week
        self.__max_hate_per_month = max_hate_per_month
    
    def scan(self, hate_monitors: Iterable[HateMonitor]) -> str:
        msg = f'found unusual number of hate - email was sent to {self.__alert_email}'
        send_email = False
        # check all rules - if any rule is true - return the msg
        # set
        if send_email:
            # send email logic
            a=1 
        return 'scan completed successfully without any unusual findings!'
