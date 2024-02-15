# main.py
import page_main
import tkinter as tk


def main():
    root = tk.Tk()
    my_gui = page_main.MYGUI(root)
    my_gui.run()


if __name__ == "__main__":
    main()
