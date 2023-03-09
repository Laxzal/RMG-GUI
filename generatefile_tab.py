import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import customtkinter as ctk


class GenerateFile(ctk.CTkFrame):
    def __init__(self, master, datasource_tab, tab1):
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
        self.tab1 = tab1
        self.datasource_tab = datasource_tab
        
    def email_noinput_error(self):
        if not self.email_entry.get():
            messagebox.showerror("Error", "Please enter your email address")
            return False
        return self.email_entry.get()
    
    def generate_file(self):
        
        species_blocks, species_checks = self.tab1.spec_noinput_error()
        email = self.email_noinput_error() 
        thermo, kinetics, seedmech = self.datasource_tab.datasource_items()
        thermo = ', '.join(['"{}"'.format(value) for value in thermo])
        kinetics = ', '.join(['"{}"'.format(value) for value in kinetics])
        seedmech = ', '.join(['"{}"'.format(value) for value in seedmech])
        
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
            
            
            file_content_datasource = f"database(\n\tthermoLibraries = [{thermo}],\n\treactionLibraries = [{kinetics}],\n\tseedMechanisms = [{seedmech}],\n\tkineticsDepositories = ['training'],\n\tkineticsFamilies = 'default',\n\tkineticsEstimator = 'rate rules'\n)"
            
            # create file contents SPECIES
            file_content_species = f"species(\n    label='{species_label[0]}',\n    reactive={species_reactive[0]},\n    structure={species_adj_smiles_choice[0]}('{species_adj_smiles[0]}'),\n)\n\n"
            if len(species_adj_smiles) > 1:
                for i in range(1, len(species_adj_smiles)):
                    file_content_species += f"species(\n    label='{species_label[i]}',\n    reactive={species_reactive[i]},\n    structure={species_adj_smiles_choice[i]}('{species_adj_smiles[i]}'),\n)\n\n"
            
            
            email_list = []
            email_list.append(email)
            file_content_email = f"email('{email_list[0]}')\n\n"
            
            
            file_path = filedialog.asksaveasfilename(defaultextension='.py', filetypes=[('Python Files', '*.py')])
            if not file_path:
                return
            # write file
            with open(file_path, 'w') as f:
                f.write(file_content_datasource)
                f.write("""\n\n""")
                f.write(file_content_species)
                f.write(file_content_email)
        # show success message
        success_label = tk.Label(self.frame0, text='File saved successfully!', fg='green')
        success_label.grid(row=2, column=0, columnspan=2, pady=10)
