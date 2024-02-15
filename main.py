# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# main.py
import page_main
import tkinter as tk


def main():
    root = tk.Tk()
    my_gui = page_main.MYGUI(root)
    my_gui.run()


if __name__ == "__main__":
    main()
