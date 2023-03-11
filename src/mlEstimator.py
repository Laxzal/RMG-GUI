import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class mlEstimator(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 17 Frames
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
        self.frame13 = ttk.Frame(self.master)
        self.frame13.grid(row=13, column=0, sticky='nsew')
        self.frame14 = ttk.Frame(self.master)
        self.frame14.grid(row=14, column=0, sticky='nsew')
        self.frame15 = ttk.Frame(self.master)
        self.frame15.grid(row=15, column=0, sticky='nsew')
        self.frame16 = ttk.Frame(self.master)
        self.frame16.grid(row=16, column=0, sticky='nsew')

        # Create a lable and tick box for using mlEstimator
        self.useMlEstimator = tk.IntVar()
        self.useMlEstimator.set(0)
        self.useMlEstimatorLabel = ttk.Label(self.frame0, text='Use mlEstimator')
        self.useMlEstimatorLabel.grid(row=0, column=0, sticky='w')
        self.useMlEstimatorCheck = ttk.Checkbutton(self.frame0, variable=self.useMlEstimator)
        self.useMlEstimatorCheck.grid(row=0, column=1, sticky='w')

        # Create a label for thermo and drop down with '' and True and False
        self.thermoLabel = ttk.Label(self.frame1, text='Thermo')
        self.thermoLabel.grid(row=0, column=0, sticky='w')
        self.thermo = tk.StringVar()
        self.thermo.set('')
        self.thermoDropDown = ttk.Combobox(self.frame1, textvariable=self.thermo, values=['', 'True', 'False'])
        self.thermoDropDown.grid(row=0, column=1, sticky='w')

        # Create a label for name and entry box
        self.nameLabel = ttk.Label(self.frame2, text='Name')
        self.nameLabel.grid(row=0, column=0, sticky='w')
        self.name = tk.StringVar()
        self.name.set('')
        self.nameEntry = ttk.Entry(self.frame2, textvariable=self.name)
        self.nameEntry.grid(row=0, column=1, sticky='w')

        #Create a label for minHeavyAtoms and an entry box that only takes integers 0 and above
        self.minHeavyAtomsLabel = ttk.Label(self.frame3, text='Min Heavy Atoms')
        self.minHeavyAtomsLabel.grid(row=0, column=0, sticky='w')
        self.minHeavyAtoms = tk.IntVar()
        self.minHeavyAtoms.set(0)
        self.minHeavyAtomsEntry = ttk.Entry(self.frame3, textvariable=self.minHeavyAtoms)
        self.minHeavyAtomsEntry.grid(row=0, column=1, sticky='w')
        self.minHeavyAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for maxHeavyAtoms and an entry box that only takes integers 0 and above
        self.maxHeavyAtomsLabel = ttk.Label(self.frame4, text='Max Heavy Atoms')
        self.maxHeavyAtomsLabel.grid(row=0, column=0, sticky='w')
        self.maxHeavyAtoms = tk.IntVar()
        self.maxHeavyAtoms.set(0)
        self.maxHeavyAtomsEntry = ttk.Entry(self.frame4, textvariable=self.maxHeavyAtoms)
        self.maxHeavyAtomsEntry.grid(row=0, column=1, sticky='w')
        self.maxHeavyAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for minCarbonAtoms and an entry box that only takes integers 0 and above
        self.minCarbonAtomsLabel = ttk.Label(self.frame5, text='Min Carbon Atoms')
        self.minCarbonAtomsLabel.grid(row=0, column=0, sticky='w')
        self.minCarbonAtoms = tk.IntVar()
        self.minCarbonAtoms.set(0)
        self.minCarbonAtomsEntry = ttk.Entry(self.frame5, textvariable=self.minCarbonAtoms)
        self.minCarbonAtomsEntry.grid(row=0, column=1, sticky='w')
        self.minCarbonAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for maxCarbonAtoms and an entry box that only takes integers 0 and above
        self.maxCarbonAtomsLabel = ttk.Label(self.frame6, text='Max Carbon Atoms')
        self.maxCarbonAtomsLabel.grid(row=0, column=0, sticky='w')
        self.maxCarbonAtoms = tk.IntVar()
        self.maxCarbonAtoms.set(0)
        self.maxCarbonAtomsEntry = ttk.Entry(self.frame6, textvariable=self.maxCarbonAtoms)
        self.maxCarbonAtomsEntry.grid(row=0, column=1, sticky='w')
        self.maxCarbonAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for minOxygenAtoms and an entry box that only takes integers 0 and above
        self.minOxygenAtomsLabel = ttk.Label(self.frame7, text='Min Oxygen Atoms')
        self.minOxygenAtomsLabel.grid(row=0, column=0, sticky='w')
        self.minOxygenAtoms = tk.IntVar()
        self.minOxygenAtoms.set(0)
        self.minOxygenAtomsEntry = ttk.Entry(self.frame7, textvariable=self.minOxygenAtoms)
        self.minOxygenAtomsEntry.grid(row=0, column=1, sticky='w')
        self.minOxygenAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for maxOxygenAtoms and an entry box that only takes integers 0 and above
        self.maxOxygenAtomsLabel = ttk.Label(self.frame8, text='Max Oxygen Atoms')
        self.maxOxygenAtomsLabel.grid(row=0, column=0, sticky='w')
        self.maxOxygenAtoms = tk.IntVar()
        self.maxOxygenAtoms.set(0)
        self.maxOxygenAtomsEntry = ttk.Entry(self.frame8, textvariable=self.maxOxygenAtoms)
        self.maxOxygenAtomsEntry.grid(row=0, column=1, sticky='w')
        self.maxOxygenAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for minNitrogenAtoms and an entry box that only takes integers 0 and above
        self.minNitrogenAtomsLabel = ttk.Label(self.frame9, text='Min Nitrogen Atoms')
        self.minNitrogenAtomsLabel.grid(row=0, column=0, sticky='w')
        self.minNitrogenAtoms = tk.IntVar()
        self.minNitrogenAtoms.set(0)
        self.minNitrogenAtomsEntry = ttk.Entry(self.frame9, textvariable=self.minNitrogenAtoms)
        self.minNitrogenAtomsEntry.grid(row=0, column=1, sticky='w')
        self.minNitrogenAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))


        # Create a label for maxNitrogenAtoms and an entry box that only takes integers 0 and above
        self.maxNitrogenAtomsLabel = ttk.Label(self.frame10, text='Max Nitrogen Atoms')
        self.maxNitrogenAtomsLabel.grid(row=0, column=0, sticky='w')
        self.maxNitrogenAtoms = tk.IntVar()
        self.maxNitrogenAtoms.set(0)
        self.maxNitrogenAtomsEntry = ttk.Entry(self.frame10, textvariable=self.maxNitrogenAtoms)
        self.maxNitrogenAtomsEntry.grid(row=0, column=1, sticky='w')
        self.maxNitrogenAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for onlyCyclics and a drop down that has '' and 'True' and 'False'
        self.onlyCyclicsLabel = ttk.Label(self.frame11, text='Only Cyclics')
        self.onlyCyclicsLabel.grid(row=0, column=0, sticky='w')
        self.onlyCyclics = tk.StringVar()
        self.onlyCyclics.set('')
        self.onlyCyclicsEntry = ttk.Combobox(self.frame11, textvariable=self.onlyCyclics, values=['', 'True', 'False'], state='readonly')
        self.onlyCyclicsEntry.grid(row=0, column=1, sticky='w')

        # Create a laebl for OnlyHeterocyclics and a drop down that has '' and 'True' and 'False'
        self.onlyHeterocyclicsLabel = ttk.Label(self.frame12, text='Only Heterocyclics')
        self.onlyHeterocyclicsLabel.grid(row=0, column=0, sticky='w')
        self.onlyHeterocyclics = tk.StringVar()
        self.onlyHeterocyclics.set('')
        self.onlyHeterocyclicsEntry = ttk.Combobox(self.frame12, textvariable=self.onlyHeterocyclics, values=['', 'True', 'False'], state='readonly')
        self.onlyHeterocyclicsEntry.grid(row=0, column=1, sticky='w')
         
        # Create a label for minCycleOverlap and an entry box that only takes integers 0 and above
        self.minCycleOverlapLabel = ttk.Label(self.frame13, text='Min Cycle Overlap')
        self.minCycleOverlapLabel.grid(row=0, column=0, sticky='w')
        self.minCycleOverlap = tk.IntVar()
        self.minCycleOverlap.set(0)
        self.minCycleOverlapEntry = ttk.Entry(self.frame13, textvariable=self.minCycleOverlap)
        self.minCycleOverlapEntry.grid(row=0, column=1, sticky='w')
        self.minCycleOverlapEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))



        # Create a label for H298UncertaintyCutOff and an entry box that only takes floats and the label also has measurement of kcal/mol
        self.H298UncertaintyCutOffLabel = ttk.Label(self.frame14, text='H298 Uncertainty Cut Off (kcal/mol)')
        self.H298UncertaintyCutOffLabel.grid(row=0, column=0, sticky='w')
        self.H298UncertaintyCutOff = tk.DoubleVar()
        self.H298UncertaintyCutOff.set(0.0)
        self.H298UncertaintyCutOffEntry = ttk.Entry(self.frame14, textvariable=self.H298UncertaintyCutOff)
        self.H298UncertaintyCutOffEntry.grid(row=0, column=1, sticky='w')
        self.H298UncertaintyCutOffEntry.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))


        # Create a lable for S298UncertaintyCutOff and an entry box that only takes floats and the label also has measurement of cal/mol/K
        self.S298UncertaintyCutOffLabel = ttk.Label(self.frame15, text='S298 Uncertainty Cut Off (cal/mol/K)')
        self.S298UncertaintyCutOffLabel.grid(row=0, column=0, sticky='w')
        self.S298UncertaintyCutOff = tk.DoubleVar()
        self.S298UncertaintyCutOff.set(0.0)
        self.S298UncertaintyCutOffEntry = ttk.Entry(self.frame15, textvariable=self.S298UncertaintyCutOff)
        self.S298UncertaintyCutOffEntry.grid(row=0, column=1, sticky='w')
        self.S298UncertaintyCutOffEntry.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))

        # Create a label for CpUncertaintyCutOff and an entry box that only takes floats and the label also has measurement of cal/mol/K
        self.CpUncertaintyCutOffLabel = ttk.Label(self.frame16, text='Cp Uncertainty Cut Off (cal/mol/K)')
        self.CpUncertaintyCutOffLabel.grid(row=0, column=0, sticky='w')
        self.CpUncertaintyCutOff = tk.DoubleVar()
        self.CpUncertaintyCutOff.set(0.0)
        self.CpUncertaintyCutOffEntry = ttk.Entry(self.frame16, textvariable=self.CpUncertaintyCutOff)
        self.CpUncertaintyCutOffEntry.grid(row=0, column=1, sticky='w')
        self.CpUncertaintyCutOffEntry.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))



    def validateFloat(self, P):
        if P == '':
            return True
        try:
            float(P)
            return True
        except ValueError:
            return False

    def validateInt(self, P):
        if P == '':
            return True
        try:
            int(P)
            return True
        except ValueError:
            return False

    def generate_mlestimator(self):
        
        if self.useMlEstimator.get() == 1:

            # Get all the values from the entry boxes
            self.thermo_val = self.thermoDropDown.get() if self.thermoDropDown.get() != '' else None
            self.name_val = self.name.get() if self.name.get() != '' else None
            self.minHeavyAtoms_val = self.minHeavyAtoms.get() if self.minHeavyAtoms.get() != '' else None
            self.maxHeavyAtoms_val = self.maxHeavyAtoms.get() if self.maxHeavyAtoms.get() != '' else None
            self.minCarbonAtoms_val = self.minCarbonAtoms.get() if self.minCarbonAtoms.get() != '' else None
            self.maxCarbonAtoms_val = self.maxCarbonAtoms.get() if self.maxCarbonAtoms.get() != '' else None
            self.minOxygenAtoms_val = self.minOxygenAtoms.get() if self.minOxygenAtoms.get() != '' else None
            self.maxOxygenAtoms_val = self.maxOxygenAtoms.get() if self.maxOxygenAtoms.get() != '' else None
            self.minNitrogenAtoms_val = self.minNitrogenAtoms.get() if self.minNitrogenAtoms.get() != '' else None
            self.maxNitrogenAtoms_val = self.maxNitrogenAtoms.get() if self.maxNitrogenAtoms.get() != '' else None
            self.onlyCyclics_val = self.onlyCyclicsEntry.get() if self.onlyCyclicsEntry.get() != '' else None
            self.onlyHeterocyclics_val = self.onlyHeterocyclicsEntry.get() if self.onlyHeterocyclicsEntry.get() != '' else None
            self.minCycleOverlap_val = self.minCycleOverlapEntry.get() if self.minCycleOverlapEntry.get() != '' else None
            self.H298UncertaintyCutOffEntry_val = self.H298UncertaintyCutOffEntry.get() if self.H298UncertaintyCutOffEntry.get() != '' else None
            self.S298UncertaintyCutOffEntry_val = self.S298UncertaintyCutOffEntry.get() if self.S298UncertaintyCutOffEntry.get() != '' else None
            self.CpUncertaintyCutOffEntry_val = self.CpUncertaintyCutOffEntry.get() if self.CpUncertaintyCutOffEntry.get() != '' else None
            
            # Create a dictionary of all the values
            return {'thermo': self.thermo_val, 
                    'name': self.name_val, 
                    'minHeavyAtoms': self.minHeavyAtoms_val, 
                    'maxHeavyAtoms': self.maxHeavyAtoms_val, 
                    'minCarbonAtoms': self.minCarbonAtoms_val, 
                    'maxCarbonAtoms': self.maxCarbonAtoms_val, 
                    'minOxygenAtoms': self.minOxygenAtoms_val, 
                    'maxOxygenAtoms': self.maxOxygenAtoms_val, 
                    'minNitrogenAtoms': self.minNitrogenAtoms_val, 
                    'maxNitrogenAtoms': self.maxNitrogenAtoms_val, 
                    'onlyCyclics': self.onlyCyclics_val, 
                    'onlyHeterocyclics': self.onlyHeterocyclics_val, 
                    'minCycleOverlap': self.minCycleOverlap_val, 
                    'H298UncertaintyCutOff': self.H298UncertaintyCutOffEntry_val, 
                    'S298UncertaintyCutOff': self.S298UncertaintyCutOffEntry_val, 
                    'CpUncertaintyCutOff': self.CpUncertaintyCutOffEntry_val}
        
        else:
            return None