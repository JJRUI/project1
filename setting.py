# setting.py
import pyautogui

screen_width, screen_height = pyautogui.size()
window_width = 300
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2


# 函数来判断一个整数是否为质数
def judgment(number):
    if number <= 1:
        return True
    if number <= 3:
        return False
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


def odd_sum(number):
    # odd_sum = 0  # 用于存储奇数的平方和
    if number == 1:
        odd_sum = 0
    else:
        n = int(number / 2)
        odd_sum = int(((4 * pow(n, 3)) - n) / 3)

    return odd_sum