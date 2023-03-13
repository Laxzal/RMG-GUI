import tkinter as tk
from tkinter import ttk
from src.species_tab import Species
from src.generatefile_tab import GenerateFile
from src.datasource_tab import DualListBoxes
from src.reactor_system import simpleReactor, liquidReactor
from src.simulator_tolerances import simulatorTolerances
from src.model_tolerances import modelTolerances
from src.quantummechanics_tab import quantumMechanics
from src.mlEstimator import mlEstimator
from src.pressureDependence import pressureDependence
from src.uncertainty_analysis import uncertaintyAnalysis
from src.miscellaneous_opts import miscellaneousOptions
from src.generateSpeciesConstraint import generateSpeciesConstraint
from src.RestartFromSeed import restartFromSeedMechanism
import webbrowser

# New imports
import customtkinter
from src.datasource_tab_v2 import thermoDatabase
from src.datasource_kinetic import kineticDatabase

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x600")

        self.title("My App")
        
        custom_style = ttk.Style()
        #sv_ttk.set_theme("dark")
        custom_style.configure("CustomNotebook.TNotebook", tabposition="wn", tabmargins=[10, 10, 10, 0])
        custom_style.configure("CustomNotebook.TNotebook.Tab", padding=[5, 5], font=("Arial", 14), foreground="#555", background="#ccc")

        # Create a notebook widget
        self.notebook = ttk.Notebook(self, style="CustomNotebook.TNotebook")
        self.notebook.pack(fill="both", expand=True)
        
        menu = tk.Menu(self)
        self.config(menu=menu)
        
        
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.exitProgram)
        
        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        
        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

        self.datasources_tab = ttk.Frame(self.notebook)
        self.deprecated_tab = ttk.Frame(self.notebook)
        self.species_tab = ttk.Frame(self.notebook)
        self.reactors_tab = ttk.Frame(self.notebook)
        self.liquid_reactor_tab = ttk.Frame(self.notebook)
        self.simulator_tolerances_tab = ttk.Frame(self.notebook)
        self.model_tolerance_tab = ttk.Frame(self.notebook)
        self.quantummechanics_tab = ttk.Frame(self.notebook)
        self.mlEstimator_tab = ttk.Frame(self.notebook)
        self.pressure_tab = ttk.Frame(self.notebook)
        self.uncertainty_tab = ttk.Frame(self.notebook)
        self.miscellaneous_tab = ttk.Frame(self.notebook)
        self.generate_species_constraint_tab = ttk.Frame(self.notebook)
        self.restart_from_seed_tab = ttk.Frame(self.notebook)
        self.generate_file_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.datasources_tab, text="Data Sources")
        self.notebook.add(self.deprecated_tab, text="Deprecated")
        self.notebook.add(self.species_tab, text='Species Generator')
        self.notebook.add(self.reactors_tab, text='simpleReactor Generator')
        self.notebook.add(self.liquid_reactor_tab, text='liquidReactor Generator')
        self.notebook.add(self.simulator_tolerances_tab, text='simulatorTolerances Generator')
        self.notebook.add(self.model_tolerance_tab, text='modelTolerances Generator')
        self.notebook.add(self.quantummechanics_tab, text='QuantumMechanics Generator')
        self.notebook.add(self.mlEstimator_tab, text='MLEstimator Generator')
        self.notebook.add(self.pressure_tab, text='Pressure Dependence Generator')
        self.notebook.add(self.uncertainty_tab, text='Uncertainty Analysis Generator')
        self.notebook.add(self.miscellaneous_tab, text='Miscellaneous Options Generator')
        self.notebook.add(self.generate_species_constraint_tab, text='Generate Species Constraint')
        self.notebook.add(self.restart_from_seed_tab, text='Restart From Seed Mechanism')
        self.notebook.add(self.generate_file_tab, text="Generate Input File")

        self.deprecated_tab_label = thermoDatabase(self.deprecated_tab)
        self.deprecated_tab_label.grid(row=0, column=0)
        self.kinetic_sources = kineticDatabase(self.deprecated_tab)
        self.kinetic_sources.grid(row=1, column=0)
        #self.reaction_sources = ReactionSources(self.deprecated_tab)
        #self.reaction_sources.grid(row=0, column=15)
        
        
        self.datasource_tab_label = DualListBoxes(self.datasources_tab)
        self.datasource_tab_label.pack(fill='both', expand=True)
        self.species_tab_label = Species(self.species_tab)
        self.reactors_tab_label = simpleReactor(self.reactors_tab, self.species_tab_label)
        self.liquid_reactor_tab_label = liquidReactor(self.liquid_reactor_tab, self.species_tab_label)
        self.simulator_tolerances_tab_label = simulatorTolerances(self.simulator_tolerances_tab)
        self.model_tolerances_tab_label = modelTolerances(self.model_tolerance_tab)
        self.quantummechanics_tab_label = quantumMechanics(self.quantummechanics_tab)
        self.mlEstimator_tab_label = mlEstimator(self.mlEstimator_tab)
        self.pressure_tab_label = pressureDependence(self.pressure_tab)
        self.uncertainty_tab_label = uncertaintyAnalysis(self.uncertainty_tab)
        self.miscellaneous_tab_label = miscellaneousOptions(self.miscellaneous_tab)
        self.generate_species_constraint_tab_label = generateSpeciesConstraint(self.generate_species_constraint_tab)
        self.restart_from_seed_tab_label = restartFromSeedMechanism(self.restart_from_seed_tab)
        
        
        self.generate_file_tab_label = GenerateFile(self.generate_file_tab,
                                                    datasource_tab= self.datasource_tab_label,
                                                    species_tab= self.species_tab_label,
                                                    reactors_tab= self.reactors_tab_label,
                                                    liquid_tab = self.liquid_reactor_tab_label,
                                                    simulatortol_tab = self.simulator_tolerances_tab_label,
                                                    model_tab= self.model_tolerances_tab_label,
                                                    options_tab= self.miscellaneous_tab_label,
                                                    pdep_tab= self.pressure_tab_label,
                                                    generate_species_constraint_tab= self.generate_species_constraint_tab_label,
                                                    quantummechanics_tab= self.quantummechanics_tab_label,
                                                    mlEstimator_tab= self.mlEstimator_tab_label,
                                                    uncertainty_tab= self.uncertainty_tab_label,
                                                    restart_from_seed_tab= self.restart_from_seed_tab_label)
    def exitProgram(self):
        exit()
        
    
    def about(self):
        self.about_window = tk.Toplevel(self)
        self.about_window.title("About")
        self.about_window.geometry("400x400")
        self.about_window.resizable(False, False)
        self.about_window.grab_set()
        self.about_window.focus_set()
        self.about_window.transient(self)
        self.about_window.protocol("WM_DELETE_WINDOW", self.about_window.destroy)
        self.about_window.bind("<Escape>", lambda e: self.about_window.destroy())
        self.about_window.bind("<Return>", lambda e: self.about_window.destroy())

        #Center labels
        self.about_label = ttk.Label(self.about_window, text="RMG-Py Input File Generator")
        self.about_label.place(relx=0.5, rely=0.5, anchor='center')
        self.about_label = ttk.Label(self.about_window, text="Version 1.0")
        self.about_label.place(relx=0.5, rely=0.6, anchor='center')
        self.about_label = ttk.Label(self.about_window, text="Developed by: Calvin Pieters")
        self.about_label.place(relx=0.5, rely=0.7, anchor='center')
        self.about_label_link = ttk.Label(self.about_window, text="https://github.com/Laxzal/RMG-GUI", foreground="blue", cursor="hand2")
        self.about_label_link.place(relx=0.5, rely=0.8, anchor='center')
        self.about_label_link.bind("<Button-1>", lambda e: self.callback("https://github.com/Laxzal/RMG-GUI"))
        
    def callback(self,url):
        webbrowser.open_new(url)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()