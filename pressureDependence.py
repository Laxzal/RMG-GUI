import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter as ctk

class pressureDependence(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Create 8 frames
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

    # Create a tick box in gui to use Pressure Dependence
        self.use_pressure_dependence = tk.BooleanVar()
        self.use_pressure_dependence.set(0)
        self.use_pressure_dependence_check = tk.Checkbutton(self.frame0, text="Use Pressure Dependence", variable=self.use_pressure_dependence)
        self.use_pressure_dependence_check.grid(row=0, column=0, padx=5, pady=5)

        # Create a lable and a drop down menu with options that are 'Modified Strong Collision' and 'Rservoir State'
        self.pressure_dependence_type_label = tk.Label(self.frame1, text='Pressure Dependence Method:')
        self.pressure_dependence_type_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.pressure_dependence_type = ttk.Combobox(self.frame1, width=40, state='readonly')
        self.pressure_dependence_type.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.pressure_dependence_type['values'] = ('Modified Strong Collision', 'Reservoir State')
        self.pressure_dependence_type.current(0)

        # Create a label called maximumGrainSize and a measurement of kcal/mol and just entry box to enter that allows float only
        self.maximumGrainSize_label = tk.Label(self.frame2, text='Maximum Grain Size (kcal/mol):')
        self.maximumGrainSize_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.maximumGrainSize = tk.Entry(self.frame2, width=10)
        self.maximumGrainSize.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.maximumGrainSize.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))


        # Create a label for minimumNumberOfGrains and an entry box that allows only float
        self.minimumNumberOfGrains_label = tk.Label(self.frame3, text='Minimum Number of Grains:')
        self.minimumNumberOfGrains_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.minimumNumberOfGrains = tk.Entry(self.frame3, width=10)
        self.minimumNumberOfGrains.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.minimumNumberOfGrains.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))

        # Create a lable for temperatures that has two entry boxes to represent the range of temperatures and a separator between them and then another label for temp measurement and an entry box for the measurement and another label that says step size and an entry box to represent the step size that only allows integer positive numbers
        self.temperatures_label = tk.Label(self.frame4, text='Temperatures:')
        self.temperatures_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.temperatures = tk.Entry(self.frame4, width=10)
        self.temperatures.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.temperatures.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))
        self.temperatures_separator = tk.Label(self.frame4, text=' - ')
        self.temperatures_separator.grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.temperatures2 = tk.Entry(self.frame4, width=10)
        self.temperatures2.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        self.temperatures2.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))
        self.temperatures_measurement = tk.Label(self.frame4, text='Measurement:')
        self.temperatures_measurement.grid(row=0, column=4, padx=5, pady=5, sticky='e')
        self.temperatures_step_size = tk.Entry(self.frame4, width=10)
        self.temperatures_step_size.grid(row=0, column=5, padx=5, pady=5, sticky='w')
        #self.temperatures_step_size.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))
        self.temperatures_step_size_label = tk.Label(self.frame4, text='Step Size:')
        self.temperatures_step_size_label.grid(row=0, column=6, padx=5, pady=5, sticky='e')
        self.temperatures_step_size_entry = tk.Entry(self.frame4, width=10)
        self.temperatures_step_size_entry.grid(row=0, column=7, padx=5, pady=5, sticky='w')
        self.temperatures_step_size_entry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

        # Create a label for pressures that has two entry boxes to represent the range of pressures and a separator between them and then another label for pressure measurement and an entry box for the measurement and another label that says step size and an entry box to represent the step size that only allows integer positive numbers
        self.pressures_label = tk.Label(self.frame5, text='Pressures:')
        self.pressures_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.pressures = tk.Entry(self.frame5, width=10)
        self.pressures.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.pressures.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))
        self.pressures_separator = tk.Label(self.frame5, text=' - ')
        self.pressures_separator.grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.pressures2 = tk.Entry(self.frame5, width=10)
        self.pressures2.grid(row=0, column=3, padx=5, pady=5, sticky='w')
        self.pressures2.config(validate='key', validatecommand=(self.register(self.validateFloat), '%P'))
        self.pressures_measurement = tk.Label(self.frame5, text='Measurement:')
        self.pressures_measurement.grid(row=0, column=4, padx=5, pady=5, sticky='e')
        self.pressures_measurement_entry = tk.Entry(self.frame5, width=10)
        self.pressures_measurement_entry.grid(row=0, column=5, padx=5, pady=5, sticky='w')
        self.pressures_step_size_label = tk.Label(self.frame5, text='Step Size:')
        self.pressures_step_size_label.grid(row=0, column=6, padx=5, pady=5, sticky='e')
        self.pressures_step_size = tk.Entry(self.frame5, width=10)
        self.pressures_step_size.grid(row=0, column=7, padx=5, pady=5, sticky='w')
        self.pressures_step_size.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))


        # Create a label for interpolation with a drop down that has 'PDepArrhenius' and 'Chebyshev' and if 'Chebyshev' is selected then a label for Temperature Basis Function and an entry box that only takes integers 0 and above and a label for Pressure Basis Function and an entry box that only takes integers 0 and above
        self.interpolationLabel = ttk.Label(self.frame6, text='Interpolation')
        self.interpolationLabel.grid(row=0, column=0, sticky='w')
        self.interpolation = tk.StringVar()
        self.interpolation.set('PDepArrhenius')
        self.interpolationEntry = ttk.Combobox(self.frame6, textvariable=self.interpolation, values=['PDepArrhenius', 'Chebyshev'], state='readonly')
        self.interpolationEntry.grid(row=0, column=1, sticky='w')
        self.interpolationEntry.bind('<<ComboboxSelected>>', self.interpolationSelected)

        # Create a label for maximum Atoms and an entry box that only takes integers 0 and above
        self.maximumAtomsLabel = ttk.Label(self.frame9, text='Maximum Atoms')
        self.maximumAtomsLabel.grid(row=0, column=0, sticky='w')
        self.maximumAtoms = tk.IntVar()
        self.maximumAtoms.set('')
        self.maximumAtomsEntry = ttk.Entry(self.frame9, textvariable=self.maximumAtoms)
        self.maximumAtomsEntry.grid(row=0, column=1, sticky='w')
        self.maximumAtomsEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

    def interpolationSelected(self, event):
        self.interpolation = self.interpolationEntry.get()
        if self.interpolation == 'Chebyshev':
            self.interpolationEntry.set('Chebyshev')
            self.TemperatureBasisFunctionLabel = ttk.Label(self.frame7, text='Temperature Basis Function')
            self.TemperatureBasisFunctionLabel.grid(row=0, column=0, sticky='w')
            self.TemperatureBasisFunction = tk.IntVar()
            self.TemperatureBasisFunction.set(0)
            self.TemperatureBasisFunctionEntry = ttk.Entry(self.frame7, textvariable=self.TemperatureBasisFunction)
            self.TemperatureBasisFunctionEntry.grid(row=0, column=1, sticky='w')
            self.TemperatureBasisFunctionEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

            self.PressureBasisFunctionLabel = ttk.Label(self.frame8, text='Pressure Basis Function')
            self.PressureBasisFunctionLabel.grid(row=0, column=0, sticky='w')
            self.PressureBasisFunction = tk.IntVar()
            self.PressureBasisFunction.set(0)
            self.PressureBasisFunctionEntry = ttk.Entry(self.frame8, textvariable=self.PressureBasisFunction)
            self.PressureBasisFunctionEntry.grid(row=0, column=1, sticky='w')
            self.PressureBasisFunctionEntry.config(validate='key', validatecommand=(self.register(self.validateInt), '%P'))

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
        elif P == '0':
            return False
        try:
            int(P)
            return True
        except ValueError:
            return False