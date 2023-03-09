import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class simulatorTolerances(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.master = master

        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, sticky='nsew')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, sticky='nsew')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=2, column=0, sticky='nsew')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=1, column=1, sticky='nsew')
        self.frame4 = ttk.Frame(self.master)
        self.frame4.grid(row=2, column=1, sticky='nsew')


        # Create a tick box in gui to use Simulator Tolerances
        self.use_simulator_tolerances = tk.BooleanVar()
        self.use_simulator_tolerances.set(0)
        self.use_simulator_tolerances_check = tk.Checkbutton(self.frame0, text="Use Simulator Tolerances", variable=self.use_simulator_tolerances)
        self.use_simulator_tolerances_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a label and entry for atol
        self.atol_label = tk.Label(self.frame1, text='atol:')
        self.atol_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.atol_entry = tk.Entry(self.frame1, width=10)
        self.atol_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a label and entry for rtol
        self.rtol_label = tk.Label(self.frame2, text='rtol:')
        self.rtol_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.rtol_entry = tk.Entry(self.frame2, width=10)
        self.rtol_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a label and entry for sens_atol
        self.sens_atol_label = tk.Label(self.frame3, text='sens_atol:')
        self.sens_atol_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.sens_atol_entry = tk.Entry(self.frame3, width=10)
        self.sens_atol_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Create a label and entry for sens_rtol
        self.sens_rtol_label = tk.Label(self.frame4, text='sens_rtol:')
        self.sens_rtol_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.sens_rtol_entry = tk.Entry(self.frame4, width=10)
        self.sens_rtol_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
