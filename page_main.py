# page_main.py
import tkinter as tk
import setting as S
from page import Page


class MYGUI:
    def __init__(self, root):
        self.root = root
        root.title("MYGUI")
        root.geometry(f"{S.window_width}x{S.window_height}+{S.x}+{S.y}")

        # 创建界面容器
        self.page_frame = tk.Frame(self.root)
        self.page1_frame = tk.Frame(self.root)

        # 主界面
        self.label1 = tk.Label(self.page_frame, text="请按需求点击下面的两个按钮", height=2)
        self.label1.pack()
        self.button1 = tk.Button(self.page_frame, text="奇数和", height=2, width=20, command=self.check_button1)
        self.button1.pack()
        self.button2 = tk.Button(self.page_frame, text="判断质数", height=2, width=20, command=self.check_button2)
        self.button2.pack()
        self.label2 = tk.Label(self.page_frame, justify="left", text="1、输入一个正整数，求不包括它自己前面\n" + "所有的奇数的平方和。\n"+"2、输入一个正整数，判断它是否为质数。")
        self.label2.pack()

        # 初始时只显示主界面
        self.page_frame.pack()
        self.page1_frame.pack_forget()

        self.my_page1 = Page(self.page_frame, self.page1_frame, '1')
        self.my_page2 = Page(self.page_frame, self.page1_frame, '2')

    def check_button1(self):
        self.page1_frame = tk.Frame(self.root)
        self.my_page1 = Page(self.page_frame, self.page1_frame, '1')
        self.my_page1.run()

    def check_button2(self):
        self.page1_frame = tk.Frame(self.root)
        self.my_page2 = Page(self.page_frame, self.page1_frame, '2')
        self.my_page2.run()

    def run(self):
        self.root.mainloop()
