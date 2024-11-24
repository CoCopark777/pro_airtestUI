# -*- coding: utf-8 -*-
"""

1-打开浏览器
2-输入账号密码
3-点击登录

"""
import sys
# print(sys.getdefaultencoding())
import os
import time

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Windows:///",])

# touch(Template(r"C:/Users/Administrator/Desktop/airtest/登录页面.air/tpl1732027205703.png", record_pos=(-0.399, -0.038), resolution=(2560, 1080)))
# time.sleep(3)
# # 定义谷歌浏览器的路径
# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # 根据您的实际安装路径修改
#
# # 打开指定网址
# os.system(f'"{chrome_path}" "https://www.example.com"')
import webbrowser

# 打开谷歌首页
webbrowser.open('https://www.saucedemo.com/')
touch(Template(r"C:/Users/Administrator/Desktop/airtest/登录页面.air/tpl1732071939147.png", target_pos=9, record_pos=(-0.448, -0.195), resolution=(2560, 1080)))
sleep(3)
import win32api
import win32con
import win32clipboard

def get_selected_text():
    # 模拟 Ctrl + C 操作来获取选中的文本
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    win32api.keybd_event(ord('C'), 0, 0, 0)
    win32api.keybd_event(ord('C'), 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 从剪贴板获取文本
    win32clipboard.OpenClipboard()
    selected_text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return selected_text

print(get_selected_text())