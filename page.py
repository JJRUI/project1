# page.py
import random
import setting as S
import tkinter as tk


class Page:
    def __init__(self, page_frame, page1_frame, string):
        self.string = string
        self.page_frame = page_frame
        self.page1_frame = page1_frame

        # 创建标签和输入框
        self.label = tk.Label(self.page1_frame, text="请输入一个正整数:", height=2)
        self.entry = tk.Entry(self.page1_frame)

        # 创建按钮
        self.return_button = tk.Button(self.page1_frame, justify="left", text=" < ", height=1, width=3, command=self.check_return)
        if self.string == '1':
            self.button1 = tk.Button(self.page1_frame, text="求和", height=2, width=20, command=self.check_button1)
        elif self.string == '2':
            self.button1 = tk.Button(self.page1_frame, text="检查是否为质数", height=2, width=20, command=self.check_button1)

        self.button2 = tk.Button(self.page1_frame, text="随机生成一个正整数", height=2, width=20, command=self.check_button2)
        self.button3 = tk.Button(self.page1_frame, text="重新输入", height=2, width=20, command=self.check_button3)

        # 创建结果标签
        self.result_label = tk.Label(self.page1_frame, text="", height=2)

    def run(self):
        self.page_frame.pack_forget()
        self.page1_frame.pack()

        self.return_button.place(x=0, y=0)

        # 放置标签和输入框
        self.label.pack()
        self.entry.pack()

        # 放置按钮
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        # 放置结果标签
        self.result_label.pack()

    def check_return(self):
        self.page_frame.pack()
        self.page1_frame.destroy()

    # 处理按钮1点击事件
    def check_button1(self):
        input_number = self.entry.get()
        if input_number.isdigit():
            input_number = int(input_number)
            if self.string == '1':
                result = S.odd_sum(input_number)
                self.result_label.config(text=f"正整数{input_number}之前的所有奇数的平方和为:{result}")
            elif self.string == '2':
                result = S.judgment(input_number)
                self.result_label.config(text=f"结果为:{result}")
        else:
            self.result_label.config(text="请输入正整数")

    # 处理按钮2点击事件
    def check_button2(self):
        self.button1.config(state="disabled")
        self.entry.delete(0, 'end')
        string = str(random.randint(1, 2 ** 63 - 1))
        self.entry.insert(0, string)
        input_number = int(string)
        if self.string == '1':
            result = S.odd_sum(input_number)
            self.result_label.config(text=f"正整数{input_number}之前的所有奇数的平方和为:{result}")
        elif self.string == '2':
            result = S.judgment(input_number)
            self.result_label.config(text=f"结果为:{result}")

    # 处理按钮3点击事件
    def check_button3(self):
        self.button1.config(state='normal')
        self.entry.delete(0, "end")
        self.result_label.config(text="")
