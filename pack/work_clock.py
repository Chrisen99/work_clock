# -*- encoding:utf-8 -*-

"""
@author: Chrisen
@file:  work_clock.py
@date:  2019/05/08
"""

import os
import logging
import easygui
from datetime import date, timedelta
from chinese_calendar import is_workday


def ut_clock(today_date):
    tomorrow_date = today_date + timedelta(1)
    if not is_workday(today_date):
        pass
    elif not is_workday(tomorrow_date):
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
    elif tomorrow_date.strftime('%w') == '1':
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
    elif tomorrow_date.strftime('%m') != today_date.strftime('%m'):
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
    else:
        pass


def make_log_path(path):
    if os.path.exists(path):
        return os.path.abspath(path)
    else:
        return os.makedirs(path)


if __name__ == '__main__':
    log_path = make_log_path('D:/WorkClockLog/')
    print(log_path)
    logging.basicConfig(level=logging.INFO,
                        filename='{}/work_clock.log'.format(log_path),
                        format='%(asctime)s : %(levelname)s : %(message)s'
                        )
    target_date = date.today()
    ut_clock(today_date=target_date)
    logging.info('今日已运行')
