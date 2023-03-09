import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk


class simpleReactor(ctk.CTkFrame):

    def __init__(self, master, species_tab) -> None:
        super().__init__(master)
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
        self.frame_terminate = ttk.Frame(self.master)
        self.frame_terminate.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')
        self.terminateConversion_label = ttk.Label(self.frame_terminate, text="Terminate conversion:", justify=tk.CENTER, width=20)
        self.terminateConversion_label.grid(row=1, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateConversion_var = tk.BooleanVar()
        self.terminateConversion_check = tk.Checkbutton(self.frame_terminate, text="Use terminateConversion", variable=self.terminateConversion_var,
                                                         command=self.show_terminateConversion)
        self.terminateConversion_check.grid(row=1, column=8, padx=5, pady=5, sticky='w')

        # Create terminateTime checkbox and entry boxes
        self.terminateTime_label = ttk.Label(self.frame_terminate, text="Terminate time:",  justify=tk.CENTER, width=20)
        self.terminateTime_label.grid(row=14, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateTime_var = tk.BooleanVar()
        self.terminateTime_check = tk.Checkbutton(self.frame_terminate, text="Use terminateTime", variable=self.terminateTime_var, 
                                                  command=self.show_terminateTime)
        self.terminateTime_check.grid(row=14, column=8, padx=5, pady=5, sticky='w')

        # Create terminateRate checkbox and entry boxes
        self.terminateRate_label = ttk.Label(self.frame_terminate, text="Terminate rate:",  justify=tk.CENTER, width =20)
        self.terminateRate_label.grid(row=16, column=7, padx=5, pady=5, sticky='nswe')
        self.terminateRate_var = tk.BooleanVar()
        self.terminateRate_check = tk.Checkbutton(self.frame_terminate, text="Use terminateRateRatio", variable=self.terminateRate_var, 
                                                  command=self.show_terminateRate)
        self.terminateRate_check.grid(row=16, column=8, padx=5, pady=5, sticky='w')


        # Create Sensitivity checkbox and listbox
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
        self.sensitivity_label = ttk.Label(self.frame1, text="Sensitivity",  justify=tk.CENTER, width=5,)
        self.sensitivity_label.grid(row=1, column=10, padx=5, pady=5, sticky='we', columnspan=1)
        self.sensitivity_var = tk.BooleanVar()
        self.sensitivity_check = tk.Checkbutton(self.frame1, text="Use sensitivity", variable=self.sensitivity_var, 
                                                command=self.show_sensitivity)
        self.sensitivity_check.grid(row=1, column=12, padx=5, pady=5, sticky='w')
        self.sensitivity_left_listbox_label = ttk.Label(self.frame1, text="Unselected Species:",  justify=tk.CENTER, width=20)
        self.sensitivity_left_listbox_label.grid(row=2, column=10, padx=5, pady=5, sticky='nswe')
        self.sensitivity_right_listbox_label = ttk.Label(self.frame1, text="Selected Species:",  justify=tk.CENTER, width=20)
        self.sensitivity_right_listbox_label.grid(row=2, column=12, padx=5, pady=5, sticky='nswe')
        
        self.sensitivity_left_listbox = tk.Listbox(self.frame1, selectmode=tk.MULTIPLE, width=20)
        self.sensitivity_right_listbox = tk.Listbox(self.frame1, selectmode=tk.MULTIPLE, width=20)
        # Sensitivty buttons left to right
        self.sensitivity_left_to_right_button = ttk.Button(self.frame1, text=">>", command=self.sensitivity_left_to_right)
        # Sensitivty buttons right to left
        self.sensitivity_right_to_left_button = ttk.Button(self.frame1, text="<<", command=self.sensitivity_right_to_left)

        
        # Create Sesnitivity threshold label and entry box
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=1, column=1, padx=5, pady=5, sticky='we')
        self.sensitivity_threshold_label = ttk.Label(self.frame2, text="Sensitivity threshold",  justify=tk.CENTER, width=22)
        self.sensitivity_threshold_label.grid(row=0, column=0, padx=10, pady=5, sticky='nswe')
        self.sensitivity_threshold_entry = ttk.Entry(self.frame2, width=5)
        self.sensitivity_threshold_entry.grid(row=0, column=1, padx=5, pady=5, sticky='we')
        
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
            if self.list_of_species:
                for widget in self.list_of_species:
                    widget.grid_forget()
            self.moleFrac_label.grid_forget()
            self.moleFrac_entry.grid_forget()

    def generate_terminateConversion(self):
        self.species = self.species_tab.generate_field_reactor()
        
        
        for i, species in enumerate(self.species):
            self.moleFrac_label = ttk.Combobox(self.frame_terminate, textvariable=species, values=self.species)
            self.moleFrac_label.grid(row=i+2, column=8, padx=5, pady=5, sticky='nswe')
            self.moleFrac_entry = ttk.Entry(self.frame_terminate, width=10)
            self.moleFrac_entry.grid(row=i+2, column=9, padx=5, pady=5, sticky='nswe')

            self.list_of_species.append(self.moleFrac_label)
            self.list_of_species.append(self.moleFrac_entry)
    
    def show_terminateTime(self):
        if self.terminateTime_var.get() == 1:
            self.terminatetime_true_label = ttk.Label(self.frame_terminate, text="Seconds:")
            self.terminatetime_true_label.grid(row=15, column=7, padx=5, pady=5, sticky='nswe')
            self.terminateTime_true_entry = ttk.Entry(self.frame_terminate, width=10)
            self.terminateTime_true_entry.grid(row=15, column=8, padx=5, pady=5, sticky='nswe')
        else:
            self.terminatetime_true_label.grid_forget()
            self.terminateTime_true_entry.grid_forget()

    def show_terminateRate(self):
        if self.terminateRate_var.get() == 1:
            self.terminaterate_true_label = ttk.Label(self.frame_terminate, text="Ratio:")
            self.terminaterate_true_label.grid(row=17, column=7, padx=5, pady=5, sticky='nswe')
            self.terminaterate_true_entry = ttk.Entry(self.frame_terminate, width=10)
            self.terminaterate_true_entry.grid(row=17, column=8, padx=5, pady=5, sticky='nswe')
        else:
            self.terminaterate_true_label.grid_forget()
            self.terminaterate_true_entry.grid_forget()

    def show_sensitivity(self):
        
        if self.sensitivity_var.get() == 1:
            self.sensitivity_left_listbox.grid(row=3, column=10, padx=5, pady=5, sticky='nswe', rowspan=2)
            self.sensitivity_right_listbox.grid(row=3, column=12, padx=5, pady=5, sticky='nswe', rowspan=2)

            self.sensitivity_left_to_right_button.grid(row=3, column=11, padx=5, pady=5, sticky='nswe')
            self.sensitivity_right_to_left_button.grid(row=4, column=11, padx=5, pady=5, sticky='nswe')
            self.generate_sensitivity()
        else:
            self.sensitivity_left_listbox.delete(0, tk.END)
            self.sensitivity_right_listbox.delete(0, tk.END)
            self.sensitivity_left_to_right_button.grid_forget()
            self.sensitivity_right_to_left_button.grid_forget()
            self.sensitivity_left_listbox.grid_forget()
            self.sensitivity_right_listbox.grid_forget()
            
    
    def generate_sensitivity(self):
        self.species = self.species_tab.generate_field_reactor()
        for i, species in enumerate(self.species):
            self.sensitivity_left_listbox.insert(i, species)
    
    def sensitivity_left_to_right(self):
        for i in self.sensitivity_left_listbox.curselection():
            self.sensitivity_right_listbox.insert(tk.END, self.sensitivity_left_listbox.get(i))
            self.sensitivity_left_listbox.delete(i)
    
    def sensitivity_right_to_left(self):
        for i in self.sensitivity_right_listbox.curselection():
            self.sensitivity_left_listbox.insert(tk.END, self.sensitivity_right_listbox.get(i))
            self.sensitivity_right_listbox.delete(i)

class liquidReactor(ctk.CTkFrame):

    def __init__(self, master,species_tab, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')


        # Create a tick box to use liquid reactor
        #Create a tick box in the GUI if the user wants to use a reactor
        self.reactor_var = tk.BooleanVar()
        self.reactor_var.set(0)
        self.reactor_check = tk.Checkbutton(self.frame0, text="Use liquidReactor", variable=self.reactor_var)
        self.reactor_check.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')

        # Create temperature label and two entry boxes, represeting range
        self.temperature_label = ttk.Label(self.frame0, text="Temperature (K):")
        self.temperature_label.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
        self.temperature_entry1 = ttk.Entry(self.frame0, width=10)
        self.temperature_entry1.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')

        # Add a separator between the two entry boxes
        separator = ttk.Separator(self.frame0, orient='horizontal')
        separator.grid(row=1, column=2, padx=5, pady=5, sticky='we', columnspan=1)

        self.temperature_entry2 = ttk.Entry(self.frame0, width=10)
        self.temperature_entry2.grid(row=1, column=3, padx=5, pady=5, sticky='nswe')


        # Create initial concentration of species label with tdrop down boxes in frame 1\
        self.initial_concentration_label = ttk.Label(self.frame1, text="Initial concentration (mol/m^3):")
        self.initial_concentration_label.grid(row=0, column=0, padx=5, pady=5, sticky='nswe')
        self.initial_concentration_var = tk.BooleanVar()
        self.initial_concentration_var.set(0)
        self.initial_concentration_check = tk.Checkbutton(self.frame1, text="Use initial concentration", variable=self.initial_concentration_var, command=self.show_initial_conc)
        self.initial_concentration_check.grid(row=0, column=1, padx=5, pady=5, sticky='nswe')

        self.list_of_species =[]
        self.list_of_species_terminateConversion = []
        #show terminateconversion label and entry box
        self.terminateConversion_label = ttk.Label(self.frame2, text="Terminate conversion", justify=tk.CENTER, width=25)
        self.terminateConversion_label.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
        self.terminateConversion_var = tk.BooleanVar()
        self.terminateConversion_check = tk.Checkbutton(self.frame2, text="Use terminateConversion", variable=self.terminateConversion_var,
                                                         command=self.show_terminateConversion)
        self.terminateConversion_check.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Show terminate time label and entry box
        self.terminateTime_label = ttk.Label(self.frame3, text="Terminate time (s)", justify=tk.CENTER, width=25)
        self.terminateTime_label.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')
        self.terminateTime_var = tk.BooleanVar()
        self.terminateTime_check = tk.Checkbutton(self.frame3, text="Use terminateTime", variable=self.terminateTime_var,
                                                            command=self.show_terminateTime)
        self.terminateTime_check.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        

        #Species tab
        self.species_tab = species_tab
    def show_initial_conc(self):
        if self.initial_concentration_var.get() == 1:
            self.generate_species()
        else:
            if self.list_of_species:
                for widget in self.list_of_species:
                    widget.grid_forget()
            self.moleFrac_label.grid_forget()
            self.moleFrac_entry.grid_forget()

    def generate_species(self):
        self.species = self.species_tab.generate_field_reactor()
        

        for i, species in enumerate(self.species):
            self.moleFrac_label = ttk.Combobox(self.frame1, textvariable=species, values=self.species)
            self.moleFrac_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='nswe')
            self.moleFrac_entry = ttk.Entry(self.frame1, width=10)
            self.moleFrac_entry.grid(row=i+2, column=1, padx=5, pady=5, sticky='nswe')

            self.list_of_species.append(self.moleFrac_label)
            self.list_of_species.append(self.moleFrac_entry)

    def show_terminateConversion(self):
        if self.terminateConversion_var.get() == 1:
            self.terminateConversion_label.grid(row=1, column=0, padx=5, pady=5, sticky='nswe')
            self.terminateConversion_check.grid(row=1, column=1, padx=5, pady=5, sticky='nswe')
            self.generate_terminateConversion()
        else:
            if self.list_of_species_terminateConversion:
                for widget in self.list_of_species_terminateConversion:
                    widget.grid_forget()
            self.moleFrac_label.grid_forget()
            self.moleFrac_entry.grid_forget()

    def generate_terminateConversion(self):
        self.species = self.species_tab.generate_field_reactor()
        
        
        for i, species in enumerate(self.species):
            self.moleFrac_label = ttk.Combobox(self.frame2, textvariable=species, values=self.species)
            self.moleFrac_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='nswe')
            self.moleFrac_entry = ttk.Entry(self.frame2, width=10)
            self.moleFrac_entry.grid(row=i+2, column=1, padx=5, pady=5, sticky='nswe')
            self.list_of_species_terminateConversion.append(self.moleFrac_label)
            self.list_of_species_terminateConversion.append(self.moleFrac_entry)
    def show_terminateTime(self):
        if self.terminateTime_var.get() == 1:
            self.terminatetime_true_label = ttk.Label(self.frame3, text="Seconds:")
            self.terminatetime_true_label.grid(row=3, column=0, padx=5, pady=5, sticky='nswe')
            self.terminateTime_true_entry = ttk.Entry(self.frame3, width=10)
            self.terminateTime_true_entry.grid(row=3, column=1, padx=5, pady=5, sticky='nswe')
        else:
            self.terminatetime_true_label.grid_forget()
            self.terminateTime_true_entry.grid_forget()