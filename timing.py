# -*- codeing -*-
# @Time : 2021/11/27 15:37
# @Author : Torres-圣君
# @File : timing.py
# @Sofaware : PyCharm
import datetime
# import os
import subprocess
import time
import tkinter as tk
from tkinter import messagebox


class TimingTime:
    def __init__(self):
        self.Timing_custom_flag = True
        self.count = 1
        self.year = int(time.strftime('%Y'))    # 获取：年
        self.month = int(time.strftime('%m'))   # 获取：月
        self.day = int(time.strftime('%d'))     # 获取：日
        self.hour = int(time.strftime('%H'))    # 获取：时
        self.min = int(time.strftime('%M'))     # 获取：分
        self.second = int(time.strftime('%S'))  # 获取：秒

        self.now_s = int(time.time())
        # self.set_year = tk.IntVar()     # 定义年
        # self.set_month = tk.IntVar()    # 定义月
        # self.set_day = tk.IntVar()      # 定义日
        self.set_hour = tk.IntVar()     # 定义时
        self.set_min = tk.IntVar()      # 定义分
        self.set_second = tk.IntVar()   # 定义秒

        self.new_month = self.month     # 用于计算新的月份
        self.new_day = self.day         # 用于计算新的天数
        pass

    def timingcustom(self):
        if self.Timing_custom_flag:
            self.Timing_custom_flag = False
            # 创建子窗口，主窗口一旦关闭，子窗口连同一起关闭
            self.ttwin = tk.Toplevel()
            self.ttwin.title("设置定时关机-24小时制")
            self.ttwin.resizable(0, 0)
            sw = self.ttwin.winfo_screenwidth()
            sh = self.ttwin.winfo_screenheight()
            ww = 300
            wh = 100
            x = (sw - ww) / 2
            y = (sh - wh - 50) / 2
            self.ttwin.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

            # 设置小时定时
            hour_text = tk.Label(self.ttwin, text="时：")
            hour_text.place(x=30, y=10)
            set_hour = tk.Entry(self.ttwin, textvariable=self.set_hour, width=10)
            set_hour.place(x=80, y=10)
            # 设置分钟定时
            min_text = tk.Label(self.ttwin, text="分：")
            min_text.place(x=30, y=40)
            set_min = tk.Entry(self.ttwin, textvariable=self.set_min, width=10)
            set_min.place(x=80, y=40)
            # 设置秒定时
            second_text = tk.Label(self.ttwin, text="秒：")
            second_text.place(x=30, y=70)
            set_second = tk.Entry(self.ttwin, textvariable=self.set_second, width=10)
            set_second.place(x=80, y=70)
            # 固定追加的默认值
            if self.count:
                set_hour.insert(0, "0")
                set_min.insert(0, "0")
                set_second.insert(0, "0")
                self.count -= 1
            # 设置确定按钮
            ok_button = tk.Button(self.ttwin, text="确定", command=self.timing_custom)
            ok_button.place(x=220, y=10)
            # 设置取消按钮
            quit_button = tk.Button(self.ttwin, text="取消", command=lambda: (self.ttwin.destroy(), self.exit_ttwin()))
            quit_button.place(x=220, y=60)
            # 设置点'X'后执行的内容
            self.ttwin.protocol('WM_DELETE_WINDOW', lambda: (self.ttwin.destroy(), self.exit_ttwin()))
            self.ttwin.mainloop()

            self.ttwin.mainloop()
            self.Timing_custom_flag = True

    def exit_ttwin(self):
        # 点击'取消'或'X'后，将规则重回为True
        self.Timing_custom_flag = True

    def timing_custom(self):
        # 判断用户输入的值是否合法
        try:
            if 0 <= int(self.set_hour.get()) < 24 and \
                    0 <= int(self.set_min.get()) < 60 and \
                    0 <= int(self.set_second.get()) < 60:
                use_time = "%02d:%02d:%02d" % (self.set_hour.get(), self.set_min.get(), self.set_second.get())
                # 调用get_use_time_s函数，获取定时操作
                self.get_use_time_s(use_time)
            else:
                messagebox.showerror(title='设置异常', message='您的输入超出范围，请设置正确的值！')
        except Exception as re:
            messagebox.showerror(title='设置异常', message='您的输入有误，请输入正整数！')
            print(re)

    def count_time_00(self):
        self.get_use_time_s("00:00:00")

    def count_time_06(self):
        self.get_use_time_s("06:00:00")

    def count_time_12(self):
        self.get_use_time_s("12:00:00")

    def count_time_18(self):
        self.get_use_time_s("18:00:00")

    def get_use_time_s(self, use_time):
        set_use_time = use_time.split(":")
        # 判断传入的时间是否已经过去。没有过去，则定时为今日
        if self.hour < int(set_use_time[0]) or \
                (self.hour == int(set_use_time[0]) and self.min < int(set_use_time[1])) or \
                (self.hour == int(set_use_time[0]) and self.min == int(set_use_time[1]) and self.second < int(set_use_time[2])):
            # 获取对话框停留的秒数
            msg_time_start = int(time.time())
            res = messagebox.askokcancel('关机提醒', message=f'确定要设置在{use_time}关机吗？')
            msg_time_end = int(time.time())
            msg_time = msg_time_end - msg_time_start
            # 如果点确定则执行
            if res:
                # 获取当前时间
                d1 = datetime.datetime.strptime(
                    f'{self.year}-{self.month}-{self.day} {self.hour}:{self.min}:{self.second}', '%Y-%m-%d %H:%M:%S')
                # 获取设置的时间
                d2 = datetime.datetime.strptime(f'{self.year}-{self.month}-{self.day} {use_time}', '%Y-%m-%d %H:%M:%S')
                # 获取现在到指定时间需要的时间
                delta = d2 - d1
                delta_time = str(delta).split(":")
                # 获取现在到指定时间的秒数
                set_timing = int(delta_time[0]) * 60 + int(delta_time[1]) * 60 + int(delta_time[2]) - msg_time - 1
                # os.system(f"Windows定时关机 -s -t {set_timing}")
                subprocess.run(f"shutdown -s -t {set_timing}",
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
                messagebox.showinfo(title='关机提醒', message=f'该计算机将于{use_time}关机！')
        # 如果过去，则询问是否定为明天
        else:
            # 获取对话框停留的秒数
            msg_time_start = int(time.time())
            res = messagebox.askokcancel("关机提醒", message="你设置的关机时间已过去，是否设置为明天的定时？")
            msg_time_end = int(time.time())
            msg_time = msg_time_end - msg_time_start
            # 如果点确定则执行
            if res:
                # 如果设置的时间以过，则天数+1
                if (self.month != 1 or self.month != 2 or self.month != 3 or self.month != 5 or
                        self.month != 7 or self.month != 8 or self.month != 10 or self.month != 12) and \
                        self.day == 30:     # 如果月数不是1,2,3,5,7,8,10,12月，并且是第30天时，月份+1，天数归1
                    self.new_month = self.month + 1
                    self.new_day = 1
                elif self.day == 31:        # 如果是第31天时，月份+1，天数归1
                    self.new_month = self.month + 1
                    self.new_day = 1
                else:       # 否则，也就是不是每月的最后一天，则天数+1
                    self.new_day = self.day + 1
                # 获取当前时间
                d1 = datetime.datetime.strptime(
                    f'{self.year}-{self.month}-{self.day} {self.hour}:{self.min}:{self.second}', '%Y-%m-%d %H:%M:%S')
                # 获取设置的时间
                d2 = datetime.datetime.strptime(f'{self.year}-{self.new_month}-{self.new_day} {use_time}', '%Y-%m-%d %H:%M:%S')
                # 获取现在到指定时间需要的时间
                delta = d2 - d1
                delta_time = str(delta).split(":")
                # 获取现在到指定时间的秒数
                set_timing = int(delta_time[0]) * 60 * 60 + int(delta_time[1]) * 60 + int(delta_time[2]) - msg_time - 1
                # os.system(f"Windows定时关机 -s -t {set_timing}")
                subprocess.run(f"shutdown -s -t {set_timing}",
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
                messagebox.showinfo(title='关机提醒', message=f'该计算机将于{self.new_month}月{self.new_day}日 {use_time}关机！')
                print(set_timing)
