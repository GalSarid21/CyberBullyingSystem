from DAL.social_media_dto import HateMonitor
from flask import render_template
from flask_mail import Mail, Message
from datetime import datetime, timedelta
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


    def scan(self, hate_monitors: Iterable[HateMonitor], mail_app: Mail) -> str:
        
        found_hate_msg = f'found unusual number of hate - ' +\
                         f'email was sent to {self.__alert_email}'

        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        num_hates_in_last_hour = self.__get_numer_of_hates_for_time_period(
            hate_monitors, one_hour_ago)
        
        if num_hates_in_last_hour > self.__max_hate_per_hour:
            self.__send_mail_for_time_period(
                'hour', num_hates_in_last_hour, self.__max_hate_per_hour, mail_app)
            return found_hate_msg
        
        one_day_ago = datetime.utcnow() - timedelta(days=1)
        num_hates_in_last_day = self.__get_numer_of_hates_for_time_period(
            hate_monitors, one_day_ago)
        
        if num_hates_in_last_day > self.__max_hate_per_day:
            self.__send_mail_for_time_period(
                'day', num_hates_in_last_day, self.__max_hate_per_day, mail_app)
            return found_hate_msg
        
        one_week_ago = datetime.utcnow() - timedelta(weeks=1)
        num_hates_in_last_week = self.__get_numer_of_hates_for_time_period(
            hate_monitors, one_week_ago)
        
        if num_hates_in_last_week > self.__max_hate_per_week:
            self.__send_mail_for_time_period(
                'week', num_hates_in_last_week, self.__max_hate_per_week, mail_app)
            return found_hate_msg

        one_month_ago = datetime.utcnow() - timedelta(days=30)
        num_hates_in_last_month = self.__get_numer_of_hates_for_time_period(
            hate_monitors, one_month_ago)
        
        if num_hates_in_last_month > self.__max_hate_per_month:
            self.__send_mail_for_time_period(
                'month', num_hates_in_last_month, self.__max_hate_per_month, mail_app)
            return found_hate_msg

        return 'scan completed successfully without any unusual findings!'
    

    def __get_numer_of_hates_for_time_period(self, 
                                             hate_monitors: Iterable[HateMonitor],
                                             time_period: datetime) -> int:
        
        all_hms_in_period = [hm for hm in hate_monitors if hm.added_on >= time_period and hm.is_hate()]
        all_hate_in_period = [hm for hm in all_hms_in_period if hm.is_hate()]
        return len(all_hate_in_period) 

    def __send_mail_for_time_period(self, 
                                    period_str: str, 
                                    num_hate_for_period: int,
                                    max_hate_rule: int,
                                    mail_app: Mail) -> None:
        msg = Message(
            subject='Online Bullying Detection (OBD) Alert Message', 
            recipients = [self.__alert_email])
        
        num = num_hate_for_period - max_hate_rule
        denum = max_hate_rule
        hate_deviation_pct = round((num/denum)*100, 2)
        pct_section = f"The number of hate events is {hate_deviation_pct}% higher " +\
                      f"than the latest rule in our system " if hate_deviation_pct > 0 else ''+\
                      f"The number of hate events is equal to the latest rule in our system "

        msg.html = render_template(
            'scan_email_template.html', 
            user_name=self.__user_name,
            scan_time=datetime.utcnow().strftime('%Y-%m-%d %H:%M'),
            num_hate=num_hate_for_period,
            period_str=period_str,
            pct_section=pct_section,
            max_hate_rule=max_hate_rule)
        
        mail_app.send(msg)
