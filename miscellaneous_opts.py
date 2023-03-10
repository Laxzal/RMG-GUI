import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk


class miscellaneousOptions(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 13 frames
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
        self.frame12 = ttk.Frame(self.master)
        self.frame12.grid(row=12, column=0, sticky='nsew')


        # Create a tick box in gui to use miscellaneous options
        self.use_miscellaneous_options = tk.BooleanVar()
        self.use_miscellaneous_options.set(0)
        self.use_miscellaneous_options_check = tk.Checkbutton(self.frame0, text="Use Miscellaneous Options", variable=self.use_miscellaneous_options)
        self.use_miscellaneous_options_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a label called Name with an entry box that is set to 'Seed'
        self.name_label = ttk.Label(self.frame1, text="Name")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.frame1)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.name_entry.insert(0, 'Seed')

        #Create a label called generateSeedEachIteration with a drop down menu of '', True and False
        self.generate_seed_each_iteration_label = ttk.Label(self.frame2, text="generateSeedEachIteration")
        self.generate_seed_each_iteration_label.grid(row=0, column=0, padx=5, pady=5)
        self.generate_seed_each_iteration = tk.StringVar()
        self.generate_seed_each_iteration.set('')
        self.generate_seed_each_iteration_menu = ttk.OptionMenu(self.frame2, self.generate_seed_each_iteration, '', 'True', 'False')
        self.generate_seed_each_iteration_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called saveSeedToDatabase with a drop down menu of '', True and False
        self.save_seed_to_database_label = ttk.Label(self.frame3, text="saveSeedToDatabase")
        self.save_seed_to_database_label.grid(row=0, column=0, padx=5, pady=5)
        self.save_seed_to_database = tk.StringVar()
        self.save_seed_to_database.set('')
        self.save_seed_to_database_menu = ttk.OptionMenu(self.frame3, self.save_seed_to_database, '', 'True', 'False')
        self.save_seed_to_database_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called units with an entry box set to 'si'
        self.units_label = ttk.Label(self.frame4, text="units")
        self.units_label.grid(row=0, column=0, padx=5, pady=5)
        self.units_entry = ttk.Entry(self.frame4)
        self.units_entry.grid(row=0, column=1, padx=5, pady=5)
        self.units_entry.insert(0, 'si')

        #Create a label called generateOutputHTML with a drop down menu of '', True and False
        self.generate_output_html_label = ttk.Label(self.frame5, text="generateOutputHTML")
        self.generate_output_html_label.grid(row=0, column=0, padx=5, pady=5)
        self.generate_output_html = tk.StringVar()
        self.generate_output_html.set('')
        self.generate_output_html_menu = ttk.OptionMenu(self.frame5, self.generate_output_html, '', 'True', 'False')
        self.generate_output_html_menu.grid(row=0, column=1, padx=5, pady=5)

        #Create a label called generatePlots with a drop down menu of '', True and False
        self.generate_plots_label = ttk.Label(self.frame6, text="generatePlots")
        self.generate_plots_label.grid(row=0, column=0, padx=5, pady=5)
        self.generate_plots = tk.StringVar()
        self.generate_plots.set('')
        self.generate_plots_menu = ttk.OptionMenu(self.frame6, self.generate_plots, '', 'True', 'False')
        self.generate_plots_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called saveSimulationProfiles with a drop down menu of '', True and False
        self.save_simulation_profiles_label = ttk.Label(self.frame7, text="saveSimulationProfiles")
        self.save_simulation_profiles_label.grid(row=0, column=0, padx=5, pady=5)
        self.save_simulation_profiles = tk.StringVar()
        self.save_simulation_profiles.set('')
        self.save_simulation_profiles_menu = ttk.OptionMenu(self.frame7, self.save_simulation_profiles, '', 'True', 'False')
        self.save_simulation_profiles_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called verboseComments with a drop down menu of '', True and False
        self.verbose_comments_label = ttk.Label(self.frame8, text="verboseComments")
        self.verbose_comments_label.grid(row=0, column=0, padx=5, pady=5)
        self.verbose_comments = tk.StringVar()
        self.verbose_comments.set('')
        self.verbose_comments_menu = ttk.OptionMenu(self.frame8, self.verbose_comments, '', 'True', 'False')
        self.verbose_comments_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called saveEdgeSpecies with a drop down menu of '', True and False
        self.save_edge_species_label = ttk.Label(self.frame9, text="saveEdgeSpecies")
        self.save_edge_species_label.grid(row=0, column=0, padx=5, pady=5)
        self.save_edge_species = tk.StringVar()
        self.save_edge_species.set('')
        self.save_edge_species_menu = ttk.OptionMenu(self.frame9, self.save_edge_species, '', 'True', 'False')
        self.save_edge_species_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called keepIrreversible with a drop down menu of '', True and False
        self.keep_irreversible_label = ttk.Label(self.frame10, text="keepIrreversible")
        self.keep_irreversible_label.grid(row=0, column=0, padx=5, pady=5)
        self.keep_irreversible = tk.StringVar()
        self.keep_irreversible.set('')
        self.keep_irreversible_menu = ttk.OptionMenu(self.frame10, self.keep_irreversible, '', 'True', 'False')
        self.keep_irreversible_menu.grid(row=0, column=1, padx=5, pady=5)

        # Creaye a label called trimolecularProductReversible with a drop down menu of '', True and False
        self.trimolecular_product_reversible_label = ttk.Label(self.frame11, text="trimolecularProductReversible")
        self.trimolecular_product_reversible_label.grid(row=0, column=0, padx=5, pady=5)
        self.trimolecular_product_reversible = tk.StringVar()
        self.trimolecular_product_reversible.set('')
        self.trimolecular_product_reversible_menu = ttk.OptionMenu(self.frame11, self.trimolecular_product_reversible, '', 'True', 'False')
        self.trimolecular_product_reversible_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create a label called saveSeedModules with an entry box that takes only integers
        self.save_seed_modules_label = ttk.Label(self.frame12, text="saveSeedModules")
        self.save_seed_modules_label.grid(row=0, column=0, padx=5, pady=5)
        self.save_seed_modules_entry = ttk.Entry(self.frame12)
        self.save_seed_modules_entry.grid(row=0, column=1, padx=5, pady=5)
        self.save_seed_modules_entry.insert(0, '-1')

    def generate_options(self):
        
        if self.use_miscellaneous_options.get() == 1:
            # Get all the values from the entry boxes
            self.name_value = self.name_entry.get() if self.name_entry.get() != '' else None
            self.generate_seed_each_iteration_menu_value = self.generate_seed_each_iteration.get() if self.generate_seed_each_iteration.get() != '' else None
            self.save_seed_to_database_menu_value = self.save_seed_to_database.get() if self.save_seed_to_database.get() != '' else None
            self.units_entry_value = self.units_entry.get() if self.units_entry.get() != '' else None
            self.generate_output_html_menu_value = self.generate_output_html.get() if self.generate_output_html.get() != '' else None
            self.generate_plots_menu_value = self.generate_plots.get() if self.generate_plots.get() != '' else None
            self.save_simulation_profiles_menu_value = self.save_simulation_profiles.get() if self.save_simulation_profiles.get() != '' else None
            self.verbose_comments_menu_value = self.verbose_comments.get() if self.verbose_comments.get() != '' else None
            self.save_edge_species_menu_value = self.save_edge_species.get() if self.save_edge_species.get() != '' else None
            self.keep_irreversible_menu_value = self.keep_irreversible.get() if self.keep_irreversible.get() != '' else None
            self.trimolecular_product_reversible_menu_value = self.trimolecular_product_reversible.get() if self.trimolecular_product_reversible.get() != '' else None
            self.save_seed_modules_entry_value = self.save_seed_modules_entry.get() if self.save_seed_modules_entry.get() != '' else None
            
            # Return all values in a dictionary
            return {'name': self.name_value,
                    'generateSeedEachIteration': self.generate_seed_each_iteration_menu_value,
                    'saveSeedToDatabase': self.save_seed_to_database_menu_value,
                    'units': self.units_entry_value,
                    'generateOutputHTML': self.generate_output_html_menu_value,
                    'generatePlots': self.generate_plots_menu_value,
                    'saveSimulationProfiles': self.save_simulation_profiles_menu_value,
                    'verboseComments': self.verbose_comments_menu_value,
                    'saveEdgeSpecies': self.save_edge_species_menu_value,
                    'keepIrreversible': self.keep_irreversible_menu_value,
                    'trimolecularProductReversible': self.trimolecular_product_reversible_menu_value,
                    'saveSeedModulus': self.save_seed_modules_entry_value}
        else:
            return None
            