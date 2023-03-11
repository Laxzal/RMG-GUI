import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk


class generateSpeciesConstraint(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 14 Frames
        self.frame_specs = ttk.Frame(self.master)
        self.frame_specs.grid(row=0, column=0, sticky='nsew')
        self.frame0 = ttk.Frame(self.master)
        self.frame0.grid(row=1, column=0, sticky='nsew')
        self.frame1 = ttk.Frame(self.master)
        self.frame1.grid(row=2, column=0, sticky='nsew')
        self.frame2 = ttk.Frame(self.master)
        self.frame2.grid(row=3, column=0, sticky='nsew')
        self.frame3 = ttk.Frame(self.master)
        self.frame3.grid(row=4, column=0, sticky='nsew')
        self.frame4 = ttk.Frame(self.master)
        self.frame4.grid(row=5, column=0, sticky='nsew')
        self.frame5 = ttk.Frame(self.master)
        self.frame5.grid(row=6, column=0, sticky='nsew')
        self.frame6 = ttk.Frame(self.master)
        self.frame6.grid(row=7, column=0, sticky='nsew')
        self.frame7 = ttk.Frame(self.master)
        self.frame7.grid(row=8, column=0, sticky='nsew')
        self.frame8 = ttk.Frame(self.master)
        self.frame8.grid(row=9, column=0, sticky='nsew')
        self.frame9 = ttk.Frame(self.master)
        self.frame9.grid(row=10, column=0, sticky='nsew')
        self.frame10 = ttk.Frame(self.master)
        self.frame10.grid(row=11, column=0, sticky='nsew')
        self.frame11 = ttk.Frame(self.master)
        self.frame11.grid(row=12, column=0, sticky='nsew')
        self.frame12 = ttk.Frame(self.master)
        self.frame12.grid(row=13, column=0, sticky='nsew')
        self.frame13 = ttk.Frame(self.master)
        self.frame13.grid(row=14, column=0, sticky='nsew')

        # Create a checkbox to allow the user to select whether they want to generate a species constraint
        self.generate_spec_constraints_label = ttk.Label(self.frame_specs, text='Generate Species Constraints')
        self.generate_spec_constraints_label.grid(row=0, column=0, sticky='w')
        self.generateSpeciesConstraint_var = tk.BooleanVar()
        self.generateSpeciesConstraint_var.set(False)
        self.generateSpeciesConstraint_checkbox = ttk.Checkbutton(self.frame_specs, variable=self.generateSpeciesConstraint_var)
        self.generateSpeciesConstraint_checkbox.grid(row=0, column=1, sticky='w')
        

        # Create a label called allowed with an entry box and let the user know they can use a comma to separate multiple species
        self.allowedLabel = ttk.Label(self.frame0, text='Allowed Species')
        self.allowedLabel.grid(row=0, column=0, sticky='w')
        self.allowedEntry = ttk.Entry(self.frame0)
        self.allowedEntry.grid(row=0, column=1, sticky='w')
        self.allowedLabel2 = ttk.Label(self.frame0, text='(Separate multiple species with a comma)')
        self.allowedLabel2.grid(row=0, column=2, sticky='w')

        # Create a label called maximumCarbonAtoms with an entry box that only accepts integers
        self.maximumCarbonAtomsLabel = ttk.Label(self.frame1, text='Maximum Carbon Atoms')
        self.maximumCarbonAtomsLabel.grid(row=1, column=0, sticky='w')
        self.maximumCarbonAtomsEntry = ttk.Entry(self.frame1, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumCarbonAtomsEntry.grid(row=1, column=1, sticky='w')

        # Create a label called maximumOxygenAtoms with an entry box that only accepts integers
        self.maximumOxygenAtomsLabel = ttk.Label(self.frame2, text='Maximum Oxygen Atoms')
        self.maximumOxygenAtomsLabel.grid(row=2, column=0, sticky='w')
        self.maximumOxygenAtomsEntry = ttk.Entry(self.frame2, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumOxygenAtomsEntry.grid(row=2, column=1, sticky='w')

        # Create a label called maximumNitrogenAtoms with an entry box that only accepts integers
        self.maximumNitrogenAtomsLabel = ttk.Label(self.frame3, text='Maximum Nitrogen Atoms')
        self.maximumNitrogenAtomsLabel.grid(row=3, column=0, sticky='w')
        self.maximumNitrogenAtomsEntry = ttk.Entry(self.frame3, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumNitrogenAtomsEntry.grid(row=3, column=1, sticky='w')

        # Create a label called maximumSiliconAtoms with an entry box that only accepts integers
        self.maximumSiliconAtomsLabel = ttk.Label(self.frame4, text='Maximum Silicon Atoms')
        self.maximumSiliconAtomsLabel.grid(row=4, column=0, sticky='w')

        self.maximumSiliconAtomsEntry = ttk.Entry(self.frame4, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumSiliconAtomsEntry.grid(row=4, column=1, sticky='w')

        # Create a label called maximumSulfurAtoms with an entry box that only accepts integers
        self.maximumSulfurAtomsLabel = ttk.Label(self.frame5, text='Maximum Sulfur Atoms')
        self.maximumSulfurAtomsLabel.grid(row=5, column=0, sticky='w')
        self.maximumSulfurAtomsEntry = ttk.Entry(self.frame5, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumSulfurAtomsEntry.grid(row=5, column=1, sticky='w')

        #Create a label called maximumHeavyAtoms with an entry box that only accepts integers
        self.maximumHeavyAtomsLabel = ttk.Label(self.frame6, text='Maximum Heavy Atoms')
        self.maximumHeavyAtomsLabel.grid(row=6, column=0, sticky='w')
        self.maximumHeavyAtomsEntry = ttk.Entry(self.frame6, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumHeavyAtomsEntry.grid(row=6, column=1, sticky='w')

        # Create a label called maximumSurfaceSites with an entry box that only accepts integers
        self.maximumSurfaceSitesLabel = ttk.Label(self.frame7, text='Maximum Surface Sites')
        self.maximumSurfaceSitesLabel.grid(row=7, column=0, sticky='w')
        self.maximumSurfaceSitesEntry = ttk.Entry(self.frame7, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumSurfaceSitesEntry.grid(row=7, column=1, sticky='w')

        # Create a label called maximumRadicalElectrons with an entry box that only accepts integers
        self.maximumRadicalElectronsLabel = ttk.Label(self.frame8, text='Maximum Radical Electrons')
        self.maximumRadicalElectronsLabel.grid(row=8, column=0, sticky='w')
        self.maximumRadicalElectronsEntry = ttk.Entry(self.frame8, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumRadicalElectronsEntry.grid(row=8, column=1, sticky='w')

        # Create a label called maximumSingletCarbenes with an entry box that only accepts integers
        self.maximumSingletCarbenesLabel = ttk.Label(self.frame9, text='Maximum Singlet Carbenes')
        self.maximumSingletCarbenesLabel.grid(row=9, column=0, sticky='w')
        self.maximumSingletCarbenesEntry = ttk.Entry(self.frame9, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumSingletCarbenesEntry.grid(row=9, column=1, sticky='w')

        # Create a label called maximumCarbeneRadicals with an entry box that only accepts integers
        self.maximumCarbeneRadicalsLabel = ttk.Label(self.frame10, text='Maximum Carbene Radicals')
        self.maximumCarbeneRadicalsLabel.grid(row=10, column=0, sticky='w')
        self.maximumCarbeneRadicalsEntry = ttk.Entry(self.frame10, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumCarbeneRadicalsEntry.grid(row=10, column=1, sticky='w')

        # Create a label called maximumIsotopicAtoms with an entry box that only accepts integers
        self.maximumIsotopicAtomsLabel = ttk.Label(self.frame11, text='Maximum Isotopic Atoms')
        self.maximumIsotopicAtomsLabel.grid(row=11, column=0, sticky='w')
        self.maximumIsotopicAtomsEntry = ttk.Entry(self.frame11, validate='key', validatecommand=(self.register(self.validateInt), '%P'))
        self.maximumIsotopicAtomsEntry.grid(row=11, column=1, sticky='w')

        # Create a label called  allowSingletO2 with a drop down menu that only has '' , 'True', and 'False' as options
        self.allowSingletO2Label = ttk.Label(self.frame12, text='Allow Singlet O2')
        self.allowSingletO2Label.grid(row=12, column=0, sticky='w')
        self.allowSingletO2Entry = ttk.Combobox(self.frame12, values=['', 'True', 'False'])
        self.allowSingletO2Entry.grid(row=12, column=1, sticky='w')
        self.allowSingletO2Entry.current(2)


    def validateInt(self, P):
        if P.isdigit():
            return True
        elif P == '':
            return True
        else:
            return False
    
    def generate_spec_constraints(self):
        
        # user selects to use spec constraints
        if self.generateSpeciesConstraint_var.get() == 1:
            
            #Get all the values from the entry boxes
            self.allowd_values = self.allowedEntry.get()
            self.wordsplit = self.allowed_values.split(',')
            for i in range(len(self.wordsplit)):
                self.wordsplit[i] = "'" + self.wordsplit[i].strip() + "'"
                
            self.allowd_values = ','.join(self.wordsplit)
            
            
            self.maximum_carbon_atoms = self.maximumCarbonAtomsEntry.get()
            self.maximum_oxygen_atoms = self.maximumOxygenAtomsEntry.get()
            self.maximum_nitrogen_atoms = self.maximumNitrogenAtomsEntry.get()
            self.maximum_silicon_atoms = self.maximumSiliconAtomsEntry.get()
            self.maximum_sulfur_atoms = self.maximumSulfurAtomsEntry.get()
            self.maximum_heavy_atoms = self.maximumHeavyAtomsEntry.get()
            self.maximum_surface_sites = self.maximumSurfaceSitesEntry.get()
            self.maximum_radical_electrons = self.maximumRadicalElectronsEntry.get()
            self.maximum_singlet_carbenes = self.maximumSingletCarbenesEntry.get()
            self.maximum_carbene_radicals = self.maximumCarbeneRadicalsEntry.get()
            self.maximum_isotopic_atoms = self.maximumIsotopicAtomsEntry.get()
            self.allow_singlet_o2 = self.allowSingletO2Entry.get()
            
            # Create a dictionary with all the values
            return {'allowed': self.allowd_values, 
                    'maximumCarbonAtoms': self.maximum_carbon_atoms, 
                    'maximumOxygenAtoms': self.maximum_oxygen_atoms, 
                    'maximumNitrogenAtoms': self.maximum_nitrogen_atoms, 
                    'maximumSiliconAtoms': self.maximum_silicon_atoms, 
                    'maximumSulfurAtoms': self.maximum_sulfur_atoms, 
                    'maximumHeavyAtoms': self.maximum_heavy_atoms, 
                    'maximumSurfaceSites': self.maximum_surface_sites, 
                    'maximumRadicalElectrons': self.maximum_radical_electrons, 
                    'maximumSingletCarbenes': self.maximum_singlet_carbenes, 
                    'maximumCarbeneRadicals': self.maximum_carbene_radicals, 
                    'maximumIsotopicAtoms': self.maximum_isotopic_atoms, 
                    'allowSingletO2': self.allow_singlet_o2}
        else:
            return None