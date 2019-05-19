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
    """
    Ut 定时提醒填写函数
    :param today_date: 提醒日期
    :return: 是否提醒标签
    """
    # UT 定时提醒填写部分
    tomorrow_date = today_date + timedelta(1)
    if not is_workday(today_date):
        # 今天不是工作日：不提醒
        remind_flag = "无需"
    elif not is_workday(tomorrow_date):
        # 今天是工作日，明天不是工作日：提醒
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
        remind_flag = "需"
    elif tomorrow_date.strftime('%w') == '1':
        # 今天是工作日，明天是周一：提醒
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
        remind_flag = "需"
    elif tomorrow_date.strftime('%m') != today_date.strftime('%m'):
        # 今天是工作日，明天是下月1号：提醒
        easygui.msgbox("填写UT，填写UT，填写UT！！！", title="提醒", ok_button="已填写")
        remind_flag = "需"
    else:
        # 其他情况：不提醒
        remind_flag = "无需"

    def get_last_workday(tg_date):
        """
        获取目标日期的上一个工作日
        :param tg_date: 目标日期
        :return: 上一个工作日日期
        """
        i = -1
        while True:
            last_day = tg_date + timedelta(i)
            if is_workday(last_day):
                return last_day
            i -= 1

    # UT最后一次提醒部分
    last_workday = get_last_workday(today_date)
    if not is_workday(today_date):
        # 今天不是工作日：无需确认
        confirm_flag = "无需确认"
    elif today_date.isocalendar()[1] != last_workday.isocalendar()[1]:
        # 今天是本周的第一个工作日：需要确认
        easygui.msgbox("确认已填写UT", title="提醒", ok_button="确认")
        confirm_flag = "已确认"
    elif today_date.strftime('%m') != last_workday.strftime('%m'):
        # 今天是本月的第一个工作日：需要确认
        easygui.msgbox("确认已填写UT", title="提醒", ok_button="确认")
        confirm_flag = "已确认"
    else:
        # 其他情况：无需确认
        confirm_flag = "无需确认"
    return remind_flag, confirm_flag


if __name__ == '__main__':
    log_path = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(level=logging.INFO,
                        filename='{}/work_clock.log'.format(log_path),
                        format='%(asctime)s : %(levelname)s : %(message)s'
                        )
    target_date = date.today()
    # target_date = date.today() + timedelta(1)
    remind, confirm = ut_clock(today_date=target_date)
    logging.info(f'今日{remind}填写Ut，{confirm}填写')
