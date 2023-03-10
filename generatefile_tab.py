import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import customtkinter as ctk


class GenerateFile(ctk.CTkFrame):
    def __init__(self, master, datasource_tab = None, species_tab=None, reactors_tab= None, liquid_tab = None,
                 simulatortol_tab = None, model_tab = None, options_tab = None, pdep_tab = None):
        super().__init__(master)
        self.master = master
        
        # Create Frame
        self.frame0 = ttk.Frame(self.master)
        self.frame0.place(relx=0.5, rely=0.5, anchor='center')
        
        self.email_label = tk.Label(self.frame0, text="Enter your email:")
        self.email_label.grid(row=0, column=0, sticky='w')
        
        self.email_entry = tk.Entry(self.frame0)
        self.email_entry.grid(row=0, column=1, sticky='w')
        
        self.generate_button = tk.Button(self.frame0, text="Generate output file", command=self.generate_file)
        self.generate_button.grid(row=1, column=0, pady=10)
        self.datasource_tab = datasource_tab
        self.species_tab = species_tab
        self.reactors_tab = reactors_tab
        self.liquid_tab = liquid_tab
        self.simulatortol_tab = simulatortol_tab
        self.model_tab = model_tab
        self.options_tab = options_tab
        self.pdep_tab = pdep_tab
    def email_noinput_error(self):
        if not self.email_entry.get():
            messagebox.showerror("Error", "Please enter your email address")
            return False
        return self.email_entry.get()
    
    def generate_file(self):
        
        species_blocks, species_checks = self.species_tab.spec_noinput_error()
        email = self.email_noinput_error() 

        
        if email and species_blocks and species_checks:
            # create list of species SMILES from user input
            species_label = []
            species_adj_smiles_choice = []
            species_adj_smiles = []
            species_reactive = []
            for i in range(0, len(species_blocks), 3):
                species_label.append(species_blocks[i].get())
                species_adj_smiles_choice.append(species_blocks[i+1].get())
                species_adj_smiles.append(species_blocks[i+2].get())
            for i in range(0, len(species_checks)):
                species_reactive.append(species_checks[i].get())
            
            
            
            # create file contents SPECIES
            print(species_blocks)
            print(species_adj_smiles_choice)
            if species_adj_smiles_choice[0] == 'SMILES':
                file_content_species = f"species( \n    label='{species_label[0]}',\n    reactive={species_reactive[0]},\n    structure={species_adj_smiles_choice[0]}('{species_adj_smiles[0]}'),\n)\n\n"
            else:
                file_content_species = f"species(\n    label='{species_label[0]}',\n    reactive={species_reactive[0]},\n    structure={species_adj_smiles_choice[0]}({species_adj_smiles[0]}),\n)\n\n"
            if len(species_adj_smiles) > 1:
                for i in range(1, len(species_adj_smiles)):
                    if species_adj_smiles_choice[i] == 'SMILES':
                        file_content_species += f"species(\n    label='{species_label[i]}',\n    reactive={species_reactive[i]},\n    structure={species_adj_smiles_choice[i]}('{species_adj_smiles[i]}'),\n)\n\n"
                    else:
                        file_content_species += f"species(\n    label='{species_label[i]}',\n    reactive={species_reactive[i]},\n    structure={species_adj_smiles_choice[i]}({species_adj_smiles[i]}),\n)\n\n"

            email_list = []
            email_list.append(email)
            file_content_email = f"email('{email_list[0]}')\n\n"
            
            
            # Database
            thermo, kinetics, seedmech = self.datasource_tab.datasource_items()
            thermo = ', '.join(['"{}"'.format(value) for value in thermo])
            kinetics = ', '.join(['"{}"'.format(value) for value in kinetics])
            seedmech = ', '.join(['"{}"'.format(value) for value in seedmech])
            
            file_content_datasource = f"database(\n\tthermoLibraries = [{thermo}],\n\treactionLibraries = [{kinetics}],\n\tseedMechanisms = [{seedmech}],\n\tkineticsDepositories = ['training'],\n\tkineticsFamilies = 'default',\n\tkineticsEstimator = 'rate rules'\n)"
            
            # Species
            
                # create list of species SMILES from user input
            species_label = []
            species_adj_smiles_choice = []
            species_adj_smiles = []
            species_reactive = []
            for i in range(0, len(species_blocks), 3):
                species_label.append(species_blocks[i].get())
                species_adj_smiles_choice.append(species_blocks[i+1].get())
                species_adj_smiles.append(species_blocks[i+2].get())
            for i in range(0, len(species_checks)):
                species_reactive.append(species_checks[i].get())
            
            # Reaction Systems - simpleReactor & liquidReactor
            
                # simpleReactor
                
        self.simpleReactor_dict = self.reactors_tab.generate_simplereactor()
        file_content_simplereactor = None
        if self.simpleReactor_dict is not None:
            file_content_simplereactor = "simpleReactor(\n\t"
            print(self.simpleReactor_dict)
            for key, value in self.simpleReactor_dict.items():
                # Check for temperature
                if key == 'temperature':
                        file_content_simplereactor += f"temperature = ('{value}','K'),\n\t"
                # Check for pressure
                if key == 'pressure':
                    if value is not None:
                        file_content_simplereactor += f"pressure = ('{value}','bar'),\n\t"
                # Check for initialMoleFractions
                if key == 'initialMoleFractions':
                    file_content_simplereactor += f'initialMoleFractions = {{\n\t'
                    if value is not None:
                        for key, values in value.items():
                            if values is not None:
                                file_content_simplereactor += f"\t'{key}': {values},\n\t"
                    file_content_simplereactor += f"}},\n\t"
                # Check for nSims
                if key == 'nSims' and value is not None:
                    file_content_simplereactor += f"nSims = {value},\n\t"
                
                # Check for terminationConversion
                if key == 'terminationConversion' and value is not None:
                    file_content_simplereactor += f"terminationConversion = {{\n\t"
                    for key, value in value.items():
                        if value is not None:
                            file_content_simplereactor += f"\t'{key}': {value},\n\t"
                    file_content_simplereactor += f"}},\n\t"
                
                # Check for terminationTime
                if key == 'terminationTime' and value is not None:
                    file_content_simplereactor += f"terminationTime = ({value},'s'),\n\t"
                
                # Check for terminationRateRatio
                if key == 'terminationRateRatio' and value is not None:
                    file_content_simplereactor += f"terminationRateRatio = {value},\n\t"
                
                # Check for sensitivity
                if key == 'sensitivity' and value is not None:
                    file_content_simplereactor += f"sensitivity = ["
                    for value_item in value:
                        value_item = value_item[0]
                        file_content_simplereactor += f"'{value_item}'"
                    file_content_simplereactor += f"],\n\t"
                
                # Check for sensitivityThreshold
                if key == 'sensitivityThreshold' and value is not None:
                    file_content_simplereactor += f"sensitivityThreshold = {value},\n\t"
            file_content_simplereactor += ")\n\t"
            # liquidReactor
            
        self.liquidreactor_dict = self.liquid_tab.generate_liquidreactor()
        file_content_liquidreactor = None
        if self.liquidreactor_dict is not None:
            file_content_liquidreactor = "liquidReactor(\n\t"
            print(self.liquidreactor_dict)
            for key, value in self.liquidreactor_dict.items():
                # Check for temperature
                if key == 'temperature':
                    if value is not None:
                        file_content_liquidreactor += f"temperature = ('{value}','K'),\n\t"
                # Check for pressure
                if key == 'pressure':
                    if value is not None:
                        file_content_liquidreactor += f"pressure = ('{value}','bar'),\n\t"
                # Check for initialConcentrations
                if key == 'initialConcentrations':
                    file_content_liquidreactor += f'initialConcentrations= {{\n\t'
                    if value is not None or value != {}:
                        for key, values in value.items():
                            if values is not None or key != '':
                                file_content_liquidreactor += f"\t'{key}': {values},\n\t"
                    file_content_liquidreactor += f"}},\n\t"
                # Check for nSims
                if key == 'nSims' and value is not None:
                    file_content_liquidreactor += f"nSims = {value},\n\t"
                
                # Check for terminationConversion
                if key == 'terminationConversion' and value is not None:
                    file_content_liquidreactor += f"terminationConversion = {{\n\t"
                    for key, value in value.items():
                        if value is not None:
                            file_content_liquidreactor += f"\t'{key}': {value},\n\t"
                    file_content_liquidreactor += f"}},\n\t"
                
                # Check for terminationTime
                if key == 'terminationTime' and value is not None:
                    file_content_liquidreactor += f"terminationTime = ({value},'s'),\n\t"
                
                # Check for terminationRateRatio
                if key == 'terminationRateRatio' and value is not None:
                    file_content_liquidreactor += f"terminationRateRatio = {value},\n\t"
                
                # Check for sensitivity
                if key == 'sensitivity' and value is not None:
                    file_content_liquidreactor += f"sensitivity = ["
                    for value_item in value:
                        value_item = value_item[0]
                        file_content_liquidreactor += f"'{value_item}'"
                    file_content_liquidreactor += f"],\n\t"
                
                # Check for sensitivityThreshold
                if key == 'sensitivityThreshold' and value is not None:
                    file_content_liquidreactor += f"sensitivityThreshold = {value},\n\t"
        
        
            file_content_liquidreactor += ")\n\t"
    
    
            # Simulator
        simulatortol_dict = self.simulatortol_tab.generate_sim_tol()
        file_content_simulatortol = None
        
        if simulatortol_dict is not None:
            file_content_simulatortol = "simulator(\n\t"
            for key, value in simulatortol_dict.items():
                if key == 'atol':
                    file_content_simulatortol += f"atol = {value},\n\t"
                if key == 'rtol':
                    file_content_simulatortol += f"rtol = {value},\n\t"
                if key == 'sens_atol':
                    file_content_simulatortol += f"sens_atol = {value},\n\t"
                if key == 'sens_rtol':
                    file_content_simulatortol += f"sens_rtol = {value},\n\t"
            
            file_content_simulatortol += ")\n\t"
        
            # Model
        model_dict = self.model_tab.generate_model_tol()
        file_content_model = None
        
        if model_dict is not None:
            file_content_model = "model(\n\t"
            for key, value in model_dict.items():
                if key == 'toleranceKeepInEdge':
                    if value is not None:
                        file_content_model += f"toleranceKeepInEdge = {value},\n\t"
                if key == 'toleranceMoveToCore':
                    if value is not None:
                        file_content_model += f"toleranceMoveToCore = {value},\n\t"
                if key == 'toleranceInterruptSimulation':
                    if value is not None:
                        file_content_model += f"toleranceInterruptSimulation = {value},\n\t"
                if key == 'maximumEdgeSpecies':
                    if value is not None:
                        file_content_model += f"maximumEdgeSpecies = {value},\n\t"
                if key == 'minCoreSizeForPrune':
                    if value is not None:    
                        file_content_model += f"minCoreSizeForPrune = {value},\n\t"
                if key == 'maxNumObjsPerIter':
                    if value is not None:
                        file_content_model += f"maxNumObjsPerIter = {value},\n\t"
                if key == 'terminateAtMaxObjects':
                    if value is not None:
                        file_content_model += f"terminateAtMaxObjects = {value},\n\t"
                if key == 'toleranceMoveEdgeReactionToCore':
                    if value is not None:
                        file_content_model += f"toleranceMoveEdgeReactionToCore = {value},\n\t"
                if key == 'toleranceMoveEdgeReactionToCoreInterrupt':
                    if value is not None:    
                        file_content_model += f"toleranceMoveEdgeReactionToCoreInterrupt = {value},\n\t"
                if key == 'toleranceMoveSurfaceSpeciesToCore':
                    if value is not None:
                        file_content_model += f"toleranceMoveSurfaceSpeciesToCore = {value},\n\t"
                if key == 'toleranceMoveSurfaceReactionToCore':
                    if value is not None:
                        file_content_model += f"toleranceMoveSurfaceReactionToCore = {value},\n\t"
                if key == 'toleranceMoveEdgeReactionToSurface':
                    if value is not None:
                        file_content_model += f"toleranceMoveEdgeReactionToSurface = {value},\n\t"
                if key == 'toleranceThermoKeepSpeciesInEdge':
                    if value is not None:
                        file_content_model += f"toleranceThermoKeepSpeciesInEdge = {value},\n\t"
                if key == 'minSpeciesExistIterationsForPrune':
                    if value is not None:
                        file_content_model += f"minSpeciesExistIterationsForPrune = {value},\n\t"
                if key == 'filterReactions':
                    if value is not None:    
                        file_content_model += f"filterReactions = {value},\n\t"
                if key == 'filterThreshold':
                    if value is not None:
                        file_content_model += f"filterThreshold = {value},\n\t"
            file_content_model += ")\n\t"
            
            # Options
        options_dict = self.options_tab.generate_options()
        file_content_options = None
        
        if options_dict is not None:
            file_content_options = f"options(\n\t"
            for key, value in options_dict.items():
                if key == 'name':
                    if value is not None:
                        file_content_options += f"name='{value}',\n\t"
                if key == 'generateSeedEachIteration':
                    if value is not None:
                        file_content_options += f"generateSeedEachIteration={value},\n\t"
                if key == 'saveSeedToDatabase':
                    if value is not None:
                        file_content_options += f"saveSeedToDatabase={value},\n\t"
                if key == 'units':
                    if value is not None:
                        file_content_options += f"units='{value}',\n\t"
                if key == 'generateOutputHTML':
                    if value is not None:
                        file_content_options += f"generateOutputHTML={value},\n\t"
                if key == 'generatePlots':
                    if value is not None:
                        file_content_options += f"generatePlots={value},\n\t"
                if key == 'saveSimulationProfiles':
                    if value is not None:
                        file_content_options += f"saveSimulationProfiles={value},\n\t"
                if key == 'verboseComments':
                    if value is not None:
                        file_content_options += f"verboseComments={value},\n\t"
                if key == 'saveEdgeSpecies':
                    if value is not None:
                        file_content_options += f"saveEdgeSpecies={value},\n\t"
                if key == 'keepIrreversible':
                    if value is not None:
                        file_content_options += f"keepIrreversible={value},\n\t"
                if key == 'trimolecularProductReversible':
                    if value is not None:
                        file_content_options += f"trimolecularProductReversible={value},\n\t"
                if key == 'saveSeedModulus':
                    if value is not None:
                        file_content_options += f"saveSeedModulus={value},\n\t"
            file_content_options += ")\n\t"
                        

            # pressureDependence
        self.pressure_dependence_dict = self.pdep_tab.generate_pdep()
        file_content_pdep = None
        
        if self.pressure_dependence_dict is not None:
            file_content_pdep = f"pressureDependence(\n\t"
            for key, value in self.pressure_dependence_dict.items():
                if key == 'method':
                    if value is not None:
                        file_content_pdep += f"method='{value}',\n\t"
                if key == 'maximumGrainSize':
                    if value is not None:
                        file_content_pdep += f"maximumGrainSize=({value},'kcal/mol'),\n\t"
                if key == 'minimumNumberOfGrains':
                    if value is not None:
                        file_content_pdep += f"minimumNumberOfGrains={value},\n\t"
                if key == 'temperature':
                    if value is not None:
                        file_content_pdep += f"temperature=({value}),\n\t"
                if key == 'pressure':
                    if value is not None:
                        file_content_pdep += f"pressure=({value}),\n\t"
                if key == 'interpolation':
                    if value is not None:
                        file_content_pdep += f"interpolation='({value})',\n\t"
                if key == 'maximumAtoms':
                    if value is not None:
                        file_content_pdep += f"maximumAtoms={value},\n\t"
            file_content_pdep += ")\n\t"
            
            # generated species constraints
            
            # Quantum Mechanics
            
            # ml Estimator
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        file_path = filedialog.asksaveasfilename(defaultextension='.py', filetypes=[('Python Files', '*.py')])
        if not file_path:
            return
        # write file
        with open(file_path, 'w') as f:
            f.write(file_content_datasource)
            f.write("""\n\n""")
            f.write(file_content_species)
            f.write("""\n\n""")
            if file_content_simplereactor:
                f.write(file_content_simplereactor)
                f.write("""\n\n""")
            if file_content_liquidreactor:
                f.write(file_content_liquidreactor)
                f.write("""\n\n""")
            if file_content_simulatortol:
                f.write(file_content_simulatortol)
                f.write("""\n\n""")
            if file_content_model:
                f.write(file_content_model)
                f.write("""\n\n""")
            if file_content_options:
                f.write(file_content_options)
                f.write("""\n\n""")
            if file_content_pdep:
                f.write(file_content_pdep)
                f.write("""\n\n""")
            f.write(file_content_email)
        # show success message
        success_label = tk.Label(self.frame0, text='File saved successfully!', fg='green')
        success_label.grid(row=2, column=0, columnspan=2, pady=10)
