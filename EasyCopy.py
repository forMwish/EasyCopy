#!/usr/bin/env python
# coding: utf-8
from system_hotkey import SystemHotkey
import pyperclip as pyclip
import time


# 剪贴板字符串处理
def StringProcess(self):
    # 读取字符串（剪贴板）
    read_text = pyclip.paste()
    # 字符串处理
    output_text = read_text.replace("\r\n", " ")
    output_text = output_text.replace("\n", " ")
    output_text = output_text.replace("\r", " ")
    # 输出字符串（剪贴板）
    pyclip.copy(output_text)

hk = SystemHotkey()
hk.register(('control', 'shift', 'm'), callback=StringProcess)

while (1):
    time.sleep(1000)
