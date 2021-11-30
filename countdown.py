# -*- codeing -*-
# @Time : 2021/11/27 15:22
# @Author : Torres-圣君
# @File : countdown.py
# @Sofaware : PyCharm
# import os
import subprocess
import tkinter as tk
from tkinter import messagebox


class CountDownTime:
    def __init__(self):
        # 设置打开窗口规则
        self.count_custom_flag = True
        # 设置自定义时间默认值规则
        self.count = 1
        self.day = tk.IntVar()  # 定义天数
        self.hour = tk.IntVar()  # 定义小时
        self.minute = tk.IntVar()  # 定义分钟
        # 设置倒计时规则
        self.res_flag = False
        pass

    # 设置条件，令该窗口只能被创建一次
    def count_custom(self):
        if self.count_custom_flag:
            self.count_custom_flag = False
            # 创建子窗口，主窗口一旦关闭，子窗口连同一起关闭
            cdwin = tk.Toplevel()
            cdwin.title("自定义关机倒计时")
            cdwin.resizable(0, 0)
            sw = cdwin.winfo_screenwidth()
            sh = cdwin.winfo_screenheight()
            ww = 300
            wh = 100
            x = (sw - ww) / 2
            y = (sh - wh - 50) / 2
            cdwin.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
            # 设置天数倒计时
            day_text = tk.Label(cdwin, text="设置天数：")
            day_text.place(x=10, y=10)
            set_day = tk.Entry(cdwin, textvariable=self.day, width=10)
            set_day.place(x=80, y=10)
            # 设置小时倒计时
            hour_text = tk.Label(cdwin, text="设置小时：")
            hour_text.place(x=10, y=40)
            set_hour = tk.Entry(cdwin, textvariable=self.hour, width=10)
            set_hour.place(x=80, y=40)
            # 设置分钟倒计时
            minute_text = tk.Label(cdwin, text="设置分钟：")
            minute_text.place(x=10, y=70)
            set_minute = tk.Entry(cdwin, textvariable=self.minute, width=10)
            set_minute.place(x=80, y=70)
            # 固定追加的默认值
            if self.count:
                set_minute.insert(0, "1")
                self.count -= 1
            # 设置确定按钮
            ok_button = tk.Button(cdwin, text="确定", command=self.count_custom_time)
            ok_button.place(x=220, y=10)
            # cdwin.bind('<Return>', self.count_custom_time)
            # 设置取消按钮
            quit_button = tk.Button(cdwin, text="取消", command=lambda: (cdwin.destroy(), self.exit_cdwin()))
            quit_button.place(x=220, y=60)
            # cdwin.bind('<Escape>', lambda: (cdwin.destroy(), self.exit_cdwin()))
            # 设置点'X'后执行的内容
            cdwin.protocol('WM_DELETE_WINDOW', lambda: (cdwin.destroy(), self.exit_cdwin()))
            cdwin.mainloop()

    def exit_cdwin(self):
        # 点击'取消'或'X'后，将规则重回为True
        self.count_custom_flag = True

    def count_time_15(self):
        self.use_time_s(15)
        if self.res_flag:
            messagebox.showinfo(title='关机提醒', message='该计算机将于00小时15分00秒后关机！')

    def count_time_30(self):
        self.use_time_s(30)
        if self.res_flag:
            messagebox.showinfo(title='关机提醒', message='该计算机将于00小时30分00秒后关机！')

    def count_time_60(self):
        self.use_time_s(60)
        if self.res_flag:
            messagebox.showinfo(title='关机提醒', message='该计算机将于01小时00分00秒后关机！')

    def count_time_90(self):
        self.use_time_s(90)
        if self.res_flag:
            messagebox.showinfo(title='关机提醒', message='该计算机将于01小时30分00秒后关机！')

    # 15、30、60、90定时关机函数
    def use_time_s(self, use_time):
        self.res_flag = messagebox.askokcancel("关机提醒", message=f"确定要设置{use_time}分钟后关机吗？")
        if self.res_flag:
            time_s = use_time * 60
            # os.system(f"Windows定时关机 -s -t {time_s}")
            subprocess.run(f"shutdown -s -t {time_s}",
                           shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    # 用户自定义关机函数
    def count_custom_time(self):
        # 判断用户输入的值是否合法
        try:
            if 0 <= self.day.get() < 7 and 0 <= self.hour.get() < 24 and 0 <= self.minute.get() < 60:
                self.res_flag = messagebox.askokcancel("关机提醒", message="确定要设置在%02d天%02d小时%02d分钟后关机吗？" %
                                                                       (self.day.get(), self.hour.get(), self.minute.get()))
                if self.res_flag:
                    time_m = (self.day.get() * 24 * 60 * 60) + (self.hour.get() * 60 * 60) + (self.minute.get() * 60)
                    # os.system(f"Windows定时关机 -s -t {time_m}")
                    subprocess.run(f"shutdown -s -t {time_m}",
                                   shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
                    messagebox.showinfo(title='关机提醒', message='该计算机将于%02d天%02d小时%02d分00秒后关机！' %
                                                              (self.day.get(), self.hour.get(), self.minute.get()))
            elif 7 < self.day.get() < 99 and 0 <= self.hour.get() < 24 and 0 <= self.minute.get() < 60:
                self.res_flag = messagebox.askokcancel("设置异常", message=f"兄弟，{self.day.get()}天......你这还需要关机？")
                if self.res_flag:
                    time_m = (self.day.get() * 24 * 60 * 60) + (self.hour.get() * 60 * 60) + (self.minute.get() * 60)
                    # os.system(f"Windows定时关机 -s -t {time_m}")
                    subprocess.run(f"shutdown -s -t {time_m}",
                                   shell=True,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
                    messagebox.showinfo(title='关机提醒', message='该计算机将于%02d天%02d小时%02d分00秒后关机！' %
                                                              (self.day.get(), self.hour.get(), self.minute.get()))
            elif self.day.get() > 99:
                messagebox.showerror(title='设置异常', message=f'{self.day.get()}天......过分了哈，想都别想！')
            else:
                messagebox.showerror(title='设置异常', message='您的输入超出范围，请设置正确的值！')
        except Exception as re:
            messagebox.showerror(title='设置异常', message='您的输入有误，请输入正整数！')
            print(re)
