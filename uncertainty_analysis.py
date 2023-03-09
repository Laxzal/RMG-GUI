import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class uncertaintyAnalysis(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 12 frames
        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, sticky='nsew')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, sticky='nsew')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=2, column=0, sticky='nsew')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=3, column=0, sticky='nsew')
        self.frame4 = ttk.Frame(self.master)
        self.frame4.grid(row=4, column=0, sticky='nsew')
        self.frame5 = ttk.Frame(self.master)
        self.frame5.grid(row=5, column=0, sticky='nsew')
        self.frame6 = ttk.Frame(self.master)
        self.frame6.grid(row=6, column=0, sticky='nsew')
        self.frame7 = ttk.Frame(self.master)
        self.frame7.grid(row=7, column=0, sticky='nsew')
        self.frame8 = ttk.Frame(self.master)
        self.frame8.grid(row=8, column=0, sticky='nsew')
        self.frame9 = ttk.Frame(self.master)
        self.frame9.grid(row=9, column=0, sticky='nsew')
        self.frame10 = ttk.Frame(self.master)
        self.frame10.grid(row=10, column=0, sticky='nsew')
        self.frame11 = ttk.Frame(self.master)
        self.frame11.grid(row=11, column=0, sticky='nsew')

        # Create a tick box in gui to use uncertainty analysis
        self.use_uncertainty_analysis = tk.BooleanVar()
        self.use_uncertainty_analysis.set(0)
        self.use_uncertainty_analysis_check = tk.Checkbutton(self.frame0, text="Use Uncertainty Analysis", variable=self.use_uncertainty_analysis)
        self.use_uncertainty_analysis_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a lable for local Analysis and drop down of options '' and True and False
        self.local_analysis_label = ttk.Label(self.frame1, text="Local Analysis")
        self.local_analysis_label.grid(row=0, column=0, padx=5, pady=5)
        self.local_analysis = tk.StringVar()
        self.local_analysis.set('')
        self.local_analysis_drop = ttk.OptionMenu(self.frame1, self.local_analysis, '', 'True', 'False')
        self.local_analysis_drop.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for global analysis and drop down of options '' and True and False
        self.global_analysis_label = ttk.Label(self.frame2, text="Global Analysis")
        self.global_analysis_label.grid(row=0, column=0, padx=5, pady=5)
        self.global_analysis = tk.StringVar()
        self.global_analysis.set('')
        self.global_analysis_drop = ttk.OptionMenu(self.frame2, self.global_analysis, '', 'True', 'False')
        self.global_analysis_drop.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for uncorrelated and a drop down of options '' and True and False
        self.uncorrelated_label = ttk.Label(self.frame3, text="Uncorrelated")
        self.uncorrelated_label.grid(row=0, column=0, padx=5, pady=5)
        self.uncorrelated = tk.StringVar()
        self.uncorrelated.set('')
        self.uncorrelated_drop = ttk.OptionMenu(self.frame3, self.uncorrelated, '', 'True', 'False')
        self.uncorrelated_drop.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for correlated and a drop down of options '' and True and False
        self.correlated_label = ttk.Label(self.frame4, text="Correlated")
        self.correlated_label.grid(row=0, column=0, padx=5, pady=5)
        self.correlated = tk.StringVar()
        self.correlated.set('')
        self.correlated_drop = ttk.OptionMenu(self.frame4, self.correlated, '', 'True', 'False')
        self.correlated_drop.grid(row=0, column=1, padx=5, pady=5)

        # create a label for local number and an entry box that takes an integer
        self.local_number_label = ttk.Label(self.frame5, text="Local Number")
        self.local_number_label.grid(row=0, column=0, padx=5, pady=5)
        self.local_number = tk.IntVar()
        self.local_number.set(0)
        self.local_number_entry = ttk.Entry(self.frame5, textvariable=self.local_number)
        self.local_number_entry.grid(row=0, column=1, padx=5, pady=5)

        # create a label for global number and an entry box that takes an integer
        self.global_number_label = ttk.Label(self.frame6, text="Global Number")
        self.global_number_label.grid(row=0, column=0, padx=5, pady=5)
        self.global_number = tk.IntVar()
        self.global_number.set(0)
        self.global_number_entry = ttk.Entry(self.frame6, textvariable=self.global_number)
        self.global_number_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a laebl for termmination time and an entry box that takes a float or integer
        self.termination_time_label = ttk.Label(self.frame7, text="Termination Time")
        self.termination_time_label.grid(row=0, column=0, padx=5, pady=5)
        self.termination_time = tk.DoubleVar()
        self.termination_time.set(0)
        self.termination_time_entry = ttk.Entry(self.frame7, textvariable=self.termination_time)
        self.termination_time_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for pceRunTime and an entry box that takes a float or integer
        self.pceRunTime_label = ttk.Label(self.frame8, text="PCE Run Time")
        self.pceRunTime_label.grid(row=0, column=0, padx=5, pady=5)
        self.pceRunTime = tk.DoubleVar()
        self.pceRunTime.set(0)
        self.pceRunTime_entry = ttk.Entry(self.frame8, textvariable=self.pceRunTime)
        self.pceRunTime_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for pceErrorTol and an entry box that takes a float or integer
        self.pceErrorTol_label = ttk.Label(self.frame9, text="PCE Error Tolerance")
        self.pceErrorTol_label.grid(row=0, column=0, padx=5, pady=5)
        self.pceErrorTol = tk.DoubleVar()
        self.pceErrorTol.set(0)
        self.pceErrorTol_entry = ttk.Entry(self.frame9, textvariable=self.pceErrorTol)
        self.pceErrorTol_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label for pceMaxEval and an entry box that takes an integer or None
        self.pceMaxEval_label = ttk.Label(self.frame10, text="PCE Max Eval")
        self.pceMaxEval_label.grid(row=0, column=0, padx=5, pady=5)
        self.pceMaxEval = tk.IntVar()
        self.pceMaxEval.set(0)
        self.pceMaxEval_entry = ttk.Entry(self.frame10, textvariable=self.pceMaxEval)
        self.pceMaxEval_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a label and a drop down menu of '' and True and False for logx
        self.logx_label = ttk.Label(self.frame11, text="Log X")
        self.logx_label.grid(row=0, column=0, padx=5, pady=5)
        self.logx = tk.StringVar()
        self.logx.set('')
        self.logx_drop = ttk.OptionMenu(self.frame11, self.logx, '', 'True', 'False')
        self.logx_drop.grid(row=0, column=1, padx=5, pady=5)
