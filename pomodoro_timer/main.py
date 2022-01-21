import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Pomodoro Timer')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='tomato.png'))

        self.s = ttk.Style()
        self.s.configure('TNotebook.Tab', font=('Ubuntu', 16))
        self.s.configure('TButton.Tab', font=('Ubuntu', 16))

        # Tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text='25:00', font=('Ubuntu', 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_brake_timer_label = ttk.Label(self.tab2, text='5:00', font=('Ubuntu', 48))
        self.short_brake_timer_label.pack(pady=20)

        self.long_brake_timer_label = ttk.Label(self.tab3, text='15:00', font=('Ubuntu', 48))
        self.long_brake_timer_label.pack(pady=20)

        # Attach tabs
        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Short Brake')
        self.tabs.add(self.tab3, text='Long Brake')

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text='Start', command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text='Skip', command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text='Reset', command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text='Pomordoros: 0', font=('Ubuntu', 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.root.mainloop()

    def start_timer_thread(self):
        pass

    def start_timer(self):
        pass

    def reset_clock(self):
        pass

    def skip_clock(self):
        pass


PomodoroTimer()
