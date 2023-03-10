import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from species_tab import Species
import sv_ttk
from generatefile_tab import GenerateFile
from deprecated_tab import ThermoSources, ReactionSources
from datasource_tab import DualListBoxes
from reactor_system import simpleReactor, liquidReactor
from simulator_tolerances import simulatorTolerances
from model_tolerances import modelTolerances
from quantummechanics_tab import quantumMechanics
from mlEstimator import mlEstimator
from pressureDependence import pressureDependence
from uncertainty_analysis import uncertaintyAnalysis
from miscellaneous_opts import miscellaneousOptions
from generateSpeciesConstraint import generateSpeciesConstraint
from RestartFromSeed import restartFromSeedMechanism

class MainApp(tk.Tk):
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

        self.thermo_sources = ThermoSources(self.deprecated_tab)
        self.thermo_sources.grid(row=0, column=0)
        self.reaction_sources = ReactionSources(self.deprecated_tab)
        self.reaction_sources.grid(row=0, column=15)
        
        
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
                                                    pdep_tab= self.pressure_tab_label)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()