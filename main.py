from tkinter import *
from tkinter import ttk
from time import strftime


def main():
    # creating tkinter window
    root = Tk()
    root.title('Clock')
    # displaying time on the label
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000, time)

    # Clock label initialization and positioning
    lbl = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
    lbl.pack(anchor='center')

    time()
    root.mainloop()


if __name__ == '__main__':
    main()
