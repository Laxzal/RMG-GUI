import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Species(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        #self.master.title('Species File Generator')
        self.label = tk.Label(self, text="Species Generator")
        self.label.pack(pady=5, padx=5)
        
        # set default number of species blocks
        self.num_species_blocks = tk.StringVar()
        self.num_species_blocks.set('1')
        
        # create dropdown menu to select number of species blocks
        num_species_menu_label = tk.Label(self.master, text='Number of Species Blocks:')
        num_species_menu_label.grid(row=0, column=0)
        num_species_menu = ttk.Combobox(self.master, width=2, textvariable=self.num_species_blocks, state='readonly')
        num_species_menu.grid(row=0, column=1)
        num_species_menu['values'] = ('1', '2', '3', '4', '5')
        num_species_menu.bind('<<ComboboxSelected>>', self.on_select)
        num_species_menu.current(0)
        
        # create button to generate file
        #generate_button = tk.Button(self.master, text='Generate', command=self.generate_file)
        #generate_button.grid(row=10, column=6, columnspan=2, pady=10)
        
        # create list to store species blocks
        self.species_blocks = []
        self.species_labels_blocks = []
        self.species_checks = []
        self.on_select()
        
    def on_select(self, event=None):
        # clear existing species blocks
        for block in self.species_blocks:
            block.destroy()
        self.species_blocks = []
        self.species_checks = []
        
        for block in self.species_labels_blocks:
            block.destroy()
        self.species_labels_blocks = []
        
        # create new species blocks
        num_blocks = int(self.num_species_blocks.get())
        for i in range(num_blocks):
            species_label = tk.Label(self.master, text=f'Species {i+1}:')
            species_label.grid(row=i+2, column=0, padx=5, pady=5, sticky='e')
            species_label_entry = tk.Entry(self.master, width=50)
            species_label_entry.grid(row=i+2, column=1, padx=5, pady=5, sticky='w')
            
            species_smiles = tk.Label(self.master, text=f'SMILES {i+1}:')
            species_smiles.grid(row=i+2, column=3, padx=5, pady=5)
            species_smiles_entry = tk.Entry(self.master, width=50)
            species_smiles_entry.grid(row=i+2, column=4, padx=5, pady=5, sticky='w')

            reactive_var = tk.BooleanVar()
            reactive_var.set(0)
            reactive_check = tk.Checkbutton(self.master, text="Reactive", variable=reactive_var)
            reactive_check.grid(row=i+2, column=5, padx=5, pady=5)

            self.species_blocks.append(species_label_entry)
            self.species_blocks.append(species_smiles_entry)
            self.species_checks.append(reactive_var)
            self.species_labels_blocks.append(species_label)
            self.species_labels_blocks.append(species_smiles)
            self.species_labels_blocks.append(reactive_check)
    
    def spec_noinput_error(self):
            species = []
            for entry in self.species_blocks:
                if entry.get() == '':
                    messagebox.showerror('Error', 'Please enter all species information')
                    return None, None
                species.append(entry.get())
            return self.species_blocks, self.species_checks