import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class simpleReactor(tk.Frame):

    def __init__(self, master, species_tab) -> None:
        super().__init__()
        self.master = master

        self.frame0=ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, sticky='nswe', padx=5, pady=5)
        #self.frame0.grid_columnconfigure(0, weight=1)
        #Create a label in the GUI
        self.label = ttk.Label(self.frame0, text="Simple Reactor")
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')

        #Create a tick box in the GUI if the user wants to use a reactor
        self.reactor_var = tk.BooleanVar()
        self.reactor_var.set(0)
        self.reactor_check = tk.Checkbutton(self.frame0, text="Use simpleReactor", variable=self.reactor_var)
        self.reactor_check.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')

        # Create temperature label and two entry boxes - represent range of temperatures
        #frame1=ttk.Frame(self.master)
        self.temp_label = ttk.Label(self.frame0, text="Temperature (K):")
        self.temp_label.grid(row=1, column=2, padx=5, pady=5, sticky='nswe')
        self.temp_entry1 = ttk.Entry(self.frame0, width=10)
        self.temp_entry1.grid(row=1, column=3, padx=5, pady=5, sticky='nswe')
        self.temp_entry2 = ttk.Entry(self.frame0, width=10)
        self.temp_entry2.grid(row=1, column=4, padx=5, pady=5, sticky='nswe')

        # Create pressure label and two entry boxes - represent range of pressures
        #frame2=ttk.Frame(self.master)
        self.pressure_label = ttk.Label(self.frame0, text="Pressure (bar):")
        self.pressure_label.grid(row=2, column=2, padx=5, pady=5, sticky='nswe')
        self.pressure_entry1 = ttk.Entry(self.frame0, width=10)
        self.pressure_entry1.grid(row=2, column=3, padx=5, pady=5, sticky='nswe')
        self.pressure_entry2 = ttk.Entry(self.frame0, width=10)
        self.pressure_entry2.grid(row=2, column=4, padx=5, pady=5, sticky='nswe')

        # Create nSims label and entry box
        #frame3=ttk.Frame(self.master)
        self.nSims_label = ttk.Label(self.frame0, text="Number of simulations:")
        self.nSims_label.grid(row=3, column=2, padx=5, pady=5, sticky='nswe')
        self.nSims_entry = ttk.Entry(self.frame0, width=10)
        self.nSims_entry.grid(row=3, column=3, padx=5, pady=5, sticky='nswe')

        # Create initial mole fraction label and entry box
        # Create a button that generates the species list
        self.species_button = ttk.Button(self.frame0, text="Generate species list", command=self.generate_species)
        self.species_button.grid(row=4, column=0, padx=5, pady=5, sticky='nswe')
        self.species_tab = species_tab



        # Create terminateConversion checkbox and entry boxes
        self.terminateConversion_label = ttk.Label(self.frame0, text="Terminate conversion:", justify=tk.CENTER, width=20)
        self.terminateConversion_label.grid(row=1, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateConversion_var = tk.BooleanVar()
        self.terminateConversion_check = tk.Checkbutton(self.frame0, text="Use terminateConversion", variable=self.terminateConversion_var,
                                                         command=self.show_terminateConversion)
        self.terminateConversion_check.grid(row=1, column=8, padx=5, pady=5, sticky='w')

        # Create terminateTime checkbox and entry boxes
        self.terminateTime_label = ttk.Label(self.frame0, text="Terminate time:",  justify=tk.CENTER, width=20)
        self.terminateTime_label.grid(row=14, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateTime_var = tk.BooleanVar()
        self.terminateTime_check = tk.Checkbutton(self.frame0, text="Use terminateTime", variable=self.terminateTime_var, 
                                                  command=self.show_terminateTime)
        self.terminateTime_check.grid(row=14, column=8, padx=5, pady=5, sticky='w')

        # Create terminateRate checkbox and entry boxes
        self.terminateRate_label = ttk.Label(self.frame0, text="Terminate rate:",  justify=tk.CENTER, width =20)
        self.terminateRate_label.grid(row=16, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateRate_var = tk.BooleanVar()
        self.terminateRate_check = tk.Checkbutton(self.frame0, text="Use terminateRateRatio", variable=self.terminateRate_var, 
                                                  command=self.show_terminateRate)
        self.terminateRate_check.grid(row=16, column=8, padx=5, pady=5, sticky='w')


        # Create Sensitivity checkbox and listbox
        self.sensitivity_label = ttk.Label(self.frame0, text="Sensitivity",  justify=tk.CENTER, width=20, anchor='center')
        self.sensitivity_label.grid(row=1, column=10, padx=5, pady=5, sticky='we')
        self.sensitivity_var = tk.BooleanVar()
        self.sensitivity_check = tk.Checkbutton(self.frame0, text="Use sensitivity", variable=self.sensitivity_var, 
                                                command=self.show_sensitivity)
        self.sensitivity_left_listbox_label = ttk.Label(self.frame0, text="Unselected Species:",  justify=tk.CENTER, width=20)
        self.sensitivity_left_listbox_label.grid(row=2, column=10, padx=5, pady=5, sticky='nswe')
        self.sensitivity_right_listbox_label = ttk.Label(self.frame0, text="Selected Species:",  justify=tk.CENTER, width=20)
        self.sensitivity_right_listbox_label.grid(row=2, column=12, padx=5, pady=5, sticky='nswe')
        
        self.sensitivity_left_listbox = tk.Listbox(self.frame0, selectmode=tk.MULTIPLE, width=20)
        self.sensitivity_right_listbox = tk.Listbox(self.frame0, selectmode=tk.MULTIPLE, width=20)
        
        
        self.list_of_species = []
        self.species = []
    def generate_species(self):
        self.species = self.species_tab.generate_field_reactor()

        #frame4=ttk.Frame(self.master)
        self.moleFrac_label = ttk.Label(self.frame0, text="Initial mole fraction:")
        self.moleFrac_label.grid(row=4, column=2, padx=5, pady=5, sticky='nswe')

        for i, species in enumerate(self.species):
            self.moleFrac_label = ttk.Label(self.frame0, text=species)
            self.moleFrac_label.grid(row=i+5, column=2, padx=5, pady=5, sticky='nswe')
            self.moleFrac_entry = ttk.Entry(self.frame0, width=10)
            self.moleFrac_entry.grid(row=i+5, column=3, padx=5, pady=5, sticky='nswe')
    
    def show_terminateConversion(self):
        if self.terminateConversion_var.get() == 1:
            self.terminateConversion_label.grid(row=1, column=7, padx=5, pady=5, sticky='nswe')
            self.terminateConversion_check.grid(row=1, column=8, padx=5, pady=5, sticky='nswe')
            self.generate_terminateConversion()
        else:
            #self.terminateConversion_label.grid_forget()
            #self.terminateConversion_check.grid_forget()
            if self.list_of_species:
                for widget in self.list_of_species:
                    widget.grid_forget()
            self.moleFrac_label.grid_forget()
            self.moleFrac_entry.grid_forget()

    def generate_terminateConversion(self):
        self.species = self.species_tab.generate_field_reactor()
        
        
        for i, species in enumerate(self.species):
            self.moleFrac_label = ttk.Combobox(self.frame0, textvariable=species, values=self.species)
            self.moleFrac_label.grid(row=i+2, column=8, padx=5, pady=5, sticky='nswe')
            self.moleFrac_entry = ttk.Entry(self.frame0, width=10)
            self.moleFrac_entry.grid(row=i+2, column=9, padx=5, pady=5, sticky='nswe')

            self.list_of_species.append(self.moleFrac_label)
            self.list_of_species.append(self.moleFrac_entry)
    
    def show_terminateTime(self):
        if self.terminateTime_var.get() == 1:
            self.terminatetime_true_label = ttk.Label(self.frame0, text="Seconds:")
            self.terminatetime_true_label.grid(row=15, column=7, padx=5, pady=5, sticky='nswe')
            self.terminateTime_true_entry = ttk.Entry(self.frame0, width=10)
            self.terminateTime_true_entry.grid(row=15, column=8, padx=5, pady=5, sticky='nswe')
        else:
            self.terminatetime_true_label.grid_forget()
            self.terminateTime_true_entry.grid_forget()

    def show_terminateRate(self):
        if self.terminateRate_var.get() == 1:
            self.terminaterate_true_label = ttk.Label(self.frame0, text="Ratio:")
            self.terminaterate_true_label.grid(row=17, column=7, padx=5, pady=5, sticky='nswe')
            self.terminaterate_true_entry = ttk.Entry(self.frame0, width=10)
            self.terminaterate_true_entry.grid(row=17, column=8, padx=5, pady=5, sticky='nswe')
        else:
            self.terminaterate_true_label.grid_forget()
            self.terminaterate_true_entry.grid_forget()

    def show_sensitivity(self):
        
        if self.sensitivity_var.get() == 1:
            self.sensitivity_left_listbox.grid(row=3, column=10, padx=5, pady=5, sticky='nswe')
            self.sensitivity_right_listbox.grid(row=3, column=12, padx=5, pady=5, sticky='nswe')
            self.generate_sensitivity()
        else:
            self.sensitivity_left_listbox.grid_forget()
            self.sensitivity_right_listbox.grid_forget()
    
    def generate_sensitivity(self):
        self.species = self.species_tab.generate_field_reactor()
        for i, species in enumerate(self.species):
            self.sensitivity_left_listbox.insert(i, species)
    