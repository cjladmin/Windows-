# -*- codeing -*-
# @Time : 2021/11/27 14:27
# @Author : Torres-圣君
# @File : main.py
# @Sofaware : PyCharm
import base64
import ctypes
import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from countdown import CountDownTime
from timing import TimingTime
from get_image import *


# 定时关机
def timing_button():
    tt = TimingTime()
    timing['state'] = tk.DISABLED
    time_00 = tk.Button(win, text="00 : 00", width=5, command=tt.count_time_00)
    time_00.place(x=30, y=90)
    time_06 = tk.Button(win, text="06 : 00", width=5, command=tt.count_time_06)
    time_06.place(x=130, y=90)
    time_12 = tk.Button(win, text="12 : 00", width=5, command=tt.count_time_12)
    time_12.place(x=230, y=90)
    time_18 = tk.Button(win, text="18 : 00", width=5, command=tt.count_time_18)
    time_18.place(x=330, y=90)
    time_custom_timing = tk.Button(win, text="自定义", width=5, command=tt.timingcustom)
    time_custom_timing.place(x=430, y=90)


# 倒计时关机
def countdown_button():
    cdt = CountDownTime()
    countdown['state'] = tk.DISABLED
    time_15 = tk.Button(win, text="15min", width=5, command=cdt.count_time_15)
    time_15.place(x=30, y=130)
    time_30 = tk.Button(win, text="30min", width=5, command=cdt.count_time_30)
    time_30.place(x=130, y=130)
    time_60 = tk.Button(win, text="60min", width=5, command=cdt.count_time_60)
    time_60.place(x=230, y=130)
    time_90 = tk.Button(win, text="90min", width=5, command=cdt.count_time_90)
    time_90.place(x=330, y=130)
    time_custom_countdown = tk.Button(win, text="自定义", width=5, command=cdt.count_custom)
    time_custom_countdown.place(x=430, y=130)


# 取消关机
def quitdown_button():
    quit_res = messagebox.askokcancel('取消关机提醒', message=f'确定要取消关机任务吗？')
    if quit_res:
        res = subprocess.run("shutdown -a",
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        # if os.system("shutdown -a") == 1116:
        # print(res)
        if "returncode=1116" in str(res):
            messagebox.showerror(title="取消异常", message="该计算机暂无可取消的关机任务！")
        else:
            # 使用subprocess.run()执行cmd命令，去除黑窗口一闪而过
            subprocess.run("shutdown -a",
                           shell=True,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
            # os.system("shutdown -a")
            messagebox.showinfo(title="取消提醒", message="已取消定时关机任务！")


# 打开作者博客
def authorblog():
    subprocess.run("start www.cjlblog.vip",
                   shell=True,
                   stdin=subprocess.PIPE,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


# 获取最新版
def get_version():
    subprocess.run("start https://github.com/cjladmin/Windows-shutdown",
                   shell=True,
                   stdin=subprocess.PIPE,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)


if __name__ == '__main__':
    try:
        # 创建临时图片
        tmp = open(r'D:/favicon.ico', 'wb')  # 创建临时的文件
        tmp.write(base64.b64decode(favicon_ico))  # 把这个one图片解码出来，写入文件中去。
        tmp.close()
    except Exception as re:
        # 创建到文件所在目录
        tmp = open(r'favicon.ico', 'wb')  # 创建临时的文件
        tmp.write(base64.b64decode(favicon_ico))  # 把这个one图片解码出来，写入文件中去。
        tmp.close()
        print(re)

    # 任务栏图标依赖
    myappid = "company.product.version"  # 这里可以设置任意文本
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    win = tk.Tk()
    # 设置窗口名称
    win.title("定时关机程序-(以北京时间为准)")
    try:
        # 设置窗口图标
        win.iconbitmap(default="D:/favicon.ico")
        # 设置任务栏图标
        win.wm_iconbitmap('D:/favicon.ico')
    except Exception as re:
        win.iconbitmap(default="favicon.ico")
        win.wm_iconbitmap('favicon.ico')
        print(re)
    # 固定窗口大小
    win.resizable(0, 0)
    # 得到屏幕宽度
    sw = win.winfo_screenwidth()
    # 得到屏幕高度
    sh = win.winfo_screenheight()
    # 设置窗口宽500，高为200
    ww = 500
    wh = 200
    x = (sw - ww) / 2
    # 50为任务栏高度
    y = (sh - wh - 50) / 2
    win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    # 定时关机按钮
    timing = tk.Button(win, text="定时关机", command=timing_button)
    timing.place(x=80, y=30)
    # 倒计时关机按钮
    countdown = tk.Button(win, text="倒计时关机", command=countdown_button)
    countdown.place(x=210, y=30)
    # 取消关机按钮
    quitdown = tk.Button(win, text="取消关机", command=quitdown_button)
    quitdown.place(x=350, y=30)
    # 作者声明
    author = tk.Button(win, text="by Torres-圣君", font=('微软雅黑', 8), command=authorblog)
    author.place(x=415, y=175)
    # 版本号
    version = tk.Button(win, text="版本号：v1.0.1", font=('微软雅黑', 8), command=get_version)
    version.place(x=0, y=175)
    win.mainloop()
    try:
        try:
            os.remove('D:/favicon.ico')
        except Exception as re:
            os.remove('favicon.ico')
            print(re)
    except Exception as re:
        print(re)
